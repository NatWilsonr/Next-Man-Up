import pandas as pd
import matplotlib.pyplot as plt

games = pd.read_csv("../raw/games.csv")
details = pd.read_csv("../raw/games_details.csv")
players = pd.read_csv("../raw/players.csv")
teams = pd.read_csv("../raw/teams.csv")
rankings = pd.read_csv("../raw/ranking.csv")
games.head()
details.head()
players.head()
teams.head()
rankings.head() 
