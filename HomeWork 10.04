import random
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6553252483:AAGocK7axwAOn6MvISxwlZfnVngR_7kxN5o")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    for i in range(100):
        await message.answer("Добрый день!")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
        await message.answer(text='/help - отримати довідку за командами\n/start - запустити бота\n/roll - випадкове число від 1 до 100\n/roll (number) - випадкове число від 1 до введенного числа\n/roll (number) (number) - випадкове число від першого числа до другого числа\n/roll (number) (number) (number)... - випадковий параметр')
        # await message.reply(text='Help command')
        # await bot.send_message(chat_id=message.chat.id, text='Help command')


@dp.message(Command("roll"))
async def cmd_roll(message: types.Message, command: CommandObject):
    if command.args is not None:
        args = command.args.split()
        if len(args) == 1:
            max_value = int(args[0])
            await message.answer(f'Випадкове число від 1 до {max_value}: {random.randint(1, max_value)}')
        elif len(args) == 2:
            min_value = int(args[0])
            max_value = int(args[1])
            await message.answer(f'Випадкове число від {min_value} до {max_value}: {random.randint(min_value, max_value)}')
        else:
            random_value = random.choice(args)
            await message.answer(f'Випадковий параметр в {" ".join(args)}: {random_value}')
    else:
        await message.answer(f'Випадкове число від 1 до 100: {random.randint(1, 100)}')

@dp.message()
async def cmd_roll(message: types.Message):
    await message.answer(message.text)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
