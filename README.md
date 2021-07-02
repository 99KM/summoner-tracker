
# KM's Summoner Tracker

KM's Summoner Tracker is a simple Python-based CLI which allows the user to get the Ranked data of any League of Legends player on the ladder.

## Requirements

[Python 3.4 or later.](https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe)

The Python package 'requests' is required to call and return the data from Riot's API.

Install by running the following in the terminal (WIN + R > 'cmd').

```bash
pip install requests
```

## How to Use

To get the program up and running, simply open 'tracker.py'.   
At the moment, this is script is only available as a CLI, but a GUI is in the works.

Upon opening, you will be asked to enter the region for the summoner you wish to search for.

![region](https://i.imgur.com/uB9T0KD.png)

Then, enter the Summoner Name.

![name](https://i.imgur.com/AgJQZVa.png)

You will then be asked to enter your API. [Request one here.](https://developer.riotgames.com/)  
  
  After entering, the ID for the Summoner you entered earlier will appear.

![api](https://i.imgur.com/d6MEv7Q.png)

You will be asked to enter copy and paste the ID that was just given to you.   
After doing this, the Ranked data for the user you entered will be displayed.

![data](https://i.imgur.com/rYrsZjS.png)


## Roadmap

I am in the process of developing a GUI for this application to make the process a lot more streamline.   
As well as this, you will (hopefully) not need to copy and paste the ID to get your data.

## Contributing
Pull requests are welcome.   
or major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
