import discord
import os
import discord
import random
import Data.archives as archives
# import archives
# import music
# import Entertainment
from pysaucenao import SauceNao
# from awake import keep_alive
from discord.ext import commands
# import IncorrectQ.IQEXT as IQ
# import musictest
# import cogs.Comms as comms
from os import listdir
from dotenv import load_dotenv



load_dotenv()
bot = commands.Bot(command_prefix='=', help_command=None, intents=discord.Intents.all())
# bot.add_cog(music.Music(bot))
# bot.add_cog(Entertainment.Entertainment(bot))
# bot.add_cog(musictest.Music(bot))
# bot.add_cog(comms.comms(bot))
status = ['Updating to new Update Version', 'a']

# peal_mute_timer = 30
# main_mute_timer = 30

Server = {'TNO'}

for cog in listdir("cogs/"):
    if cog.endswith(".py"):
        cog = cog[:-3]
        print(f"Loading extension: {cog}")
        bot.load_extension(f"cogs.{cog}")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Stable 2.0 Update'))
    print(f'You have logged in as {bot.user}.Ready to comply')





login = os.getenv('TOKEN')

# keep_alive()
bot.run(login)
