import requests
import json
import asyncio


def main():
    allVaults = requests.get("https://vaults.finance/all")
    jsonAllVaults = json.loads(json.dumps(allVaults.json()))
    print(f'total amount of vaults {len(jsonAllVaults)}')
 
    
    for i in jsonAllVaults:   
        getHodlers(i["token"]["address"])
        

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