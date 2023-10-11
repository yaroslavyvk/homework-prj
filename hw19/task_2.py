import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv')

selected_columns = df[['Team', 'Yellow Cards', 'Red Cards']]

num_teams = df['Team'].nunique()
print(f"{num_teams} teams participated in the Euro2012.")

teams_more_than_6_goals = df[df['Goals'] > 6]
print(teams_more_than_6_goals['Team'])
