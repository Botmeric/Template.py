import asyncio
import json
import logging
import sys
import traceback

import aiohttp
import discord
from discord.ext import commands

from cogs.utils import context
from cogs.utils.config import Config
from database import Db

log = logging.getLogger(__name__)



class Bot(commands.AutoShardedBot):


    def __init__(self, *args, **kwargs):
        super().__init__(max_messages=None, command_prefix="?", case_insensitive=True, heartbeat_timeout=150.0)

        self.settings = kwargs.get('settings')

        self.owner_ids = self.settings.get('owner_ids')

        self.db = Db(self.settings.get('db_url'), self)

        self.session = aiohttp.ClientSession(loop=self.loop)

        self.load_extensions()


    async def on_ready(self):
        pass


    async def on_message(self, message):
        ctx = await self.get_context(message, cls=context.Context)
        if ctx.command is None:
            return

        if ctx.command:
            await ctx.channel.trigger_typing()
            await self.invoke(ctx)


    async def on_command_error(self, ctx: context.Context, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.author.send('This command cannot be used in private messages.')
        elif isinstance(error, commands.DisabledCommand):
            await ctx.author.send('Sorry. This command is disabled and cannot be used.')
        elif isinstance(error, commands.CommandInvokeError):
            original = error.original
            if not isinstance(original, discord.HTTPException):
                print(f'In {ctx.command.qualified_name}:', file=sys.stderr)
                traceback.print_tb(original.__traceback__)
                print(f'{original.__class__.__name__}: {original}', file=sys.stderr)
        elif isinstance(error, commands.ArgumentParsingError):
            await ctx.send(error)


    async def on_raw_reaction_add(self, payload):
        pass
    

    async def on_raw_reaction_remove(self, payload):
        pass


    async def on_guild_join(self, guild):
        pass


    async def on_guild_remove(self, guild):
        pass


    async def close(self):
        await super().close()
        await self.session.close()


    def load_extensions(self):
        extensions = [
            "cogs.example"
        ]

        log.info('Loading extentions...')
        for extension in extensions:
            try:
                self.load_extension(extension)
            except Exception as ex:
                log.exception(ex)

        log.info('Finished loading extensions.')


    def run(self, *args):
        self.loop.run_until_complete(self.start(*args))
