from aiogram import Bot, Dispatcher, executor, types

import translators

bot = Bot(token='2109667277:AAF7H179Zj9baAIMwH2PZDstwFXx3Ky0oSk')
dp = Dispatcher(bot)

english=types.InlineKeyboardButton(text='English🇺🇸',callback_data='en')
uzbek=types.InlineKeyboardButton(text='Uzbek🇺🇿',callback_data='uz')
russian=types.InlineKeyboardButton(text='Russian🇷🇺',callback_data='ru')
kb_inline=types.InlineKeyboardMarkup().add(english,uzbek,russian)


@dp.message_handler(commands=['start'])
async def button(message:types.Message):
    await message.answer("Menga Matinni Jo'nating. Men uni Tarjima Qilib Beraman ",)


text=''
@dp.message_handler()
async def transmessage(message:types.Message):
    global text
    text=message.text
    try:
        await message.edit_text(text,reply_markup=kb_inline)
    except:
        await message.answer(text,reply_markup=kb_inline)


@dp.callback_query_handler(text=['en', 'uz', 'ru'])
async def changelang(call:types.CallbackQuery):
    global text
    if call.data=='en':
        text=translators.translate_text(query_text=f'{text}',translator='google',from_language='auto',to_language='en')
        await call.message.edit_text(text,reply_markup=kb_inline)
    if call.data=='uz':
        text=translators.translate_text(query_text=f'{text}',translator='google',from_language='auto',to_language='uz')
        await call.message.edit_text(text,reply_markup=kb_inline)
    if call.data=='ru':
        text=translators.translate_text(query_text=f'{text}',translator='google',from_language='auto',to_language='ru')
        await call.message.edit_text(text,reply_markup=kb_inline)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
