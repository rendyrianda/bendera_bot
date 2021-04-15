# bot.py
import os
import random
import discord

TOKEN = ''

client = discord.Client()

@client.event
async def on_ready():
        print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    isi = [
            '```help : help\nabout : tentang bot\nflag : ????```',
            '```Version : 1.0.3\nAuthor : Rendy Rianda\nRepo Github : https://github.com/rendyrianda/bendera_bot```',
            'meow','meowww','meowwww','meow meow',
            ]
    if message.content == 'help':
        response = isi[0]
        await message.channel.send(response)
    if message.content == 'about':
        response = isi[1]
        await message.channel.send(response)
    else : #probably bad idea to put this but it's work fine
        response = isi[random.randint(2,5)]
        await message.channel.send(response)
client.run(TOKEN)
