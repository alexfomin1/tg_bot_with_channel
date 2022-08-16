from aiogram import Bot, Dispatcher
from filters import IsAdminFilter, IsOwnerFilter, MemberCanRestrictFilter
import config
import logging

logging.basicConfig(level=logging.INFO)



bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

#dp.filters_factory.bind(IsOwnerFilter)
dp.filters_factory.bind(IsAdminFilter)
dp.filters_factory.bind(MemberCanRestrictFilter)