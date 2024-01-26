import pandas as pd
import scraper
import json
from io import StringIO


def add_all_teammate_links(roster_df: pd.DataFrame, teammate_map: dict):
    """
    Adds all the teammates links from the roster dataframe to each player's
    set of teammates.
    """
    # Formats the player name to also include their college in parantheses to
    # distinguish b/w players who have the same name

    # Lambda to convert each row player name to the formatted player name
    # Apply lambda to each row and assign the result back to the 'Player' col
    roster_df["Player"] = roster_df.apply(
        func=lambda row: f"{row['Player']} ({row['College']})"
        , axis=1)

    # Map each player name to their teammates
    for player in roster_df["Player"]:
        # Exclude the current player from the teammates list
        teammates = roster_df[roster_df["Player"] != player]["Player"]
        # Add all teammates to the player's set of teammates
        teammate_map[player] = teammate_map.get(player, set()).union(teammates)


def load_roster_data():
    """
    Load roster data for each team for each year.

    :raises FileNotFoundError: If HTML file is not found.
    :raises ValueError: If no tables are in the HTML file.
    """
    teammate_map = {}
    # Create a series
    for year in scraper.years:
        for abrv in scraper.team_abbreviations_to_team_names:
            yearly_roster_path = scraper.get_file_path(year, abrv)
            try:
                # Read HTML content from the file
                with open(yearly_roster_path, 'r') as file:
                    html_content = StringIO(file.read())
                # Convert the HTML content into a pandas dataframe
                # The yearly roster table is the 0th table in the HTML
                roster_df: pd.DataFrame = pd.read_html(html_content)[0]
                add_all_teammate_links(roster_df, teammate_map)
            except (ValueError, FileNotFoundError):
                # Some teams do not have a roster each year,
                # ex. San Diego after the chargers moved to LA
                continue

    # Convert sets to lists for JSON serialization
    for player in teammate_map:
        teammate_map[player] = list(teammate_map[player])
    # Convert dictionary to JSON string
    json_data = json.dumps(teammate_map)

    # Save JSON data to a file
    player_data_path = f'../teammate_map_{scraper.years[0]}-' \
                       f'{scraper.years[-1]}.json'
    with open(player_data_path, 'w') as file:
        file.write(json_data)
        file.close()
    print('hooray')
