import requests
import json


def getTokens():
    allVaults = requests.get("https://vaults.finance/all")
    
    print(json.dumps(allVaults.json()[0]["token"]["address"]))

def main():
    params = {
        'token':'0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e',
        'key': 'ACCXw398IJc99',
        'format': 'json'
    }

    f = open(params['token']+".json", "w")
    response = requests.get("https://api.bloxy.info/token/token_holders_list", params=params)
    f.write(json.dumps(response.json()))
    f.close()
    


getTokens()