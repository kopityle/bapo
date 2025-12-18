from flask import Flask, render_template_string, request, redirect
import redis

app = Flask(__name__)
# Подключаемся к Redis, 'redis' - это имя сервиса из docker-compose.yml.
# decode_responses=True нужно, чтобы получать строки, а не байты.
db = redis.Redis(host='redis', port=6379, decode_responses=True)

# Весь HTML-код страницы храним прямо здесь для простоты.
# Он содержит список задач и форму для добавления новой.
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Список задач на Docker</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #f4f4f9; color: #333; max-width: 680px; margin: 40px auto; padding: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.1); border-radius: 8px; }
        h1 { color: #444; text-align: center; }
        ul { list-style: none; padding: 0; }
        li { background-color: #fff; padding: 15px; margin-bottom: 10px; border-left: 5px solid #5c67f2; border-radius: 4px; display: flex; align-items: center;}
        form { display: flex; margin-top: 30px; }
        input[type="text"] { flex-grow: 1; padding: 12px; border: 2px solid #ddd; border-radius: 4px 0 0 4px; font-size: 16px; }
        input[type="submit"] { padding: 12px 25px; border: none; background: #5c67f2; color: white; border-radius: 0 4px 4px 0; cursor: pointer; font-size: 16px; }
        input[type="submit"]:hover { background: #4a54c4; }
    </style>
</head>
<body>
    <h1>Список задач</h1>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>
    <form action="/" method="post">
        <input type="text" name="task" placeholder="Что нужно сделать?" required autocomplete="off">
        <input type="submit" value="Добавить">
    </form>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    # Если на страницу пришли данные из формы (методом POST)
    if request.method == 'POST':
        # Получаем текст задачи из формы
        task = request.form['task']
        # Добавляем задачу в список 'tasks' в базе данных Redis
        db.lpush('tasks', task)
        # Перенаправляем пользователя обратно на главную страницу, чтобы избежать повторной отправки формы
        return redirect('/')

    # Если страница просто открывается (методом GET)
    # Получаем весь список задач из Redis
    tasks_list = db.lrange('tasks', 0, -1)
    # Отображаем нашу HTML-страницу, передавая в нее список задач
    return render_template_string(HTML_TEMPLATE, tasks=tasks_list)