import data_processor as data_processor
import scraper
import pandas as pd


def main():
    print("LFG")
    # Scrape and download yearly roster data 
    # scraper.scrape_yearly_roster_data()

    # Read HTML into pd Series so that player lists can be accessed.
    # Create one large dict to map each player to all of their teammates
    # Convert this dictionary to json and download it
    # data_processor.load_roster_data()


if __name__ == '__main__':
    main()
