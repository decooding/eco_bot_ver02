from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
Main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["♻️ Узнать цветовой маркер отходов", "🔢 Коды переработки"]
Main_keyboard.add(*buttons)
Main_keyboard.add(KeyboardButton(text="❔ Задать вопрос экспертам")).add(KeyboardButton(text="Узнать качества воздуха"))
Main_keyboard.add(KeyboardButton(text="📍 Узнать ближайшие пункты приема вторсырья"))
Main_keyboard.add(KeyboardButton(text="💡 Советы"))
Color_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["🟦", "🟩", "🟥", "🟨"]
Color_keyboard.add(*buttons).add(KeyboardButton(text="🔄 Вернуться в главное меню"))
Digit_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣"]
Digit_keyboard.add(*buttons).add(KeyboardButton(text="🔄 Вернуться в главное меню"))
Gis_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
Gis_keyboard.add(InlineKeyboardButton("Утилизация пластмассы", url="https://2gis.kz/astana/search/Переработка%20пластика%20(утилизация%20пластмассы)/attributeId/70000201006749360"))
Gis_keyboard.add(InlineKeyboardButton("Магазин и пункт приема аккумуляторов", url="https://2gis.kz/astana/branches/70000001070520997?m=71.415418%2C51.131838%2F14.16"))
Gis_keyboard.add(InlineKeyboardButton("Утилизация батареек (приём батареек)", url="https://2gis.kz/astana/search/Утилизация%20батареек%20(приём%20батареек)/attributeId/70000201006752145/firm/70000001082885570/71.412839%2C51.140599?m=71.415418%2C51.131838%2F14.16"))
Gis_keyboard.add(InlineKeyboardButton("Прием металла (приём цветного лома)", url="https://2gis.kz/astana/search/Прием%20металла%20(приём%20цветного%20лома)/attributeId/70000201006752157?m=71.415418%2C51.125366%2F13.04"))