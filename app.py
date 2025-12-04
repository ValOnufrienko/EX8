from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    current_hour = now.hour
    greeting = ''

    # Логіка зміни вітання в залежності від години
    if 5 <= current_hour < 12:
        greeting = 'Good morning'
    elif 12 <= current_hour < 18:
        greeting = 'Good afternoon'
    elif 18 <= current_hour < 22:
        greeting = 'Good evening'
    else:
        greeting = 'Good night'

    # Список із щонайменше 5 задач
    tasks = [
        'Купити продукти',
        'Зробити домашнє завдання з Python',
        'Погуляти з собакою',
        'Подзвонити бабусі',
        'Прибрати в кімнаті'
    ]

    # Передаємо змінні greeting та tasks у шаблон index.html
    return render_template('index.html', greeting=greeting, tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
