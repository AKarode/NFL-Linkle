import dataframe_management
import scraper


def main():
    scraper.scrape_yearly_roster_data()
    dataframe_management.load_roster_data()


if __name__ == '__main__':
    main()
