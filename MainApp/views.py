from django.shortcuts import render
from django.http import HttpResponse

user_info = {
    "first_name": "Иван",
    "middle_name": "Петрович",
    "last_name": "Иванов",
    "phone": "8-923-600-01-02",
    "email": "vasya@mail.ru"
}

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Привет Приветович</i>
    """
    return HttpResponse(text)

def about(request):
    return HttpResponse(
        f'Имя: {user_info["first_name"]}<br>'
        f'Отчество: {user_info["middle_name"]}<br>'
        f'Фамилия: {user_info["last_name"]}<br>'
        f'Телефон: {user_info["phone"]}<br>'
        f'Email: {user_info["email"]}'
    )
    