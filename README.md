# Discord-VC-analyser
This is a simple bot based on [discord.py](https://github.com/Rapptz/discord.py) that efficiently tracks individually who's connected to each voice chat in a Discord server and at what times.

To use the bot, simply download it into a directory, create a `/data` folder in the same directory, [create discord bot with no additional permissions and invite it to your desired server](https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro), copy its token into `main.py`, and run `main.py`. After login success, the `/data` folder should fill up with text files, one for each voice channel in the server, formatted like so:
```
UTC_TIME_FLOAT, user1#XXXX, user2#XXXX, ...
```
Note that the bot only identifies users which joined the voice channel after the bot started running, and that it automatically deletes "unneeded" samples, I.E samples which are the same as the ones directly before and after them (where no user joined or left).
