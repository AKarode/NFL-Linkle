import time
import os
import requests
import urllib3
from bs4 import BeautifulSoup

# Disable insecure request warnings, since the website we are scraping from
# is missing an SSL  certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Each URL is of the form /rosters.nsf/Annual/<year>-<team_abbreviation>.html
base_url = 'https://www.jt-sw.com/football/pro/rosters.nsf/Annual/{}-{}'
team_abbreviations_to_team_names = {
    # Current team abbreviations as of 2019
    'arz': 'Arizona Cardinals',
    'atl': 'Atlanta Falcons',
    'bal': 'Baltimore Ravens',
    'buf': 'Buffalo Bills',
    'car': 'Carolina Panthers',
    'chi': 'Chicago Bears',
    'cin': 'Cincinnati Bengals',
    'cle': 'Cleveland Browns',
    'dal': 'Dallas Cowboys',
    'den': 'Denver Broncos',
    'det': 'Detroit Lions',
    'gb': 'Green Bay Packers',
    'hou': 'Houston Texans',
    'ind': 'Indianapolis Colts',
    'jac': 'Jacksonville Jaguars',
    'kc': 'Kansas City Chiefs',
    'lac': 'Los Angeles Chargers',
    'lam': 'Los Angeles Rams',
    'mia': 'Miami Dolphins',
    'min': 'Minnesota Vikings',
    'ne': 'New England Patriots',
    'no': 'New Orleans Saints',
    'nyg': 'New York Giants',
    'nyj': 'New York Jets',
    'oak': 'Oakland Raiders',
    'phi': 'Philadelphia Eagles',
    'pit': 'Pittsburgh Steelers',
    'sf': 'San Francisco 49ers',
    'sea': 'Seattle Seahawks',
    'tb': 'Tampa Bay Buccaneers',
    'ten': 'Tennessee Titans',
    'was': 'Washington Redskins',
    # Include teams whose name / city has changed before 2019
    'sd': 'San Diego Chargers',
    'stl': 'St. Louis Rams'
}

#  A list of years (integers) for which player data will be scraped.
# 'Hou' maps to both the houston oilers (1995-1996), can the houston texans (
# after 1997)
# It is best to start at 1997 to avoid issues like this
# The dataset only goes until 2019
years = [year for year in range(1997, 2019)]


def get_file_path(year, team_abbreviation):
    # Define the path to the yearly_roster_data relative to this script
    current_dir = __file__.rstrip('scraper.py')
    parent_dir = current_dir + '../'
    roster_dir = parent_dir + 'yearly_roster_data/'
    file_name = f'{year}-{team_abbreviation}.html'
    file_path = roster_dir + file_name
    return file_path


def make_request(url):
    """
    Make a GET request to the given URL with retries.

    :param url: The URL to send the GET request to.
    :return: Response object if successful.
    :raises InvalidURL: If the URL is unknown.
    :raises TooManyRedirects: If max retries are reached due to too many
    redirects.
    :raises RequestException: For unknown request errors.
    """
    retry_count = 3
    # Send a GET request to the URL
    while retry_count > 0:
        # The website we are scraping from has no SSL certificate
        response = requests.get(url, verify=False)
        if response.status_code in (400, 404):  # Indicates a bad request
            raise requests.exceptions.InvalidURL(f'{url} is an unknown URL')
        elif response.status_code == 429:  # Indicates too many requests
            retry_count -= 1
            # Sleep for 10 seconds before making a new request
            time.sleep(10)
        elif response.status_code != 200:  # Indicates some unknown error
            raise requests.exceptions.RequestException('Unknown error with '
                                                       f'status code {response.status_code} encountered')
        else:  # If we are here, we made a successful request
            return response

    # If we are here, we ran out of retries
    raise requests.exceptions.TooManyRedirects(
        f'Reached maximum retries for url {url}.')


def download_yearly_roster_data(year, team, file_path):
    # Check if the file already exists to avoid unnecessary downloads
    if os.path.exists(file_path):
        return
    # Get the url corresponding to the current year and team
    url = base_url.format(year, team)
    # Try to make a GET request to the URL
    try:
        response = make_request(url)
    except requests.exceptions.InvalidURL:
        # If we are here, we have tried a team abbreviation for a
        # year when that team did not exist, for example the st louis
        # rams in 2019, after they had changed cities to become Los
        # Angeles Rams
        return  # simply return if we encounter an invalid URL
    except (requests.exceptions.TooManyRedirects,
            requests.exceptions.RequestException) as e:
        raise RuntimeError(
            f'Encountered {e} when making a URL request')

    with open(file_path, 'w') as f:
        # Strip the web page of unnecessary information, return the relevant
        # roster table for the given year
        roster_html = extract_roster_table_from_page(response.text)
        # Save the html table into a file in our yearly roster data folder
        # Create the file, write to it a string represenation of our data
        f.write(str(roster_html))


def extract_roster_table_from_page(page):
    """
    Extracts the player roster table from the given HTML page.

    :param page: HTML content of the web page.
    :return: BeautifulSoup object containing the MVP table.
    """
    soup = BeautifulSoup(page, 'html.parser')
    # Extract the specific table containing roster data
    # The page has 2 html tables, we want the last one
    roster_table = soup.find_all('table')[-1]
    return roster_table


def scrape_yearly_roster_data():
    """
    Scrapes & downloads yearly roster data and saves it into HTML files.
    """
    # Iterate through each year that we want to scrape rosters for  for
    for year in years:
        # For each team abbreivation name:
        for team in team_abbreviations_to_team_names:
            file_path = get_file_path(year, team)
            try:
                download_yearly_roster_data(year, team, file_path)
            except FileExistsError:
                # If the file already exists, we can simply continue
                continue
