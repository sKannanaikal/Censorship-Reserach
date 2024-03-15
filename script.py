import json
from glob import glob

chinaBlackList = set()
countries = ['CN', 'IR']
chineseAccounts = 0
chineseInfringements = 0

def main():
    global chinaBlackList
    global countries
    with open('.\\china.csv', 'r') as chinaCensoredSites:
        for line in chinaCensoredSites.readlines():
            chinaBlackList.add(line)
    database = glob('genesisivictims/*.json')
    for index, victim in enumerate(database):
        with open(victim, 'r') as victimFile:
            data = json.load(victimFile)
        victimAccounts = data['domain']
        victimCountry = data['country']
        for account in victimAccounts:
            if victimCountry == 'CN':
                chineseAccounts += 1
            if account.lower() in chinaBlackList and victimCountry == 'CN':
                chineseInfringements += 1
                print(f'[+] Victim from {victimCountry} was found accessing {account}')
    print(f'[+] Identified a total of {chineseAccounts} chinese accounts')
    print(f'[+] Identified of this total dataset there are {chineseInfringements} infringements')
    
main()