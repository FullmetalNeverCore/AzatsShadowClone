import discord 
from discord.ext import commands, tasks
from discord.utils import get
import serverbot 
import json
import time 

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print("Azat's Shadow Clone is online!")
    vision.start()

@tasks.loop(seconds=2)
async def vision():
    img = serverbot.Azats_Vision.locate_image_on_screen("./nm.png")
    rimg = serverbot.Azats_Vision.locate_image_on_screen("./raid.png")
    if img == True:
        with open('server.json') as file:
            data = json.load(file)
            token = data['Special_Channel']['chat']
            channel = client.get_channel(token)
            print('presend!')
            embed = discord.Embed(title="SERVER : -------", description="REASON : Был замечен легендарный покемон!", color=0x00ff00)
            embed.set_image(url="attachment://leg.png")
            embed.set_footer(text="A.Z.A.T OS V. 1.12.3 (c) Cyberdyne Systems")
            await channel.send(file=discord.File("./leg.png"), embed=embed)
            print('Target found,sleeping for next 45 seconds.')
        time.sleep(45)
    if rimg == True:
        with open('server.json') as file:
            data = json.load(file)
            token = data['Special_Channel']['chat']
            channel = client.get_channel(token)
            print('presend!')
            embed = discord.Embed(title="SERVER : --------", description="REASON : Был замечен рейд на легендарного покемона!", color=0x00ff00)
            embed.set_image(url="attachment://leg.png")
            embed.set_footer(text="A.Z.A.T OS V. 1.12.3 (c) Cyberdyne Systems")
            await channel.send(file=discord.File("./leg.png"), embed=embed)
            print('Target found,sleeping for next 45 seconds.')
        time.sleep(45)


with open('server.json') as file:
    data = json.load(file)
    token = data['token']
client.run(token)