import backend.data_processor as data_processor
import scraper
import pandas as pd


def main():
    print('hello')\
    # Scrape and download yearly roster data 
    scraper.scrape_yearly_roster_data()
    # Read the downloaded HTML into pandas Series so that player lists can be accessed. 
    # Create one large dictionary to map each player to all of their teammates
    # Convert this dictionary to json  
    data_processor.load_roster_data()


if __name__ == '__main__':
    main()
