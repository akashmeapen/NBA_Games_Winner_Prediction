from nba_api.stats.endpoints import LeagueGameFinder
import pandas as pd

gamefinder = LeagueGameFinder(season_nullable='2023-24')  # e.g., 2023-24 season
games = gamefinder.get_data_frames()[0]
print(games.head())
