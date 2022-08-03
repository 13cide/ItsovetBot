from telebot import types


'''menu'''
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)

btn1 = types.KeyboardButton("Профиль")
btn2 = types.KeyboardButton("Сменить ник")
btn3 = types.KeyboardButton("Топ")
btn4 = types.KeyboardButton("Задачи ITsovet")
btn5 = types.KeyboardButton("База знаний")
btn6 = types.KeyboardButton("Подать заявление на получение рейтинга/жалобу")

menu.add(btn1, btn2, btn3)
menu.add(btn4, btn5)
menu.add(btn6)


'''menu_with_admin'''
menu_with_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)

admin_btn = types.KeyboardButton("админ")

menu_with_admin.add(btn1, btn2, btn3)
menu_with_admin.add(btn4, btn5)
menu_with_admin.add(btn6, admin_btn)
