from discord.ext import commands
import discord
import random

omikuji_results = [
    "あなたの運勢は大吉です",
    "あなたの運勢は中吉です",
    "あなたの運勢は小吉です",
    "あなたの運勢は吉です",
    "あなたの運勢は凶です",
    "あなたの運勢は大凶です"
]


class Omikuji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='omikuji', help='おみくじを引きます')
    async def omikuji(self, ctx):
        result = random.choice(omikuji_results)
        author = ctx.message.author
        pfp = author.avatar.url
        print(pfp)
        embed = discord.Embed(
            title=f'{ctx.author}の運勢', description=result, color=0x00b0f4)
        embed.set_thumbnail(url=pfp)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Omikuji(bot))
