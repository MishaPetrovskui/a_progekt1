def keyboard_get():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="+1", callback_data='+1'),
                types.InlineKeyboardButton(text="-1", callback_data='-1'),
                types.InlineKeyboardButton(text="Stop", callback_data='stop'))
    return builder


@dp.message(Command("counter"))
async def cmd_counter(message: types.Message, state: FSMContext):
    nomer = 0
    await state.update_data(Nomer=nomer)
    await message.answer(f'Значення: {nomer}', reply_markup=keyboard_get().as_markup())


@dp.callback_query(F.data == '+1')
async def adjust_counter_callback(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    nomer = data.get('Nomer')
    nomer += 1
    await state.update_data(Nomer=nomer)
    await callback.message.edit_text(f'Значення: {nomer}',
                                     reply_markup=keyboard_get().as_markup())
    await callback.answer()


@dp.callback_query(F.data == '-1')
async def adjust_counter_callback(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    nomer = data.get('Nomer')
    nomer -= 1
    await state.update_data(Nomer=nomer)
    await callback.message.edit_text(f'Значення: {nomer}',
                                     reply_markup=keyboard_get().as_markup())
    await callback.answer()


@dp.callback_query(F.data == 'stop')
async def adjust_counter_callback(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    nomer = data.get('Nomer')
    await callback.message.edit_text(f"Кінечне значення: {nomer}")
    await callback.answer()
