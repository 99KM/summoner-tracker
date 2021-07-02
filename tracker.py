# IMPORT REQUESTS

import requests

def requestSummonerData(region, summonerName, APIKey):
    # make url
    URL1 = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    # requests.get goes to the url we made and gives us back a json
    response1 = requests.get(URL1)
    return response1.json()

def requestRankedData(region, ID, APIKey):
    URL2 = "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + ID + "?api_key=" + APIKey
    print(URL2)
    response2 = requests.get(URL2)
    return response2.json()

def main():
    print("\nEnter your region to get started")
    print("Type in one the following regions for the player you wish to search for:\n")
    print("NA1 | EUW1 | EUN1 | BR1 | KR1 | JP1 | LA1 | LA2 | OC1 | TR1 | RU1\n")

    # ask the user for region, summoner name, and API Key
    # only three things I need from them in order to get create my URL and grab their ID

    region = (str)(input('Type in one of the regions above: '))
    summonerName = (str)(input('Type your Summoner Name here (do not include any spaces): '))
    APIKey = (str)(input('Copy and paste your API Key here:'))

    # send these three pieces off to requestData function which creates URL and gives me back JSON that has the ID for that specific summoner
    response1 = requestSummonerData(region, summonerName, APIKey)

    print("ID FOR", summonerName, "=", response1['id'])

    ID = (str)(input('Copy and paste the ID you just got here: '))

    response2 = requestRankedData(region, ID, APIKey)
    print("SUMMONER NAME =", response2[0]["summonerName"])
    print("QUEUE =", response2[0]["queueType"])
    print("RANK =", response2[0]["tier"], response2[0]["rank"])
    print("LP =", response2[0]["leaguePoints"])
    print("WINS =", response2[0]["wins"])
    print("LOSSES =", response2[0]["losses"])
    print("WIN RATE =", round(((response2[0]["wins"])/(response2[0]["losses"]+response2[0]["wins"])) * 100))


if __name__ == "__main__":
    main()
    input('Press ENTER to exit')