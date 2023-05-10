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
import cogs.Comms as comms
from os import listdir
from dotenv import load_dotenv



load_dotenv()
bot = commands.Bot(command_prefix='=', help_command=None, intents=discord.Intents.all())
# bot.add_cog(music.Music(bot))
# bot.add_cog(Entertainment.Entertainment(bot))
# bot.add_cog(musictest.Music(bot))
bot.add_cog(comms.comms(bot))
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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Stable 1.0 Update'))
    print(f'You have logged in as {bot.user}.Ready to comply')


# @bot.command(help='Says whatever you wanna say')
# async def say(ctx, *, arg):
#     if '@' in arg:
#         await ctx.send('Nice try peckneck')
#     else:
#         await ctx.send(arg)


# @bot.command(help='My introduction')
# async def intro(ctx):
#     response = f'Hello there,I am {bot.user}.I was made with the purpose to train Triv\'s coding skills as well' \
#                'as provide unreasonable and questionable entertainment to anyone else.I still have future commands to be' \
#                'written so do stay tuned'
#     await ctx.send(response)


# @bot.command(name='help')
# async def help_com(ctx):
#     await ctx.send(archives.help_res)


# @bot.command(name='music')
# async def music_help(ctx):
#     await ctx.send(archives.music_lst)


# @bot.command(help='My full version specifications as of now')
# async def version(ctx):
#     response = 'Trigonometry Operating Systems 2020,made on 22nd May 2020.Version 2.8.00.Collaboration of Shinonome ' \
#                'Laboratories. Last updated [28/4/22]'
#     await ctx.send(response)


# @bot.command(name='8ball', help='Now with 50 ish responses that makes me wonder why Triv does this')
# async def ball(ctx, line):
#     chance = random.choice(range(10))
#     # for ext in archives.peal_lst:
#     #   if ext in ctx.content.lower():
#     #       on_message(ctx)

#     if chance > 6:
#         choice_2 = random.choice(archives.eitball_img)
#         final = discord.Embed()
#         final.set_image(url=choice_2)
#         await ctx.send(embed=final)
#     else:

#         await ctx.send(random.choice(archives.eitball))


# @bot.command(name='satria', help='Satria:YAMETTE')
# async def sat(ctx):
#     from archives import satria_img, sat_log
#     chosen = random.choice(sat_log)
#     if chosen == 'image':
#         chosen_2 = random.choice(satria_img)
#         img = discord.Embed()
#         img.set_image(url=chosen_2)
#         await ctx.channel.send(embed=img)

#     else:
#         await ctx.channel.send(chosen)


# @bot.command(name='sauce', help='tbot going dark')
# async def source(ctx):
#     # if len(ctx.message.attachements) == 0:
#     #   await ctx.channel.send('Outside links are not accepted at the moment until further updates due to lack of ability.')

#     image = ctx.message.attachments[0].url
#     sauce = SauceNao(api_key='ecac303898453582435bd677cd046f20651ef83c')
#     results = await sauce.from_url(image)
#     if len(results) == 0:
#         await ctx.channel.send('Sauce could not be found')

#     # elif 'results' in ctx.message.content:
#     #   for sources in range(len(results)):

#     else:
#         best = results[0]
#         pic = discord.Embed(title=f'{best.title}', url=best.url)
#         pic.add_field(name='Author', value=best.author_name, inline=True)
#         pic.add_field(name='Source', value=best.type, inline=True)
#         pic.add_field(name='Similarity', value=best.similarity, inline=True)

#         pic.add_field(name='Number of results found', value=len(results), inline=True)
#         pic.set_image(url=best.thumbnail)

#         await ctx.channel.send(embed=pic)


# @bot.command(name='purge')
# async def clean(ctx, limit: int):
#     if ctx.author.id == 465755316479459328 or ctx.author.id == 676985337934774289:
#         await ctx.channel.purge(limit=limit)
#         await ctx.send('Cleared by {}'.format(ctx.author.mention), delete_after=20)
#         await ctx.message.delete()
#     else:
#         await ctx.channel.send('Haha, permission denied.')


# @bot.listen()
# async def on_reaction_add(reaction, user):
#     if str(reaction) == "📌" and (user.id == 676985337934774289 or user.id == 465755316479459328):
#         await reaction.message.pin()
#         await reaction.message.remove_reaction(reaction, user)
#         await reaction.message.channel.send("{} Pinned a message!".format(user.mention))


# # @bot.command(name='mute', help=';3c')
# # async def muted(ctx, user: discord.Member, time: int):
# #     # if not user:
# #     #   await ctx.send('Noone to mute smh')
# #
# #     all_roles = await ctx.guild.fetch_roles()
# #     num_roles = len(all_roles)
# #     if time > 0 and (ctx.author.id == 465755316479459328 or ctx.author.id == 676985337934774289):
# #         role = discord.utils.get(ctx.guild.roles, name='Mute')
# #         await role.edit(position=num_roles-2)
# #         if not role:
# #             role = await ctx.guild.create_role(name="Mute",permissions=discord.Permissions(send_messages=False))
# #             await role.edit(position=num_roles-2)
# #
# #         await user.add_roles(role)
# #         await ctx.send(f"{user.mention} was muted for {time} seconds", delete_after=10)
# #         await asyncio.sleep(time)
# #         await user.remove_roles(role)
# #     else:
# #         await ctx.send('No time given or Permission denied')


# @bot.command()
# async def pekofy(ctx):
#     messages = await ctx.channel.history(limit=2).flatten()
#     if "@" in messages[1].content:
#         await ctx.channel.send("no no peko peko ޏ₍ ὸ.ό₎ރ")
#     else:
#         await ctx.channel.send(messages[1].content + " peko")


# @bot.command(name='iq')
# async def Incorrect(ctx, *args):
#     msg = "Wrong input"

#     def checktype(argument):
#         for ar in argument:
#             if type(ar) != str:
#                 return False
#             elif "@" in ar:
#                 return False
#         return True

#     def checkamount(len):
#         if len > 6 or len < 1:
#             return False
#         return True

#     arg_tup = (arg for arg in args)
#     arg_tup = ','.join(arg_tup)
#     ag = arg_tup.split(",")
#     size = len(ag)

#     if checktype(args) and checkamount(size):
#         if size == 1:
#             await ctx.channel.send(IQ.generate_prompt1(ag[0]))
#         elif size == 2:
#             await ctx.channel.send(IQ.generate_prompt2(ag[0], ag[1]))
#         elif size == 3:
#             await ctx.channel.send(IQ.generate_prompt3(ag[0], ag[1], ag[2]))
#         elif size == 4:
#             await ctx.channel.send(IQ.generate_prompt4(ag[0], ag[1], ag[2], ag[3]))
#         elif size == 5:
#             await ctx.channel.send(IQ.generate_prompt5(ag[0], ag[1], ag[2], ag[3], ag[4]))
#         elif size == 6:
#             await ctx.channel.send(IQ.generate_prompt6(ag[0], ag[1], ag[2], ag[3], ag[4], ag[5]))
#     else:
#         await ctx.channel.send(msg)



#
# async def bill(ctx,form:str,name:str):
#   if form == 'def':

#     link = f"https://belikebill.ga/billgen-API.php?default=1&name=" + urllib.parse.quote(name)

#     # img = "tmp/" + user + ".jpg"
#     # print(img)

#     final = discord.Embed()
#     final.set_image(url=link)
#     await ctx.channel.send(embed=final)


# _________________________________________________________________________
# KARAOKE
# @bot.command(name='karaoke')


@bot.event
async def on_message(message):
    green_ID = 145176026673053696
    triv_ID = 465755316479459328
    fnux_ID = 272621808442802176
    quantum_ID = 490430593126105098
    romi_ID = 271279386953646082
    if message.author == bot.user:
        return

    if message.content == 'bich' or message.content.lower() == 'bitch':
        response = 'bitch'
        await message.channel.send(response)

    if message.content.lower() == 'squawk' or 'SQUAWK' in message.content or 'squawk' in message.content:
        response = 'Fnux gay'
        await message.channel.send(response)

    if message.content == '69':
        response = ['Nice', 'Ha,that\'s the funny sex number']
        await message.channel.send(random.choice(response))

    if message.content.lower() == 'epic' or 'epic' in message.content:
        dab = ['<:HollowDab:646713294005993473>', '<:Epicdab:646956038326714368>']
        response = random.choice(dab)
        chance = range(1, 5)
        if random.choice(chance) >= 4:
            await message.channel.send(response)

    if message.content.lower() == 'bruh':
        chance = range(1, 5)
        response = 'THAT is a bruh moment'
        if random.choice(chance) == 1:
            await message.channel.send(response)

    if message.content.lower() == 'good tbot':
        responses = ['No you', 'You\'re breathtaking', 'OwO', ':3', '<:Shorklove:646713335265361930>', 'hehehe',
                     'thank you peko~']
        response = random.choice(responses)
        await message.channel.send(response)

    if message.content == 'bad tbot':
        e = discord.Embed(title='**No u**')
        e.set_image(
            url='https://cdn.discordapp.com/attachments/662163918914977792/712854171774222417/confusionkid1.3.jpg')
        responses = ['Pffttt *cries*', 'QwQ', '>.>', 'no u', 'haha no', ';w;',
                     'better than u at least ;3c', archives.seals]
        final = random.choice(responses)
        if final == 'no u':
            await message.channel.send(embed=e)
        else:
            await message.channel.send(random.choice(responses))

    if message.content == 'bad bot':
        emoji = bot.get_emoji(647660832532070411)
        await message.add_reaction(emoji)

    if message.content.lower() == 'what the fuck':
        chance = range(1, 4)
        response = 'Ikr'
        if random.choice(chance) == 1:
            await message.channel.send(response)

    if message.content.lower() == 'smh':
        chance = range(1, 4)
        response = ['smh', 'smsmh']
        if random.choice(chance) == 1:
            await message.channel.send(random.choice(response))

    if message.content.lower() == 'no u':
        e = discord.Embed(title='**No u**')
        e.set_image(
            url='https://cdn.discordapp.com/attachments/662163918914977792/712854171774222417/confusionkid1.3.jpg')
        await message.channel.send(embed=e)

    # if message.content.lower() == 'pain':
    #     await message.channel.send("peko")

    # if random.choice(range(11)) == 11:
    #     if 'amogus' in message.content.lower() or 'amongus' in message.content.lower() or 'sus' in message.content.lower():
    #         choice = random.choice(archives.among)
    #         response = discord.Embed()
    #         response.set_image(url=choice)
    #         await message.channel.send(embed=response)
    if message.content.lower() == 'owo':
        response = '<a:Smugkid:674118792548188170>'
        await message.channel.send(response)
    """
    For ID COMMAND__________________________________________________
    """
    # if message.author.id == quantum_ID:
    #     if 'Dad' in message.content:
    #         response = 'Shut the fuck up quantum bot shut the fuck up nobody asked you bitch ass i hate you you bad ' \
    #                    'fucking bot st upid ass'
    #         await message.channel.send(response)

    if message.author.id == triv_ID:
        if message.content == 'Ban':
            response = f'Pls do not move or run,u are about to be shot down <:saffronshiny:483510554858618891>'
            await message.channel.send(response)

        if message.content.lower() == 'let\'s get some butter' or message.content.lower() == 'it\'s butter time':
            # response = bot.get_emoji(993436866797916190)
            await message.channel.send('<:slight_smile:993436866797916190>')
        # if 'cri' in message.content:
        #     response = 'Issa ok,u have me <:Shorklove:646713335265361930>'
        #     await message.channel.send(response)

    # if message.author.id == fnux_ID:
    #     if 'shoot me' in message.content:
    #         emote = '<:POP:695994877846224968>'
    #         response = 'I\'ve been looking forward to this \n ***Loads Gun***'
    #         await message.channel.send(emote)
    #         await message.channel.send(response)

    await bot.process_commands(message)

    # if message.author.id == green_ID:
    #     if ' rate ' in message.content:
    #         await message.channel.send(f'{random.choice(range(1, 11))}/10')


login = os.getenv('TOKEN')

# keep_alive()
bot.run(login)
