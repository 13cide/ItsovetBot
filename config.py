import telebot as tb
import pickle

bot = tb.TeleBot('5208301560:AAExKJUqImX7LQEK8C8VuLlZFNJTmvO7OK0')

with open('data/users_base', 'rb') as file:
    users = pickle.load(file)

with open('data/goals', 'rb') as file:
    marks = pickle.load(file)


def update():
    with open('data/users_base', 'wb') as file1:
        pickle.dump(users, file1)
    with open('data/goals', 'wb') as file2:
        pickle.dump(marks, file2)


sorry_message = "Извините, но мы не можем идентифицировать вас, пока у вас отсутствует" \
                "имя пользователя в телеграмме, чтобы это исправить, перейдите: настройки - " \
                "изменить профиль - выбрать имя пользователя. После этого свяжитесь с нашим " \
                "разработчиком https://t.me/Akhlopp \n\n c уважением, ваш ITsovet"

ITsovet_id = -627225011
