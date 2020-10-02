import time
import asyncio

import discord
from discord import ChannelType


SAMPLING_TIME = 60 #time between samples, in seconds


client = discord.Client() # needs no permissions, just to be in the server

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


def log_things():
    st = str(time.time())
    for channel in client.get_all_channels():
        if not (channel.type == ChannelType.voice): continue

        name, members = channel.name, channel.members

        fname = "data/" + name + ".txt"

        new_text = st + ", " + ", ".join(str(m) for m in members)

        try:
            with open(fname, 'r') as F: text = F.read().split("\n")
        except FileNotFoundError:
            text = []

        if len(text) >= 2 and\
           text[-2].split(", ", 1)[1] ==\
           text[-1].split(", ", 1)[1] ==\
           new_text.split(", ", 1)[1]:
            text[-1] = new_text
        else:
            text.append(new_text)
        
        with open(fname, 'w') as F:
            F.write("\n".join(text)) # inneficient


async def background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        log_things()
        await asyncio.sleep(SAMPLING_TIME)


client.loop.create_task(background_task())

client.run('<your token here>')
