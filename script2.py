import json
from glob import glob

blackList = set()
countries = ['CN', 'IR', 'KP', 'TM', 'SA']
chinatrend = {}
irantrend = {}
northKoreatrend = {}
turkmenistantrend = {}
saudiarabiatrend = {}

def updateTrendDictionary(countryDictionary, timestamp):
    if timestamp in countryDictionary:
        countryDictionary[timestamp] += 1
    else:
        countryDictionary[timestamp] = 1

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
            else:
                blackList.add(line.strip().lower())
    database = glob('genesisvictims/*.json')
    for index, victim in enumerate(database):
        with open(victim) as victimFile:
            data = json.load(victimFile)
        try:
            victimAccounts = data['domain_names']
            victimCountry = data['country']
            timestamp = data['timestamp'][:4]
        except:
            continue
        for account in victimAccounts:
            if account.lower() in blackList and victimCountry in countries:
                if victimCountry == 'CN':
                    updateTrendDictionary(chinatrend, timestamp)
                elif victimCountry == 'IR':
                    updateTrendDictionary(irantrend, timestamp)
                elif victimCountry == 'KP':
                    updateTrendDictionary(northKoreatrend, timestamp)
                elif victimCountry == 'TM':
                    updateTrendDictionary(turkmenistantrend, timestamp)
                elif victimCountry == 'SA':
                    updateTrendDictionary(saudiarabiatrend, timestamp)
    print(f'China: {chinatrend}')
    print(f'Iran: {irantrend}')
    print(f'North Korea: {northKoreatrend}')
    print(f'Turkmenistan: {turkmenistantrend}')
    print(f'Saudia Arabia: {saudiarabiatrend}')

main()
