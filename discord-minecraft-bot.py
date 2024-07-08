import os
import sys
import logging
import discord
from discord.ext import commands
import subprocess
from mcrcon import MCRcon
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Minecraft server settings from .env
MC_SERVER_PATH = os.getenv('MC_SERVER_PATH')
MC_SERVER_DIRECTORY = os.getenv('MC_SERVER_DIRECTORY')
RCON_PASSWORD = os.getenv('RCON_PASSWORD')
RCON_PORT = int(os.getenv('RCON_PORT', 25575))
JAVA_MEMORY = os.getenv('JAVA_MEMORY', '4G')

# Check if essential environment variables are set
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
if not DISCORD_BOT_TOKEN:
    logging.error("DISCORD_BOT_TOKEN is not set in the .env file.")
    sys.exit(1)

def is_server_running():
    try:
        with MCRcon("localhost", RCON_PASSWORD, port=RCON_PORT) as mcr:
            mcr.command("list")  # Simple command to check if server responds
        return True
    except:
        return False

@bot.event
async def on_ready():
    logging.info(f'{bot.user} has connected to Discord!')

@bot.command(name='s')  # Changed from 'start' to 's'
async def start_minecraft(ctx):
    if is_server_running():
        await ctx.send('Minecraft server is already running!')
        return

    await ctx.send('Starting Fabric Minecraft server...')
    try:
        subprocess.Popen(['java', f'-Xmx{JAVA_MEMORY}', '-jar', MC_SERVER_PATH], 
                         cwd=MC_SERVER_DIRECTORY)
        await ctx.send('Fabric Minecraft server started successfully!')
    except Exception as e:
        logging.error(f"Error starting Minecraft server: {str(e)}")
        await ctx.send(f'Error starting Fabric Minecraft server: {str(e)}')

@bot.command(name='c')  # Changed from 'mc_command' to 'c'
async def mc_command(ctx, *, command):
    logging.info(f"Executing command: {command}")
    try:
        with MCRcon("localhost", RCON_PASSWORD, port=RCON_PORT) as mcr:
            logging.info("RCON connection established")
            resp = mcr.command(command)
            logging.info(f"Command response: {resp}")
            await ctx.send(f'Command executed. Response: {resp}')
    except ConnectionRefusedError:
        logging.error("RCON connection refused. Is the Minecraft server running and RCON enabled?")
        await ctx.send("Error: Could not connect to Minecraft server. Is it running and is RCON enabled?")
    except Exception as e:
        logging.error(f"Error executing command: {str(e)}")
        await ctx.send(f'Error executing command: {str(e)}')

@bot.command(name='sta')  # Changed from 'mc_status' to 'sta'
async def mc_status(ctx):
    if is_server_running():
        await ctx.send('Minecraft server is running.')
    else:
        await ctx.send('Minecraft server is not running.')

# Run the bot
try:
    bot.run(DISCORD_BOT_TOKEN)
except discord.errors.LoginFailure as e:
    logging.error(f"Failed to log in: {e}")
except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")
