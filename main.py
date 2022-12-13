#!/usr/bin/env python3
"""
@file ping-pong-dash/main.py
@version 0.0.1
@author donabe8898
@date 2022-12-22
@brief VC入室通知BOT
"""
import discord
import bisect
import os
from os.path import join, dirname
from dotenv import load_dotenv
import urllib.request
import json
import re
import random
import asyncio
from collections import OrderedDict
from discord.ext import tasks
from discord import Embed
from discord import app_commands
import time
import datetime
from datetime import datetime, timedelta, timezone
import calendar
import io
import abc
import itertools
from lxml import html
from setuptools import Command

# my modules
import envop
import embed

BOT_TOKEN = envop.dot_env_bot_token()   # slashcommand testDotEnv
GUILD_ID = envop.dot_env_guild_id() # 鯖ID
CHANNEL_ID = envop.dot_env_channel_id()

### begin intents
intents = discord.Intents.default()
intents.message_content=True
intents.members = True  # これTrueにしないと鯖メンバーを検索できない
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
### end intents

"""
@tree.command(name="add",description="Adding vc channel",guild=discord.Object(id=GUILD_ID))
async def hlw(interaction) -> None:
"""

@client.event
async def on_voice_state_update(member, before, after):
    global sendEmbed
    #  Assign message channel
    if before.channel != after.channel:
        botRoom = client.get_channel(CHANNEL_ID)
        announceChannelIds = [1049940299864080477]
        ## under debug
        if after.channel is not None and after.channel.id in announceChannelIds:
            if before.channel is None:
                # asyncio.run(embed.create_embed(member, after.channel))
                sendEmbed = await embed.EmbedSender.create_embed(member, after.channel)
                await botRoom.send(embed=sendEmbed)
            else:
                update_embed = embed.EmbedSender.edit_embed(member, after.channel, sendEmbed)
                await sendEmbed.edit(embed=update_embed)


# 起動
client.run(BOT_TOKEN)



