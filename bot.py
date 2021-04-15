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
            'i hear something about this : `https://i.imgur.com/HEZ0ziM.png`',
            'not sure but i saw this \nXKZ{jCs4V_1v1_nt4oVg4}',
            'yesterday i saw this on street : https://i.imgur.com/6AnLddq.png',
            '`probably this one, https://bit.ly/IqT6zt`',
            'there is strange voice telling me bout this sequence of character \nQnVrYW4gZmxhZ255YSBIQUhBSEFIQUhBSEFIQQo=',
            '```help : help\nabout : tentang bot\nflag : ????```',
            '```Version : 1.0.3\nAuthor : Rendy Rianda\nRepo Github : https://github.com/rendyrianda/bendera_bot```',
            'meow','meowww','meowwww','meow meow',
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
    else : #probably bad idea to put this but it's work fine
        response = isi[random.randint(7,10)]
        await message.channel.send(response)
client.run(TOKEN)
