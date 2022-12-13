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

class EmbedSender:
    async def create_embed (member, channel):
        # new create
        _embed = discord.Embed(title="PONG!", description="test 0.0.1",color=0x228b22)
        _embed.add_field(name = member.name + " join the " + channel.name, value = "Enjoy!")
        return _embed

    async def edit_embed(member, channel, update):
    # edit
        members = [i.name for i in message.author.voice.channel.members]
        for i in member:
            update.add_field(name = member.name + " join the " + channel.name, value = "Enjoy!")
        return update
