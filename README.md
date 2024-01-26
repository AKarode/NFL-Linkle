# NFL-Linkle
## Overview

NFL Linkle is a web-based game, inspired by the New York Times' Wordle game. It challenges players to connect two NFL players through mutual teammates in six guesses or fewer. This is a full stack development project, combining a Python backend with a React JSX frontend for an engaging user experience.

## Features

- **Interactive Gameplay**: Users engage in a challenge of linking two NFL players via mutual teammates, enhancing their knowledge of NFL player connections.
- **Dynamic Data Processing**: Employed BeautifulSoup for efficient scraping of NFL data from profootballreference.com, transforming it into a well-structured pandas DataFrame.
- **Graph-Based Data Structure**: Developed a node-based graph to represent players and their team associations per year, facilitating effective pathfinding strategies.
- **Algorithmic Pathfinding**: Integrated a Breadth-First Search (BFS) algorithm to calculate the shortest path between any two NFL players.
- **Daily Game Updates**: The game refreshes daily with a new teammate combination to guess, maintaining replayability.

## Deployment

The game is deployed online, accessible to users worldwide. It features a user-friendly interface and seamless interaction, offering a fresh and dynamic gaming experience every day.

## Project Technicalities / Limitations

- The data reflects players' end-of-year team status and doesn't cover mid-season changes, 2-way contracts, or in-season retirements.
- This means some teammate connections might be missing for players who changed teams during the year or were on practice squads.

## Scraping

- Data source: `profootballreference.com`
- Active NFL teams: Scraped from `https://www.pro-football-reference.com/teams/` under the 'Active franchises' table.
 Html table header: 
```html
<table id="teams_active" class = "sortable state_table now_sortable" data-cols-to-freeze=",1">
```
- Team rosters: Accessed from URLs like `https://www.pro-football-reference.com/teams/{abbreviation}/{year_name}_roster.htm`, where `{abbreviation}` is a 3-letter team code (e.g., `nyg` for Giants).
  Info is in a table called `Roster`
```html
<table id="roster" class="per_match_toggle sortable stats_table now_sortable sticky_table eq2 re2 le2"  data-cols-to-freeze=",2">
```
- Team lists for past years: accessed via the team statistics for the given year's page, for instance we can look at all the row team names for ranking in team offense, since all teams in the NFL will rank somewhere here 
	- We can build the list in this manner 
	- `https://www.pro-football-reference.com/years/{year_name}/#all_team_stats`
# Sample Project Strucutre
```
NFL-Linkle/
│
├── frontend/                         # Frontend React JSX files
│   ├── src/
│   │   ├── components/               # React components
│   │   │   ├── GameBoard.jsx         # Component for the game board
│   │   │   ├── PlayerCard.jsx        # Component for displaying player info
│   │   │   └── Header.jsx            # Header component
│   │   ├── App.jsx                   # Main application component
│   │   ├── index.jsx                 # Entry point for React application
│   │   └── ...
│   ├── public/
│   │   ├── index.html                # HTML template
│   │   └── ...
│   ├── package.json                  # npm package file
│   └── ...
│
├── backend/                          # Backend Python files
│   ├── data_management/              # Data scraping and cleaning
│   │   ├── scraper.py                # Script for scraping data
│   │   ├── cleaner.py                # Script for cleaning data
│   │   └── dataframe_setup.py        # Script for setting up DataFrame
│   │
│   ├── network_analysis/             # Network analysis and BFS
│   │   ├── graph_builder.py          # Script for building graph structure
│   │   ├── bfs_algorithm.py          # Script for Breadth-First Search algorithm
│   │   └── network_utils.py          # Utility functions for network analysis
│   │
│   ├── game_logic/                   # Game logic and management
│   │   ├── player_selector.py        # Logic for selecting players
│   │   ├── team_logic.py             # Logic related to team data
│   │   └── game_rules.py             # Script detailing game rules and logic
│   │
│   ├── api/                          # API and middleware
│   │   ├── api_controller.py         # Controller for API endpoints
│   │   ├── api_routes.py             # Definitions for API routes
│   │   └── api_helpers.py            # Helper functions for API
│   │
│   ├── requirements.txt              # List of Python dependencies
│   └── ...
│
├── .gitignore                        # Git ignore file
├── README.md                         # Project README
└── ...
```


Devin Tips 
- Use a server logic for player looks up, rather than storing entrie mapping client side 
- What we should send to the players: 
  - Not the 50 mb FILE - THINK 100 LB WEIGHT ANALOGY 
  - For the dropdown menu search - this is client side
    - Send JSON {{"name": "x", "id": 0},{...},...}
    - This allows search to work locally,
  - To check is a player is a teammate: 
    - but when a player name is searched and clicked, a GET request to xxxxxxx.com/api/isRelated?player1=0&player2=1
    - This API endpoint "isRelated" can be thought of like a function that takes two integer ids and determines if one contains the other as a teammate
    - The server gets the request and determines whether the players have played together or not (ex. {"related": true})
    - This makes it so very little data is exchanged over the network == fast responses
  - I'll leave the implementation logic for the search on the backend up to you, data structures too
