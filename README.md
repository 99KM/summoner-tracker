
# KM's League Tracker

KM'S League Tracker is a simple Python-based CLI which allows the user to get the Ranked data of any League of Legends player on the ladder.

## Installation

Simply download tracker.py and run.

## Requirements

The Python package 'requests' is required to call and return the data from Riot's API.

Install by running the following in the terminal (WIN + R > 'cmd').

```bash
pip install requests
```
## How to Use

To get the program up and running, simply open 'tracker.py'. At the moment, this is script is only available as a CLI, but a GUI is in the works.

Upon opening, you will be asked to enter the region for the summoner you wish to search for.

![region](https://i.imgur.com/uB9T0KD.png)

Then, enter the Summoner Name.

![name](https://i.imgur.com/AgJQZVa.png)

You will then be asked to enter your API. [Request one here.](https://developer.riotgames.com/)  
After entering, the ID for the Summoner you entered earlier will appear.

![api](https://i.imgur.com/d6MEv7Q.png)

You will be asked to enter copy and paste the ID that was just given to you. After doing this, the Ranked data for the user you entered will be displayed.

![data](https://i.imgur.com/rYrsZjS.png)

## Script

```python
# IMPORT REQUESTS

import requests

def getID(region, summonerName, APIKey):
    # make url
    URL1 = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    # requests.get goes to the url we made and gives us back a json
    response1 = requests.get(URL1)
    return response1.json()

def getRankedData(region, ID, APIKey):
    URL2 = "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + ID + "?api_key=" + APIKey
    print(URL2)
    response2 = requests.get(URL2)
    return response2.json()

def main():
    print("Welcome!\n")
    print("Type in one the following regions for the player you wish to search for:\n")
    print("NA1 | EUW1 | EUN1 | BR1 | KR1 | JP1 | LA1 | LA2 | OC1 | TR1 | RU1\n")

    # ask the user for region, summoner name, and API Key
    # only three things I need from them in order to get create my URL and grab their ID

    region = (str)(input('Type in one of the regions above: '))
    summonerName = (str)(input('Type your Summoner Name here (do not include any spaces): '))
    APIKey = (str)(input('Copy and paste your API Key here:'))

    # send these three pieces off to getRankedData function which creates URL and gives me back a JSON that has the ID for that specific summoner
    response1 = getID(region, summonerName, APIKey)

    print("\nID FOR", summonerName, "=", response1['id'])

    ID = (str)(input('\nCopy and paste the ID you just got here: '))

    response2 = getRankedData(region, ID, APIKey)
    print("\nSUMMONER NAME =", response2[0]["summonerName"])
    print("\nQUEUE =", response2[0]["queueType"])
    print("\nRANK =", response2[0]["tier"], response2[0]["rank"])
    print("\nLP =", response2[0]["leaguePoints"])
    print("\nWINS =", response2[0]["wins"])
    print("\nLOSSES =", response2[0]["losses"])
    print("\nWIN RATE =", round(((response2[0]["wins"])/(response2[0]["losses"]+response2[0]["wins"])) * 100))


if __name__ == "__main__":
    main()
    input('\nPress ENTER to exit')
```

## Roadmap

I am in the process of developing a GUI for this application to make the process a lot more streamline. As well as this, you will (hopefully) not need to copy and paste the ID to get your data.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
