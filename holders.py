import requests


def main():
    response = requests.get("https://api.bloxy.info/token/token_holders_list?token=0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e&key=ACCXw398IJc99&format=table")
    print(response.json())


main()