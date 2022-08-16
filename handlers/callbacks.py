from aiogram import types
from decouple import config
from dispatcher import dp
import config
from decouple import config


@dp.callback_query_handler(lambda x: x.data == 'get_link_button')
async def process_callback_get_link_button(c: types.CallbackQuery):
	try:
		member = await bot.get_chat_member(config('CHANNEL_ID'), x.from_user.id)

		if (member['status'] in ('member', 'creator', 'administrator')):
			with open('link.txt', 'r') as f:
				content = f.readlines()
				f.close()
			await bot.answer_callback_query(x.id, f'Link - {content[0].strip()}', show_alert=True)
		else:
			await bot.answer_callback_query(x.id, 'First you need to subscribe to the channel!', show_alert=True)
	except:
		await bot.answer_callback_query(x.id, 'First you need to subscribe to the channel!', show_alert=True)