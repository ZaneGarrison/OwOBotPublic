#!/usr/bin/env python3

import re
from datetime import datetime
import discord
import random

TOKEN = "Input your token here"

emotes = [';;w;;', '^w^', '>w<', '(・\\`ω´・)', '(´・ω・\\`)', 'UwU', '(o´ω\\`o)', '( ͡o ω ͡o )', '（ ゜ω 。）', 'ÒwÓ', ':3',
          ':3c', '( o͡ \uA4B3 o͡ )', '( °\uA4B3° )', 'Ō>Ō'];

client = discord.Client()
file = open("discordLog.txt", "a+")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!owo'):
        # receiving message to owo and cut down
        owoString = message.content
        owoStringarray = re.split("\s", owoString, 1)
        owoString = owoStringarray[1]

        # get date and time for text file
        now = datetime.now()

        # open file and write the date and the pre owo string
        file = open("discordLog.txt", "a+")
        file.write(now.strftime("%m-%d-%Y %H:%M:%S") + "\nPre owo String \n" + owoString + "\n")

        # replace r and l with w
        owoString = re.sub("[rl]", "w", owoString)
        owoString = re.sub("[RL]", "W", owoString)

        # replace n+vowel with ny+vowel
        owoString = re.sub("na", "nya", owoString)
        owoString = re.sub("ne", "nye", owoString)
        owoString = re.sub("ni", "nyi", owoString)
        owoString = re.sub("no", "nyo", owoString)
        owoString = re.sub("Na", "Nya", owoString)
        owoString = re.sub("Ne", "Nye", owoString)
        owoString = re.sub("Ni", "Nyi", owoString)
        owoString = re.sub("No", "Nyo", owoString)

        # replace ? with ?OwO
        owoString = re.sub("\\?", "? OwO", owoString)

        # replace . with random emote while there is still a . in owoString
        while "." in owoString:
            owoString = re.sub("\\.", random.choice(emotes), owoString, 1)

        # same as above but !
        while "!" in owoString:
            owoString = re.sub("!", random.choice(emotes), owoString, 1)

        await message.channel.send(owoString)
        file.write("Post owo String \n" + owoString + "\n\n")
        file.close()

    if message.content.startswith('!ttsowo'):
        # receiving message to owo and cut down
        owoString = message.content
        owoStringarray = re.split("\s", owoString, 1)
        owoString = owoStringarray[1]

        # get date and time for text file
        now = datetime.now()

        # open file and write the date and the pre owo string
        file = open("discordLog.txt", "a+")
        file.write(now.strftime("%m-%d-%Y %H:%M:%S") + "\nPre owo String \n" + owoString + "\n")

        # replace r and l with w
        owoString = re.sub("[rl]", "w", owoString)
        owoString = re.sub("[RL]", "W", owoString)

        # replace n+vowel with ny+vowel
        owoString = re.sub("na", "nya", owoString)
        owoString = re.sub("ne", "nye", owoString)
        owoString = re.sub("ni", "nyi", owoString)
        owoString = re.sub("no", "nyo", owoString)
        owoString = re.sub("Na", "Nya", owoString)
        owoString = re.sub("Ne", "Nye", owoString)
        owoString = re.sub("Ni", "Nyi", owoString)
        owoString = re.sub("No", "Nyo", owoString)

        # replace ? with ?OwO
        owoString = re.sub("\\?", "? OwO", owoString)

        # replace . with random emote while there is still a . in owoString
        while "." in owoString:
            owoString = re.sub("\\.", random.choice(emotes), owoString, 1)

        # same as above but !
        while "!" in owoString:
            owoString = re.sub("!", random.choice(emotes), owoString, 1)

        await message.channel.send(owoString, tts=True)
        file.write("Post owo String \n" + owoString + "\n\n")
        file.close()

    if message.content.startswith('!helpowo'):
        message.channel.send("Use !owo to send a chat message in owo speak\n"
                             "Use !ttsowo for the same message but text to speech")


client.run("TOKEN")
