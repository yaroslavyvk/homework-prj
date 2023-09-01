import csv

with open('score_players.csv', mode='r') as file1:
    reader = csv.reader(file1)
    player_score = [row for row in reader]

high_scores = {}
for player, score in player_score[1:]:
    if player in high_scores:
        if score > high_scores[player]:
            high_scores[player] = score
    else:
        high_scores[player] = score

sort_high_scores = sorted(high_scores.items(), key=lambda item: item[1], reverse=True)

with open('high_scores.csv', mode='w') as file2:
    writer = csv.writer(file2)
    writer.writerow(['Player Name', 'Highest Score'])
    writer.writerows(sort_high_scores)
