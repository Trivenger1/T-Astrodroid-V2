import discord
import Data.archives as archives
import random
import Data.IQEXT as IQ
from pysaucenao import SauceNao
from discord.ext import commands


class Comms(discord.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(help='Says whatever you wanna say')
    async def say(self,ctx, *, arg):
        if '@' in arg:
            await ctx.send('Nice try peckneck')
        else:
            await ctx.send(arg)


    @commands.command(help='My introduction')
    async def intro(self,ctx):
        response = f'Hello there,I am {self.bot.user.name}.I was made with the purpose to train Triv\'s coding skills as well' \
                'as provide unreasonable and questionable entertainment to anyone else.I still have future commands to be' \
                'written so do stay tuned'
        await ctx.send(response)


    @commands.command(name='help')
    async def help_com(self,ctx):
        await ctx.send(archives.help_res)


    @commands.command(name='music')
    async def music_help(self,ctx):
        await ctx.send(archives.music_lst)


    @commands.command(help='My full version specifications as of now')
    async def version(self,ctx):
        response = 'Trigonometry Operating Systems 2020,made on 22nd May 2020.Version 2.8.00.Collaboration of Shinonome ' \
                'Laboratories. Last updated [28/4/22]'
        await ctx.send(response)


    @commands.command(name='8ball', help='Now with 50 ish responses that makes me wonder why Triv does this')
    async def ball(self,ctx, line):
        chance = random.choice(range(10))
        # for ext in archives.peal_lst:
        #   if ext in ctx.content.lower():
        #       on_message(ctx)

        if chance > 6:
            choice_2 = random.choice(archives.eitball_img)
            final = discord.Embed()
            final.set_image(url=choice_2)
            await ctx.send(embed=final)
        else:

            await ctx.send(random.choice(archives.eitball))


    @commands.command(name='satria', help='Satria:YAMETTE')
    async def sat(self,ctx):
        from Data.archives import satria_img, sat_log
        chosen = random.choice(sat_log)
        if chosen == 'image':
            chosen_2 = random.choice(satria_img)
            img = discord.Embed()
            img.set_image(url=chosen_2)
            await ctx.channel.send(embed=img)

        else:
            await ctx.channel.send(chosen)


    @commands.command(name='sauce', help='tbot going dark')
    async def source(self,ctx):
        # if len(ctx.message.attachements) == 0:
        #   await ctx.channel.send('Outside links are not accepted at the moment until further updates due to lack of ability.')

        image = ctx.message.attachments[0].url
        sauce = SauceNao(api_key='ecac303898453582435bd677cd046f20651ef83c')
        results = await sauce.from_url(image)
        if len(results) == 0:
            await ctx.channel.send('Sauce could not be found')

        # elif 'results' in ctx.message.content:
        #   for sources in range(len(results)):

        else:
            best = results[0]
            pic = discord.Embed(title=f'{best.title}', url=best.url)
            pic.add_field(name='Author', value=best.author_name, inline=True)
            pic.add_field(name='Source', value=best.type, inline=True)
            pic.add_field(name='Similarity', value=best.similarity, inline=True)

            pic.add_field(name='Number of results found', value=len(results), inline=True)
            pic.set_image(url=best.thumbnail)

            await ctx.channel.send(embed=pic)


    @commands.command(name='purge')
    async def clean(self,ctx, limit: int):
        if ctx.author.id == 465755316479459328 or ctx.author.id == 676985337934774289:
            await ctx.channel.purge(limit=limit)
            await ctx.send('Cleared by {}'.format(ctx.author.mention), delete_after=20)
            await ctx.message.delete()
        else:
            await ctx.channel.send('Haha, permission denied.')


    @commands.Cog.listener()
    async def on_reaction_add(self,reaction, user):
        if str(reaction) == "📌" and (user.id == 676985337934774289 or user.id == 465755316479459328):
            await reaction.message.pin()
            await reaction.message.remove_reaction(reaction, user)
            await reaction.message.channel.send("{} Pinned a message!".format(user.mention))


    # @bot.command(name='mute', help=';3c')
    # async def muted(ctx, user: discord.Member, time: int):
    #     # if not user:
    #     #   await ctx.send('Noone to mute smh')
    #
    #     all_roles = await ctx.guild.fetch_roles()
    #     num_roles = len(all_roles)
    #     if time > 0 and (ctx.author.id == 465755316479459328 or ctx.author.id == 676985337934774289):
    #         role = discord.utils.get(ctx.guild.roles, name='Mute')
    #         await role.edit(position=num_roles-2)
    #         if not role:
    #             role = await ctx.guild.create_role(name="Mute",permissions=discord.Permissions(send_messages=False))
    #             await role.edit(position=num_roles-2)
    #
    #         await user.add_roles(role)
    #         await ctx.send(f"{user.mention} was muted for {time} seconds", delete_after=10)
    #         await asyncio.sleep(time)
    #         await user.remove_roles(role)
    #     else:
    #         await ctx.send('No time given or Permission denied')


    @commands.command()
    async def pekofy(self, ctx):
        messages = await ctx.channel.history(limit=2).flatten()
        if "@" in messages[1].content:
            await ctx.channel.send("no no peko peko ޏ₍ ὸ.ό₎ރ")
        else:
            await ctx.channel.send(messages[1].content + " peko")


    @commands.command(name='iq')
    async def Incorrect(self, ctx, *args):
        msg = "Wrong input"

        def checktype(argument):
            for ar in argument:
                if type(ar) != str:
                    return False
                elif "@" in ar:
                    return False
            return True

        def checkamount(len):
            if len > 6 or len < 1:
                return False
            return True

        arg_tup = (arg for arg in args)
        arg_tup = ','.join(arg_tup)
        ag = arg_tup.split(",")
        size = len(ag)

        if checktype(args) and checkamount(size):
            if size == 1:
                await ctx.channel.send(IQ.generate_prompt1(ag[0]))
            elif size == 2:
                await ctx.channel.send(IQ.generate_prompt2(ag[0], ag[1]))
            elif size == 3:
                await ctx.channel.send(IQ.generate_prompt3(ag[0], ag[1], ag[2]))
            elif size == 4:
                await ctx.channel.send(IQ.generate_prompt4(ag[0], ag[1], ag[2], ag[3]))
            elif size == 5:
                await ctx.channel.send(IQ.generate_prompt5(ag[0], ag[1], ag[2], ag[3], ag[4]))
            elif size == 6:
                await ctx.channel.send(IQ.generate_prompt6(ag[0], ag[1], ag[2], ag[3], ag[4], ag[5]))
        else:
            await ctx.channel.send(msg)


def setup(bot: discord.Bot):
    bot.add_cog(Comms(bot))

    # async def bill(ctx,form:str,name:str):
    # if form == 'def':

    #     link = f"https://belikebill.ga/billgen-API.php?default=1&name=" + urllib.parse.quote(name)

    #     # img = "tmp/" + user + ".jpg"
    #     # print(img)

    #     final = discord.Embed()
    #     final.set_image(url=link)
    #     await ctx.channel.send(embed=final)
