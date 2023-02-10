from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_breakfast = KeyboardButton('🍳Завтрак🍳')
button_second_breakfast = KeyboardButton('🍪II завтрак🍪')
button_lunch = KeyboardButton('🍲Обед🍲')
# button_afternoon_snack = KeyboardButton('🧇Полдник🧇')
button_dinner = KeyboardButton('🍛Ужин🍛')
choosing_meal_kb = ReplyKeyboardMarkup(resize_keyboard=True)
choosing_meal_kb.row(button_breakfast, button_second_breakfast).row(button_lunch).row(button_dinner)
delete_kb = ReplyKeyboardRemove()