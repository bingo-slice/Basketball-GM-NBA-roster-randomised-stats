#randomise stats

import json
from random import randint


filepath = r"C:\Games\2018-19.NBA.Roster.json"
outpath = r"C:\Games\2018-19.NBA.Roster2.json"

with open(filepath, encoding='utf-8-sig') as f:
    statdata = json.load(f)

for player in statdata['players']:
    for ratings in player['ratings']:
        for stats in ratings:
            ratings[stats] = randint(1,99)

with open(outpath, 'w') as f:
    json.dump(statdata, f)
