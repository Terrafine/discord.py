import discord
from discord.ext import commands
import re

# Intents setup
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Necessary for accessing message content

# Create a bot instance with command prefix "!"
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command: Extract lines containing the specified keyword
@bot.command(read)
async def extract(ctx, mass: str):
    # Ensure a file is attached to the message
    if not ctx.message.attachments:
        await ctx.send("Please attach a .blueprint file.")
        return
    
    # Process the first attached file
    attachment = ctx.message.attachments[0]
    if not attachment.filename.endswith(".blueprint"):
        await ctx.send("Only .blueprint files are supported.")
        return
    
    # Download and read the content of the file
    file_content = await attachment.read()
    text = file_content.decode("utf-8")
    
    # Extract lines containing the keyword (case-insensitive)
    pattern = re.compile(rf'.*{re.escape(mass)}.*', re.IGNORECASE)
    matched_lines = pattern.findall(text)
    
    # Respond with the extracted lines or a message if none are found
    if matched_lines:
        response = "\n".join(matched_lines[:10])  # Limit response to 10 lines to avoid flooding
        await ctx.send(f"**Lines containing '{mass}':**\n{response}")
    else:
        await ctx.send(f"No lines found containing the keyword '{mass}'.")

# Run the bot (replace "YOUR_BOT_TOKEN" with your actual token)
bot.run("MTMxNDY5ODMyNjg3NjIyOTcyMg.G23TZF.NIhzw5Rh_q_3c3m4t18yYy0UrarGw_qx2x13eE")
