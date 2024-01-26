import pandas as pd
import scraper
import json


def add_all_teammate_links(roster_df: pd.DataFrame, teammate_map: dict):
    """
    Adds all of the teammates links from the roster dataframe to the each player's set of teammates.
    """
    # Formats the player name to also include their college in parantheses to distinguish b/w players who have the same name

    # Define a lambda function that takes a row and returns the formatted player name
    format_player_name = lambda row: f"{row['Player']} ({row['College']})"
    # Apply this function to each row and assign the result back to the 'Player' column
    roster_df["Player"] = roster_df.apply(format_player_name, axis=1)

    # Map each player name to their teammates
    for player in roster_df["Player"]:
        # Exclude the current player from the teammates list
        teammates = set(roster_df["Player"]) - {player}
        # Add all of the teammates to the player's list of teammates
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
            file_path = scraper.get_file_path(year, abrv)
            try:
                # Load the data from the html for each year into a pandas DF
                # The yearly roster table is the 0th table in the HTML
                roster_df: pd.DataFrame = pd.read_html(file_path)[0]
                add_all_teammate_links(roster_df, teammate_map)
            except (ValueError, FileNotFoundError):
                # Some teams do not have a roster each year, ex. San Diego after the chargers moved to LA
                continue

    # Convert dictionary to JSON string
    json_data = json.dumps(teammate_map)
    # Save JSON data to a file (optional, but recommended for backup)
    with open("../players_data.json", "w") as file:
        file.write(json_data)
