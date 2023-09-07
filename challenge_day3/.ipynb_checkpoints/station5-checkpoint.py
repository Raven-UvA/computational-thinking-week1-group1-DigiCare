import pandas as pd
df = pd.read_csv("teams.csv")

def solution_station_5(name):
    return int(df.loc[df['members'] == name, 'team'].values[0])

