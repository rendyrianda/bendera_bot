# bot.py
import os
import random
import discord

TOKEN = 'ODMxNzg1MTY1OTE0MjQzMDkz.YHaSTQ._jeei-czYhkUvgaaPkyHF9lFFZg'

client = discord.Client()

@client.event
async def on_ready():
        print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    isi = [
            'hmmm apa yaaa',
            'enak aja minta flag',
            'kayaknya ini : https://i.imgur.com/6AnLddq.png',
            'bentar ingat-ingat dulu....',
            'mungkin ini : QnVrYW4gZmxhZ255YSBIQUhBSEFIQUhBSEFIQQo=',
            '```help : help\nabout : tentang bot\nFlag : ????```',
            '```Version : 1.0.3\nAuthor : Rendy Rianda\nRepo Github : https://github.com/rendyrianda/bendera_bot```',
            ]
    if message.content == 'flag':
        response = isi[random.randint(0,4)]
        await message.channel.send(response)
    if message.content == 'help':
        response = isi[5]
        await message.channel.send(response)
    if message.content == 'about':
        response = isi[6]
        await message.channel.send(response)
client.run(TOKEN)
