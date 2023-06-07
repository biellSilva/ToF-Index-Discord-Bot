import discord
import aiohttp
import json

from typing import Literal

from src.config import emojis_1, names, base_url_dict



def check_name(name: str):
    for _ in names:
        if name.split(' ')[0].lower() in _.lower():
            return str(_) 
    return False


async def get_data(name, data: Literal['simulacra', 'weapons', 'matrices'], src: Literal['json', 'image']):

    '''
    for `simulacra` and `weapons` if `src == 'image'`, `name` need to be a tuple with Global Name and CN Name 

    for `matrices` if `src == 'image'`, `name` need to be `matrice['imgScr']`
    '''

    async with aiohttp.ClientSession() as cs:
        if src == 'json':
            name = check_name(name).replace(' ', '-').lower()
            if name:
                async with cs.get(f'{base_url_dict["data_json"]}/{data}/{name}.json') as res:
                    if res.status == 200:
                        return json.loads(s=await res.read())
                
        if src == 'image':
            if data == 'simulacra':
                for image_name in name:
                    if image_name.lower() == 'gnonno':
                        image_name = 'gunonno'

                    async with cs.get(f'{base_url_dict[f"{data}_{src}"]}/{image_name}.webp') as res:
                        if res.status == 200:
                            return res.url
                        
                    async with cs.get(f'{base_url_dict[f"{data}_{src}"]}/{image_name.lower()}.webp') as res:
                        if res.status == 200:
                            return res.url
            else:
                async with cs.get(f'{base_url_dict[f"{data}_{src}"]}/{name}.webp') as res:
                    if res.status == 200:
                        return res.url
                
    return False


async def home_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]

    simulacra = await get_data(name=em.title, data='simulacra', src='json')
    skin_url = f"[Skin Preview]({simulacra['skinsPreviewUrl']})" if 'skinsPreviewUrl' in simulacra else ''
    
    em.description=(f"CN Name: {simulacra['cnName'].capitalize()}\n"
                    f"Gender: {simulacra['gender']}\n"
                    f"Height: {simulacra['height']}\n"
                    f"Birthday: {simulacra['birthday']}\n"
                    f"Birthplace: {simulacra['birthplace']}\n"
                    f"Horoscope: {simulacra['horoscope']}\n\n"

                    f"{skin_url}" )
    
    thumb_url = await get_data(name=(simulacra['name'], simulacra['cnName']), data='simulacra', src='image')
    if thumb_url:
        em.set_thumbnail(url=thumb_url)

    em.clear_fields()

    for region, voiceActor in simulacra['voiceActors'].items():
        if voiceActor == '':
            continue
        em.add_field(name=region.upper(), value=voiceActor, inline=True)

    return em    
    

async def trait_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]

    simulacra = await get_data(name=em.title, data='simulacra', src='json')

    em.description = ''
    em.clear_fields()
    for trait in simulacra['traits']:
        em.add_field(name=f'Affinity {trait["affinity"]}', value=trait['description'], inline=False)

    return em


async def matrice_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]

    matrice = await get_data(name=em.title, data='matrices', src='json')

    em.clear_fields()

    for set in matrice['sets']:
        em.add_field(name=f'{set["pieces"]}x', value=set["description"], inline=False)

    thumb_url = await get_data(name=matrice['imgSrc'], data='matrices', src='image')
    if thumb_url:
        em.set_thumbnail(url=thumb_url)
    
    return em


async def weapon_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]

    weapon = await get_data(name=em.title, data='weapons', src='json')

    analysisVideo = f"[Analysis Video]({weapon['analysisVideoSrc']})" if 'analysisVideoSrc' in weapon else ''
    abilitiesVideo = f"[Abilities Video]({weapon['abilitiesVideoSrc']})" if 'abilitiesVideoSrc' in weapon else ''

    thumb_url = await get_data(name=weapon['imgSrc'], data='weapons', src='image')
    if thumb_url:
        em.set_thumbnail(url=thumb_url)

    em.clear_fields()
    em.description = (
                      f"**{weapon['name']}** {emojis_1[weapon['element']]} {emojis_1[weapon['type']]}\n"
                      f"Shatter: *{weapon['shatter']['value']} **{weapon['shatter']['tier']}***\n"
                      f"Charge: *{weapon['charge']['value']} **{weapon['charge']['tier']}***\n"
                      f"Base stats: *{' - '.join(weapon['baseStats']).title()}*\n"
                      )
    
    for i in [analysisVideo, abilitiesVideo]:
        if 'https' not in i:
            continue
        em.description += f'\n{i}'
    
    if 'weaponEffects' in weapon:
        for effect in weapon['weaponEffects']:
            em.add_field(name=effect['title'], value=effect['description'], inline=False)

    return em


async def advanc_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]

    weapon = await get_data(name=em.title, data='weapons', src='json')

    em.clear_fields()

    for ind, advanc in enumerate(weapon['advancements']):
        em.add_field(name=f'{ind+1} ★', value=advanc, inline=False)
    
    return em



async def meta_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]

    weapon = await get_data(name=em.title, data='weapons', src='json')

    em.clear_fields()

    desc = ''
    for name in weapon['recommendedPairings']:
        name : str
        url_name = name.replace(' ','-').lower()
        desc += f'\n**[{name.capitalize()}]({base_url_dict["simulacra_home"]}{url_name})**'
    
    if not desc.isspace():
        em.add_field(name='Recommended Pairings', value=desc, inline=False)

    desc = ''
    for matrix in weapon['recommendedMatrices']:
        matrix: dict
        url_name = matrix['name'].replace(' ', '-').lower()
        desc += f'\n{matrix["pieces"]}x **[{matrix["name"]}]({base_url_dict["matrice_home"]}{url_name})**'

    if not desc.isspace():
        em.add_field(name='Recommended Matrices', value=desc, inline=False)

    return em


async def abilities_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]

    weapon = await get_data(name=em.title, data='weapons', src='json')

    em.clear_fields()

    em.description = ''

    for abilitie in weapon['abilities']:
        if 'skill' in abilitie['type']:
            em.description += (f"\n\n**{abilitie['name'].title()}** *[ {abilitie['type'].capitalize()} ]*\n"
                               f"{abilitie['description']}")
            
    return em


async def discharge_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]

    weapon = await get_data(name=em.title, data='weapons', src='json')

    em.clear_fields()

    em.description = ''

    for abilitie in weapon['abilities']:
        if 'discharge' in abilitie['type']:
            em.description += (f"\n\n**{abilitie['name'].title()}** *[ {abilitie['type'].capitalize()} ]*\n"
                               f"{abilitie['description']}")
            
    return em