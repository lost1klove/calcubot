from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, User

from keyboards.inline.callback_data import action_callback
from keyboards.inline.choice_buttons import choice
from loader import dp, logger
from mod_calc import sum_data, sub_data, mul_data, div_data

operator = {"+": sum_data, "-": sub_data, "*": mul_data, "/": div_data}
n = ""


@dp.message_handler(Command("start"))
async def wlcme_msg(message: Message):
    await message.answer(text=f"Привет, {message.from_user.first_name} :) Давай посчитаем!",
                         reply_markup=choice)


@dp.callback_query_handler(text_contains="<")
async def delete_char(call: CallbackQuery):
    global n
    if n:
        n = n[:-1]
        if not n:
            await call.message.edit_text("0", reply_markup=choice)
        await call.message.edit_text(f"{n}", reply_markup=choice)
    else:
        await call.answer(cache_time=20)


@dp.callback_query_handler(text_contains="C")
async def erase(call: CallbackQuery):
    global n
    n = ""
    await call.message.edit_text("0", reply_markup=choice)


@dp.callback_query_handler(text_contains="=")
async def result(call: CallbackQuery):
    global n

    await call.answer(cache_time=10)

    if n:
        n_list = n.split()
        if len(n_list) > 1:
            try:
                ch_list = [float(i) if "." in i else int(i)
                              if i.replace(".", "", 1).isdigit()
                              else i for i in n_list]

                in_list = [i for i, v in enumerate(ch_list) if isinstance(v, str) and v in "*/"]


                while in_list:
                    k = in_list[0]
                    a, s, b = ch_list[k - 1: k + 2]
                    ch_list[k - 1: k + 2] = [operator[s](a, b)]
                    in_list = [i for i, v in enumerate(ch_list) if isinstance(v, str) and v in "*/"]

                while len(ch_list) > 1:
                    f, op, s = ch_list[:3]
                    ch_list[:3] = [operator[op](f, s)]

            except (ValueError, TypeError, KeyError):
                await call.message.edit_text("Введите значения", reply_markup=choice)
            else:
                await call.message.edit_text(f"{n}"
                                             f" = {ch_list[0]}",
                                             reply_markup=choice)
                logger.debug(f'Результат {n} = {ch_list[0]}')
            n = ""
    else:
        logger.debug(f'{update.effective_user.first_name} не ввел значения')
        await call.message.edit_text("Введите значения", reply_markup=choice)


@dp.callback_query_handler(action_callback.filter())
async def nums_choice(call: CallbackQuery, callback_data: dict):
    global n

    await call.answer(cache_time=1)
    data = callback_data["item_name"]
    if data in "+-*/":
        n += f" {data} "
    else:
        n += data
    await call.message.edit_text(f"{n}",
                                 reply_markup=choice)
    logger.debug(f'Пользователь ввел {n}')


@dp.message_handler()
async def echo(message: Message):
    logger.debug('Не верный ввод пользователем')
    await message.answer(f'{message.from_user.first_name},'
                         f' пожалуйста, кликай кнопки калькулятора!',
                         reply_markup=choice)
