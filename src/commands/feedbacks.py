import discord

from discord.ext import commands
from discord import app_commands
from time import time
from asyncio import TimeoutError

from src.config import no_bar, bot_guild, feedback_category

timeout = 500


class Feedback(commands.Cog):

    '''Feedback Command'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='feedback')
    @app_commands.checks.cooldown(1, 10, key=lambda i: i.user.id)
    async def feedbacks(self, interaction: discord.Interaction):
        '''
        Suggestions, bug reports, words of encouragement, feel free to tell me what you need.
        '''
        await interaction.response.defer(ephemeral=True)

        if interaction.user != self.bot.application.owner:
            raise NotImplementedError()
        
        em = discord.Embed(color=no_bar)

        dm_channel = await interaction.user.create_dm()

        em.description=f'Check your dm {dm_channel.jump_url}'
        await interaction.edit_original_response(embed=em)

        em.title = 'Feedback'
        em.description = (f'A feedback can be suggestions, bug reports, words of encouragement, whatever you like, feel free to tell me what you need.\n'
                          f'Send a message with all you want, it can contains everything you can send in one message\n\n'
                          f'This interaction has a `waiting cooldown` to be finished: <t:{int(time()+timeout)}:R>')
        
        em.set_thumbnail(url=self.bot.user.avatar.url)
        
        await dm_channel.send(embed=em)

        def check(message: discord.Message):
            return message.channel == dm_channel

        try:
            feedback = await self.bot.wait_for('message', timeout=timeout, check=check)
        except TimeoutError:
            return await dm_channel.send('timeout expired, feedback canceled')

        em_res = discord.Embed(color=no_bar, 
                               description=feedback.content)
        
        em_res.set_author(name=f'{feedback.author} - {feedback.author.id}', 
                          icon_url=feedback.author.display_avatar.url, 
                          url=feedback.author.dm_channel.jump_url)
        
        await dm_channel.send(embed=em_res, 
                              content=(f'This is an example of your feedback and how many files it has, type `confirm` and it will be sent\n'
                                       f'{len(feedback.attachments)} files'))
        
        def check(message: discord.Message):
            return message.channel == dm_channel and message.content.lower() == 'confirm'

        try:
            response = await self.bot.wait_for('message', timeout=timeout, check=check)
        except TimeoutError:
            return await dm_channel.send('timeout expired, submission canceled')
        

        bot_guild = self.bot.get_guild(bot_guild)
        feedback_category = bot_guild.get_channel(feedback_category)
        feedback_channel = await feedback_category.create_text_channel(name=response.author, reason='feedback channel')

        files_url = '\n'.join([file.url for file in feedback.attachments])

        await feedback_channel.send(content=files_url, embed=em_res)
        await response.add_reaction('✅')

        
    
async def setup(bot):
    await bot.add_cog(Feedback(bot))
