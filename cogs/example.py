import asyncio

import discord
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def example(self, ctx):
        await ctx.send(f'Hello, I\'m {self.bot.user.name}')


def setup(bot):
    bot.add_cog(Example(bot))
