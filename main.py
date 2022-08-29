# GPT-3PO Discord Bot
# By Ryan Manzie

import discord
from discord.ext import commands
import openai
import yaml

#Loads API Key amd Discord Token from config.yml file
with open("config.yml", 'r') as conffile:
    conf = yaml.load(conffile, Loader = yaml.FullLoader)

openai.api_key = conf["OpenAI-Token"]  # Your OpenAI API Key
Discord_Token = conf["Discord-Token"]  # The Discord Bot's Token
bot_ver = "1.0"
gpt_bot = commands.Bot(command_prefix = "%", activity=discord.Game(name="with words"))

@gpt_bot.event
async def on_ready():
    print("--- GPT-3PO  Loaded! ---")
    print(" -- Running Version {0} --".format(bot_ver))

# Response to the %talk command
@gpt_bot.command() 
async def talk(ctx, *, prompt):
    print("Processing")   
    reply = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=1,
        max_tokens=545    
    )
    reply = reply.choices[0].text
    print(reply)
    await ctx.send(reply)

#Translate a prompt into french with the %french command
@gpt_bot.command()
async def french(ctx, *, prompt):
    print("Processing")
    reply = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Translate this into French: " + prompt,
        temperature=0.4,
        max_tokens=200    
    )
    reply = reply.choices[0].text
    await ctx.send(reply)
    print(reply)

gpt_bot.run(Discord_Token)