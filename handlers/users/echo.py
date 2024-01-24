import asyncio
from random import choice
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from states.test import RandomState

router = Router()


@router.message(RandomState.name_amount)
async def get_name_amount(message: types.Message, state: FSMContext):
    try:
        # Try to convert the entered value to an integer
        name_amount = int(message.text)
        if name_amount <= 0:
            raise ValueError("Please enter a positive number.")

        await state.set_data({"name_amount": name_amount})
        await message.answer("Enter a name:")
        await state.set_state(RandomState.name)
    except ValueError:
        await message.answer("Please enter a valid positive number.")


@router.message(RandomState.name)
async def get_name(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        names = data.get("names", [])
        name_amount = data.get("name_amount", 0)
        names.append(message.text)
        await state.set_data({"names": names, "name_amount": name_amount})
        if len(names) < name_amount:
            await message.answer("Enter a name:")
        else:
            await message.answer(
                f'The name that has been randomly selected is: <b>"{choice(names)}"</b>!\nCongratulations!')
            await asyncio.sleep(0.5)
            await message.answer("Enter the number of names you want to generate:")
            await state.set_state(RandomState.name_amount)
    except:
        await message.answer("An unexpected error occurred. Please try again.")
