import json
from glob import glob

turkmenistanContent = 0
IranianContent = 0
SuadiArabianContent = 0


def main():
    database = glob('genesisvictims/*.json')
    for index, victim in enumerate(database):
        with open(victim) as victimFile:
            data = json.load(victimFile)
        victimCountry = data['country']
        for account in victimAccounts:
            if victimCountry == 'SA':
                SuadiArabianContent += 1
            elif victimCountry == 'IR':
                IranianContent += 1
            elif victimCountry == 'TM':
                turkmenistanContent += 1

    print(f'Turkmenistan: {turkmenistanContent}')
    print(f'Iran: {IranianContent}')
    print(f'Suadi Arabia: {SuadiArabianContent}')
    
main()
