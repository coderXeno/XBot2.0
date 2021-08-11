import discord
import os

client=discord.Client()

topics={'1':'Supersymmetry','2':'Schwarzchild Radius','3':'M theory','4':'Duality','5':'Bosonic String Theory'}

list_display="1.  SUPERSYMMETRY\n 2.  SCHWARZCHILD RADIUS\n 3.  M THEORY\n 4.  DUALITY\n 5.  BOSONIC STRING THEORY"

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
  print("Hello, welcome to XenoBot😍!\nThis is a bot that will help you understand some of the basic fundamentals of string theory./nMore topics will be added soon!For now please enjoy the available topics😃!!\nTo get started, just type x!start")

@client.event
async def on_message(message):
  if message.author==client.user:
    return

  msg=message.content
  if msg.startswith('x!start'):
    await message.channel.send(f"Hello, lets start the awesome journey into the fundamentals of string theory. Here's a list of the topics to get you started \n {list_display}")

  if msg.startswith('1'):
    await message.channel.send("You selected Supersymmetry") 

  if msg.startswith('2'):
    await message.channel.send("You selected Schwarzchild radius") 

  if msg.startswith('3'):
    await message.channel.send("You selected M-Theory") 

  if msg.startswith('4'):
    await message.channel.send("You selected Duality") 

  if msg.startswith('5'):
    await message.channel.send("You selected Bosonic String Theory") 
  

client.run(os.getenv('token'))

