from config import *
from requests import exceptions
from murkups import menu, menu_with_admin
import menu


@bot.message_handler(commands=["start"])
def start(m):
    try:
        user = users[m.from_user.username]

        if user["is_admin"]:  # если пользователь админ - есть ещё одна кнопка
            mark = menu_with_admin
        else:
            mark = menu

        bot.send_message(m.chat.id, 'IT совет приветствует тебя, ' + user['name'],
                         reply_markup=mark)
        user['Chat_id'] = m.chat.id
        update()
    except KeyError:
        bot.send_message(m.chat.id, sorry_message)


print("\nbot started successfully\n")

if __name__ == '__main__':
    try:
        bot.polling(none_stop=True, interval=0)

    except exceptions.ConnectionError:
        pass
