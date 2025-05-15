import discord
import requests
from discord.ext import commands
from discord import app_commands

# Your bot token and cookie
TOKEN = 'discordbottokenhere'
COOKIE = 'fullrobloxcookiehere get this from cookie editor on the chrome webstore and press export on roblox.com/home as Header String'
USER_AGENT = 'Roblox/WinInet'

# Define the bot
bot = commands.Bot(command_prefix='/', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    # Sync commands once the bot is ready
    await bot.tree.sync()

@bot.tree.command(name="download-audio", description="Download a Roblox audio by ID and placeID")
async def download_audio(interaction: discord.Interaction, placeid: str, audioid: str):
    # Debugging: Log incoming slash command parameters
    print(f"[DEBUG] Received slash command with placeID: {placeid}, audioID: {audioid}")

    headers = {
        'User-Agent': USER_AGENT,
        'cookie': COOKIE,
        'Roblox-Place-Id': placeid
    }
    url = f'https://assetdelivery.roblox.com/v1/asset?id={audioid}'
    
    try:
        # Debugging: Log the request URL and headers
        print(f"[DEBUG] Request URL: {url}")


        # Make the request to download the asset
        response = requests.get(url, headers=headers)
        
        # Debugging: Log the response status and content
        print(f"[DEBUG] Response status code: {response.status_code}")
   
        
        if response.status_code == 200:
            # Save the audio file as an OGG file
            file_name = f'Roblox_Audio_{audioid}.ogg'
            with open(file_name, 'wb') as f:
                f.write(response.content)
            await interaction.response.send_message(f'Audio downloaded successfully as {file_name}')
        else:
            await interaction.response.send_message(f'Failed to download audio. Status code: {response.status_code}')
    except Exception as e:
        # Debugging: Log the exception
        print(f"[DEBUG] Exception occurred: {str(e)}")
        await interaction.response.send_message(f'Error: {str(e)}')

# Run the bot
bot.run(TOKEN)
