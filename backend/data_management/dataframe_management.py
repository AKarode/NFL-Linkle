import pandas as pd
import scraper


def load_roster_data():
    """
    Load roster data for each team for each year.

    :raises FileNotFoundError: If HTML file is not found.
    :raises ValueError: If no tables are in the HTML file.
    """
    dfs = []  # Store a list to hold all of our data frames

    # Create a series
    for year in scraper.years:
        for abrv, team_name in scraper.team_abbreviations_to_team_names.items():
            file_path = scraper.get_file_path(year, abrv)
            try:
                # Load the data from the html for each year into a pandas DF
                # The yearly roster table is the 0th table in the HTML
                roster_df: pd.DataFrame = pd.read_html(file_path)[0]
                roster_df['Year'] = year
                roster_df['Team Name'] = team_name
                # Create a new DataFrame with only the required columns
                new_df = roster_df[['Team Name', 'Year', 'Player']]
                print(f'Creating df for {year, team_name}')
                dfs.append(new_df)
            except (ValueError, FileNotFoundError):
                # If the file for a given team and year does not exist,
                # it could be a situation similar to the St. Louis not having
                # the rams after they moved. We can simply do nothing
                continue
    dataframe: pd.DataFrame = pd.concat(dfs)
    dataframe.to_csv('../../yearly_rosters.csv')
    print(dataframe)
