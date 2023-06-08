import discord

from src.simulacra_buttons import trait_button_func, home_button_func, weapon_button_func, advanc_button_func, meta_button_func
from src.simulacra_buttons import abilities_button_func, discharge_button_func, matrice_button_func


class MainView(discord.ui.View):

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView())


    @discord.ui.button(custom_id='trait', label='Trait', style=discord.ButtonStyle.grey)
    async def trait_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''trait Button'''

        await interaction.response.defer()
        em = await trait_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=TraitView())

    @discord.ui.button(custom_id='matrice', label='Matrices', style=discord.ButtonStyle.grey)
    async def matrice_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''matrice Button'''

        await interaction.response.defer()
        em = await matrice_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=MatriceView())



class TraitView(discord.ui.View):

    @discord.ui.button(custom_id='home', label='Simulacra', style=discord.ButtonStyle.grey)
    async def home_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''home Button'''

        await interaction.response.defer()
        em = await home_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=MainView())

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView())

    @discord.ui.button(custom_id='matrice', label='Matrices', style=discord.ButtonStyle.grey)
    async def matrice_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''matrice Button'''

        await interaction.response.defer()
        em = await matrice_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=MatriceView())


class MatriceView(discord.ui.View):

    @discord.ui.button(custom_id='home', label='Simulacra', style=discord.ButtonStyle.grey)
    async def home_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''home Button'''

        await interaction.response.defer()
        em = await home_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=MainView())

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView())

    @discord.ui.button(custom_id='trait', label='Trait', style=discord.ButtonStyle.grey)
    async def trait_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''trait Button'''

        await interaction.response.defer()
        em = await trait_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=TraitView())



class WeaponView(discord.ui.View):

    @discord.ui.button(custom_id='home', label='Simulacra', style=discord.ButtonStyle.grey)
    async def home_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''home Button'''

        await interaction.response.defer()
        em = await home_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=MainView())

    @discord.ui.button(custom_id='advancements', label='Advancements', style=discord.ButtonStyle.grey)
    async def advanc_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''advancement button'''
        await interaction.response.defer()
        em = await advanc_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=AdvancView())

    @discord.ui.button(custom_id='meta', label='Meta', style=discord.ButtonStyle.grey)
    async def meta_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''meta / rec pairings button'''
        await interaction.response.defer()
        em = await meta_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=MetaView())

    @discord.ui.button(custom_id='skill', label='Skill\'s', style=discord.ButtonStyle.grey)
    async def abilities_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''skill button'''
        await interaction.response.defer()
        em = await abilities_button_func(interaction)
        await interaction.message.edit(embeds=[em], view=AbilitieView())



class AdvancView(discord.ui.View):

    @discord.ui.button(custom_id='home', label='Simulacra', style=discord.ButtonStyle.grey)
    async def home_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''home Button'''

        await interaction.response.defer()
        em = await home_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=MainView())

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView())



class MetaView(discord.ui.View):
    @discord.ui.button(custom_id='home', label='Simulacra', style=discord.ButtonStyle.grey)
    async def home_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''home Button'''

        await interaction.response.defer()
        em = await home_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=MainView())

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView())



class AbilitieView(discord.ui.View):

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView())
    
    @discord.ui.button(custom_id='discharge', label='Discharge', style=discord.ButtonStyle.grey)
    async def discharge_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''discharge Button'''
        await interaction.response.defer()
        em = await discharge_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=DischargeView())



class DischargeView(discord.ui.View):

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView())
    
    @discord.ui.button(custom_id='skill', label='Skill\'s', style=discord.ButtonStyle.grey)
    async def abilities_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''skill button'''
        await interaction.response.defer()
        em = await abilities_button_func(interaction)
        await interaction.message.edit(embeds=[em], view=AbilitieView())