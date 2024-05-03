import json
from glob import glob

countries = ['CN', 'IR', 'TM', 'SA', 'US']
blackList = set()

chinatrend = {}
totalChina = {}
censorChina = {}

irantrend = {}
totalIran = {}
censorIran = {}

ustrend = {}
totalUS = {}
censorUS = {}

turkmenistantrend = {}
totalTurkmenistan = {}
censorTurkmenistan = {}

saudiarabiatrend = {}
totalSA = {}
censorSA = {}

def updateTrendDictionary(countryDictionary, timestamp):
    if timestamp in countryDictionary:
        countryDictionary[timestamp] += 1
    else:
        countryDictionary[timestamp] = 1

def createBlackListSet():
	blackList = set()
	with open('./china.csv', 'r') as chinaCensoredSites:
        for line in chinaCensoredSites.readlines():
            if line[0] == '.':
                blackList.add(line[1:].strip().lower())
            else:
                blackList.add(line.strip().lower())
    return blackList

def generatePercentagesTimeline(censorSet, totalSet,country):
	print(f'*****Timeline for {country}*****')
	for year in censorSet:
		print(f'{year}:{round(censorSet[year]/totalSet[year], 4)*100}%')

def main():
	global blackList
	global chinatrend
	global totalChina
	global censorChina
	global irantrend
	global totalIran
	global censorIran
	global ustrend
	global censorUS
	global totalUS
	global turkmenistantrend
	global totalTurkmenistan
	global censorTurkmenistan
	global saudiarabiatrend
	global totalSA
	global censorSA
	global countries
	blackList = createBlackListSet()
	database = glob('database/*.json')
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
                    updateTrendDictionary(censorChina, timestamp)
                elif victimCountry == 'IR':
                    updateTrendDictionary(censorIran, timestamp)
                elif victimCountry == 'US':
                    updateTrendDictionary(censorUS, timestamp)
                elif victimCountry == 'TM':
                    updateTrendDictionary(censorTurkmenistan, timestamp)
                elif victimCountry == 'SA':
                    updateTrendDictionary(censorSA, timestamp)
           	if victimCountry in countries:
           		if victimCountry == 'CN':
                    updateTrendDictionary(totalChina, timestamp)
                elif victimCountry == 'IR':
                    updateTrendDictionary(totalIran, timestamp)
                elif victimCountry == 'US':
                    updateTrendDictionary(totalUS, timestamp)
                elif victimCountry == 'TM':
                    updateTrendDictionary(totalTurkmenistan, timestamp)
                elif victimCountry == 'SA':
                    updateTrendDictionary(totalSA, timestamp)


        generatePercentagesTimeline(censorChina, totalChina, 'China')
        generatePercentagesTimeline(censorIran, totalIran, 'Iran')
        generatePercentagesTimeline(censorUS, totalUS,'USA')
        generatePercentagesTimeline(censorTurkmenistan, totalTurkmenistan,'Turkmenistan')
        generatePercentagesTimeline(censorSA, totalSA,'Saudi Arabia')


if __name__ == '__main__':
	main()
