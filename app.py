from aiogram import executor, Bot, Dispatcher, types
from keyborads import *
bot = Bot(token='6191956586:AAEycG1ebRMhEq3iMBpzlAg0CXTcOIeaPXc')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def show_keyboards(message: types.Message):
    name = message.from_user.full_name
    await message.answer(text=f"Assalomu alaykum {name},\nIltimos ona tilingizni tanlang😊", reply_markup=language)


@dp.message_handler(text='uz🇺🇿')
async def uz_hendler(message: types.Message):
    name = message.from_user.full_name
    photo = 'https://lh3.googleusercontent.com/p/AF1QipNowR_J62Gzk8QB_CjWz9ijW3OM_JC0357eKnDW=w768-h768-n-o-v1'
    await message.answer_photo(photo=photo)
    await message.answer(
        text=f"Assalomu alaykum {name},\nSiz 'Azon' kitob do'konlari rasmiy botining asosiy menyusidasiz.\n"
             f"Iltimos quyidagi tugmalardan o'zingizga keraklisini tanlang😊", reply_markup=keyboards1)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
