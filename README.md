# NFL-Linkle
## Overview

NFL Linkle is a web-based game, inspired by the popular Wordle concept. It challenges players to connect two NFL players through mutual teammates in six guesses or fewer. This is a full stack development project, combining a Python backend with a React JSX frontend for an engaging user experience.

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




