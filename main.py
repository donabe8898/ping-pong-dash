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

json_open = open("fortune.json","r")    # opening file
fortune_list =  json.load(json_open)
BOT_TOKEN = envop.dot_env_bot_token()   # slashcommand testDotEnv
GUILD_ID = envop.dot_env_guild_id() # 鯖ID
CHANNEL_ID = envop.dot_env_channel_id()
Length = len(fortune_list)  # 名言の個数

### begin intents
intents = discord.Intents.default()
intents.message_content=True
intents.members = True  # これTrueにしないと鯖メンバーを検索できない
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
### end intents

@tree.command(name="add",description="Adding vc channel",guild=discord.Object(id=GUILD_ID))
async def hlw(interaction) -> None:

@client.event
async def on_voice_state_update(member, before, after):
    # Assign message channel
    if before.channel != after.channel:
        botRoom = client.get_channel(CHANNEL_ID)
        announceChannelIds = [1049940299864080477]
    if after.channel is not None and after.channel.id in announceChannelIds:
        if before.channel is None:
            asyncio.run(embed.create_embed(member))
        else
            await embed.edit_embed(embed.edit_embed(member))


# 開始処理
@client.event
async def on_ready() -> None:
    await tree.sync(guild=discord.Object(id=GUILD_ID))

# 起動
client.run(BOT_TOKEN)



