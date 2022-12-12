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

json_open = open("fortune.json","r")    # opening file
fortune_list =  json.load(json_open)
BOT_TOKEN = envop.dot_env_bot_token()   # slashcommand testDotEnv
GUILD_ID = envop.dot_env_guild_id() # 鯖ID
Length = len(fortune_list)  # 名言の個数

### begin intents
intents = discord.Intents.default()
intents.message_content=True
intents.members = True  # これTrueにしないと鯖メンバーを検索できない
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
### end intents


