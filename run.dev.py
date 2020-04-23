import logging

from bot import Bot
from cogs.utils.config import Config


logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='%H:%M')

settings = Config('config/env.dev.json').all()

bot = Bot(settings=settings)

bot.run(settings['token'])