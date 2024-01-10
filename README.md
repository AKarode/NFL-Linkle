# NFL-Linkle
## Scraping 
- We scraped our information from `profootballreference.com` 
### Getting the table of active teams for the nfl for a given year
- `https://www.pro-football-reference.com/teams/`
- Stored in a table called 'Active franchises'
- Html tag: 
```html
<table id="teams_active" class = "sortable state_table now_sortable" data-cols-to-freeze=",1">
```
### Retreiving the NFL team roster
`https://www.pro-football-reference.com/teams/{abreviation}/{year_name}_roster.htm`
- where `abbreviation` is the 3-letter shortened version of a team name
- Examples:
	- `nyg` for Giants
	- `nyj` for Jets
	- `nwe` for Patriots
		- We should hardcode / precompute these / get the set of team abreviations
-  Info is in a table called `Roster`
```html
<table id="roster" class="per_match_toggle sortable stats_table now_sortable sticky_table eq2 re2 le2"  data-cols-to-freeze=",2">
```
- Sample links
	- `https://www.pro-football-reference.com/teams/mia/2011_roster.htm`
	- `https://www.pro-football-reference.com/teams/det/2021_roster.htm`
### Getting the list of teams for a given year 
- We can go to a given year, and then look at all the row team names for ranking in team offense, since all teams in the NFL will rank somewhere here 
	- We can build the list in this manner 
	- `https://www.pro-football-reference.com/years/{year_name}/#all_team_stats`
	- Where `year_name` is a numerical value like `2014`# Project Technicalities / Limitations
- Player team data is based on the team that the player finishes the year with and does not account for mid-season trades. 
	- This means that players who started off on a given team and were traded to a new team will not have teammate connections to the team they originated on entering the year. 
- Players who retire in-season 


