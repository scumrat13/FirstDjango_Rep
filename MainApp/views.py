from django.shortcuts import render
from django.http import HttpResponse

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

for item in items:
    print

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
    
def item_info(request, item_id):
    item = None
    for i in items:
        if i['id'] == item_id:
            item = i
            break
    if item:
        return HttpResponse(
            (f'<h1>{item["name"]}</h1><h2>Количество: {item["quantity"]}</h2>')
        )
    else:
        return HttpResponse(
            f'<h1>Товар с id={item_id} не найден' 
        )