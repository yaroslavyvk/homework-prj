import random
import csv

players = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']
players_scores = [{'Player name': player, 'Score': random.randint(0, 1000)} for player in players for _ in range(100)]
header = ['Player name', 'Score']
with open('score_players.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(players_scores)
