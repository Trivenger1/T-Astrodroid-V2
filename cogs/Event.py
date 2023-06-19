import random
import Data.archives as archives
import discord
from discord.ext import commands


class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        green_ID = 145176026673053696
        triv_ID = 465755316479459328
        fnux_ID = 272621808442802176
        quantum_ID = 490430593126105098
        romi_ID = 271279386953646082

        if message.author == self.bot.user:
            return

        if message.content == 'bich' or message.content.lower() == 'bitch':
            response = 'bitch'
            await message.channel.send(response)

        if message.content.lower() == 'squawk' or 'SQUAWK' in message.content or 'squawk' in message.content:
            response = 'Fnux gay'
            await message.channel.send(response)

        if message.content == '69':
            response = ['Nice', 'Ha, that\'s the funny sex number']
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
            emoji = self.bot.get_emoji(647660832532070411)
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

        pass
        # if message.author.id == green_ID:
        #     if ' rate ' in message.content:
        #         await message.channel.send(f'{random.choice(range(1, 11))}/10')



def setup(bot: discord.Bot):
    bot.add_cog(Event(bot))