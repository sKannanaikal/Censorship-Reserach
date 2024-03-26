import json
from glob import glob

blackList = set()
countries = ['CN', 'IR', 'KP', 'TM', 'SA']
users = 0
infringements = 0
trend = {}

def main():
    global blackList
    global countries
    global infringements
    global users
    global trend
    with open('./china.csv', 'r') as chinaCensoredSites:
        for line in chinaCensoredSites.readlines():
            if line[0] == '.':
                blackList.add(line[1:].strip().lower())
                print(line[1:].strip().lower())
            else:
                blackList.add(line.strip().lower())
                print(line.strip().lower())
    database = glob('genesisvictims/*.json')
    for index, victim in enumerate(database):
        with open(victim) as victimFile:
            data = json.load(victimFile)
        victimAccounts = data['domain_names']
        victimCountry = data['country']
        timestamp = data['timestamp'][:4]
        for country in countries:
            users = 0
            infringements = 0
            trend = {}
            for account in victimAccounts:
                if account.lower() in blackList and victimCountry == 'CN':
                    if timestamp in trend:
                        trend[timestamp] += 1
                    else:
                        trend[timestamp] = 1
            print(f'Analysis complete for {country}')
            print(trend)


    

main()
