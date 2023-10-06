import pandas as pd
df = pd.read_csv('address.csv')

selected_columns = df[['Team', 'Yellow Cards', 'Red Cards']]

num_teams = df['Team'].count()
print(f"{num_teams} teams participated in the Euro2012.")

teams_more_than_6_goals = df[df['Goals'] > 6]
print(teams_more_than_6_goals['Team'])