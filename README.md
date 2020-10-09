# Discord-VC-analyser
This is a simple bot based on [discord.py](https://github.com/Rapptz/discord.py) that efficiently tracks individually who's connected to each voice chat in a Discord server and at what times.

## RUNNING

To use the bot, simply download it into a directory, create a `/data` folder in the same directory, [create a discord bot with no additional permissions and invite it to your desired server](https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro), copy its token into `main.py`, and run `main.py`. After login success, the `/data` folder should fill up with text files, one for each voice channel in the server, formatted like so:
```
UTC_TIME_FLOAT, user1#XXXX, user2#XXXX, ...
```
Note that the bot only identifies users which joined the voice channel after the bot started running, and that it automatically deletes "unneeded" samples, I.E samples which are the same as the ones directly before and after them (where no user joined or left).

## PARSING
Since the data files are simply text, they can be parsed in many ways. In case you don't want to write a parser from scratch, a small convenience module is included which can parse one or all of the data files to a usable format. The simplest way to use it is like so:
```python
from basic_parser import parse_all
user_id_dict, res_lis = parse_all()
```
Where `user_id_dict` is a `dict` containing user names and a respective "local ID" _i.e_ `{'user1#XXXX': 1, 'user2#XXXX': 2, ...}`, and `res_lis` is a list of tuples sorted by voice channels of `('<channel_name>', utc_timestamp_list, conected_user_tuple_list)`, with the UTC times represented as floats and the connected users being tuples of integers (corresponding to the used IDs returned in the first argument).
