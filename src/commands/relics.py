import discord

from discord.ext import commands
from discord import app_commands

from src.config import no_bar, base_url_dict
from src.utils import get_relic, get_data


class Relics(commands.Cog):

    '''Relics Command'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='relics')
    @app_commands.describe(name='relic name')
    @app_commands.checks.bot_has_permissions(send_messages = True, 
                                             view_channel = True, 
                                             external_emojis = True, 
                                             embed_links = True, 
                                             send_messages_in_threads = True, 
                                             attach_files = True)
    # @app_commands.checks.cooldown(1, 30, key=lambda i: i.user.id)
    async def relics(self, interaction: discord.Interaction, name: str):

        '''
        Relics (aka Gadgets) are tools that aid the player in exploration or combat.
        '''

        if interaction.user.id != self.bot.application.owner.id:
            return await interaction.response.send_message(embed=discord.Embed(
                color=no_bar, description='Sorry, it\'s still in development'
            ))

        await interaction.response.defer()

        relic = await get_relic(name=name)

        em = discord.Embed(color=no_bar, 
                           title=f'{relic["name"]}')
        

        # thumb_url = await get_data(name=relic['imgSrc'], data='relics', src='image')
        # if thumb_url:
        #     em.set_thumbnail(url=thumb_url)

        await interaction.edit_original_response(embed=em)
    
async def setup(bot):
    await bot.add_cog(Relics(bot))
