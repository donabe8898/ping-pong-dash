"""
@file fortune/dotenv.py
@version 0.1.0-alpha
@author donabe8898
@date 2022-11-6
@brief dotenv読み込み用モジュール
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

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)

def dot_env_bot_token() -> str:
    return os.environ.get("BOT_TOKEN")

def dot_env_guild_id() -> str:
    guild_id_str = os.environ.get("GUILD_ID")
    guild_id = int(guild_id_str)
    return guild_id
