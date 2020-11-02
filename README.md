# Piano Tiles Bot
A Bot which plays piano tiles famous game automatically.

# The Game
The bot uses coursor of the system and taps the coloured tiles as soon as they appear on the selected portion of the screen. It was build and tested on Mac OS.


# How It Works
The game consists of 4 vertical lanes so the bot checks only one column per lane and if it find a pixel with a predetermined color it clicks the mouse at it's position, and then starts to search for the new tile to hit using screen capture


# Running
Install the Required libraries<br>

```shell
pip install -r requirements.txt
```

Run the bot
```shell
sudo python3 bot.py
```