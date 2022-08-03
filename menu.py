from config import *


def profile(m):
    try:
        user = users[m.from_user.username]

        if user['is_admin']:
            message = "Вы член совета"
        else:
            message = "Вы не член совета"

        bot.send_message(m.chat.id, user['real_name'] + ' (' + user['name'] + ')\n\n' +
                         'Ваш рейтинг : ' + str(user['rating']) + '\n\n' + message)

    except KeyError:
        bot.send_message(m.chat.id, sorry_message)


def goals(m):
    if len(marks) == 0:
        bot.send_message(m.chat.id, "Сейчас задач нет")
    else:
        msg = ""
        for i in range(len(marks)):
            msg += str(i + 1) + ')' + marks[i] + '\n'
        bot.send_message(m.chat.id, msg)


@bot.message_handler(content_types='text')
def menu(m):
    if m.text == "Профиль":
        profile(m)
    # if m.text == "Сменить ник":
    #     change_name.change_name(m)
    # if m.text == "Топ":
    #     social_rating_update(m)
    if m.text == "Задачи ITsovet":
        goals(m)
    # if m.text == "База знаний":
    #     top(m)
    # if m.text == "Подать заявление на получение рейтинга/жалобу":
