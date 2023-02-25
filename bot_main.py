import discord
import random
import time
from discord.ext import commands
from hhsh_web import get_announcement
from fishing import fishing
from fishing import init
from codeforcce_api import get_user_data
from codeforcce_api import get_user_rank
from database import registered

token = ""
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="",intents=intents)

init() # 初始化釣魚

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.slash_command(name="test")
async def first_slash(ctx):
    await ctx.respond("我在測試")

@bot.slash_command(name="register",description="將你的 Discord 帳號註冊在這一隻機器人上")
async def register(ctx):
    status = registered(ctx.author.id)
    print(ctx.author.id)
    if( status == -1 ): await ctx.respond("你已經註冊過了！")
    else: await ctx.respond("註冊成功！")

@bot.slash_command(name="fishing",description='釣一隻魚')
async def fish(ctx):
    ans = fishing()
    await ctx.respond('你釣起了一隻 'f'{round(random.uniform(0,100000))}'' cm 的'f'{ans}')

@bot.slash_command(name="announcement",description='取得新化高中官網的前 5 則公告')
async def announcement(ctx):
    await ctx.respond('正在處理中...')
    list_data = get_announcement()
    await ctx.respond(list_data)

@bot.slash_command(name='rating',description='查詢某個 user 的 codeforces rating')
async def rating(ctx,handle: str):

    if( get_user_data(handle) == 'No User' ):
        await ctx.respond('查無此人，或 CF API 掛掉了')
    else:
        data = get_user_data(handle)
        embed=discord.Embed(title=" ", color=0x06f5f9)
        embed.set_author(name= data["handle"] + " 的 Codeforces 個人資料")
        embed.set_thumbnail(url = data["titlePhoto"])
        embed.add_field(name="Rating:", value = data["rating"], inline=True)
        embed.add_field(name="Rank:", value = data["rank"], inline=True)

        await ctx.respond( embed = embed )

bot.run(token)