import requests
import json
from pandas import DataFrame
apikey = {"X-Riot-Token": "RGAPI-07508c8c-d5d1-4c66-8274-037b9f284bf3"}
url = 'https://kr.api.riotgames.com/lol/summoner/v3/summoners/by-name/'
id = '쭈노쮸노'
r = requests.get(url+id, headers=apikey)
dc = r.json()
print(dc.keys())
accountid = dc['accountId']
print(accountid)
match_url = 'https://kr.api.riotgames.com/lol/match/v3/matchlists/by-account/'

r2 = requests.get(match_url+str(accountid),headers = apikey)
dc2 = r2.json()
print(dc2['matches'])

print(dc2['matches'][0].keys())
platformId = []
gameId = []
champion = []
queue = []
season = []
timestamp = []
role = []
lane = []
for i in dc2['matches']:
    platformId.append(i['platformId'])
    gameId.append(i['gameId'])
    champion.append(i['champion'])
    queue.append(i['queue'])
    season.append(i['season'])
    timestamp.append(i['timestamp'])
    role.append(i['role'])
    lane.append(i['lane'])
dt = DataFrame({'pid' : platformId,
                'gid' : gameId,
                'champion' : champion,
                'queue' : queue,
                'season' : season,
                'timestamp' : timestamp,
                'role' : role,
                'lane' : lane})
dt.to_csv('jnjn.csv')