import requests
import json
import asyncio


def main():
    allVaults = requests.get("https://vaults.finance/all")
    jsonAllVaults = json.loads(json.dumps(allVaults.json()))
    print(f'total amount of vaults {len(jsonAllVaults)}')
    wantTokensFile = open('wantTokens.json', 'w')
    wantTokens = {}
    
    for i in jsonAllVaults:  
        wantTokens[i['token']['symbol']]=i["token"]["address"]
        getHodlers(i["token"]["address"])

    json.dump(wantTokens,wantTokensFile)   

def getHodlers(address):
    params = {
        'token':address,
        'key': 'ACCXw398IJc99',
        'format': 'json'
    }

    f = open("./wantTokens/"+address+".json", "w")
    response = requests.get("https://api.bloxy.info/token/token_holders_list", params=params)
    f.write(json.dumps(response.json()))
    f.close()
    return print(response.status_code, address)




main()