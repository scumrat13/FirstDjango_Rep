from django.shortcuts import render
from django.http import HttpResponse

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

author_info = {
    "first_name": "Иван",
    "middle_name": "Петрович",
    "last_name": "Иванов",
    "phone": "8-923-600-01-02",
    "email": "vasya@mail.ru"
}

def home(request):
    # text = """
    # <h1>"Изучаем django"</h1>
    # <strong>Автор</strong>: <i>Привет Приветович</i>
    # """
    # return HttpResponse(text)
    return render(request, "index.html")

def about(request):
    return HttpResponse(
        f'Имя: <b>{author_info["first_name"]}</b><br>'
        f'Отчество: <b>{author_info["middle_name"]}</b><br>'
        f'Фамилия: <b>{author_info["last_name"]}</b><br>'
        f'Телефон: <b>{author_info["phone"]}</b><br>'
        f'Email: <b>{author_info["email"]}</b>'
    )
    
def item_info(request, item_id):
    back_to_item_list = f'<br> <a href="/items"> Обратно к списку товаров </a>'
    item = None
    for i in items:
        if i['id'] == item_id:
            item = i
            break
    if item:
        return HttpResponse(
            f'<h1>{item["name"]}</h1><h2>Количество: {item["quantity"]}</h2>{back_to_item_list}'
        )
    else:
        return HttpResponse(
            f'<h1>Товар с id={item_id} не найден</h1> {back_to_item_list}' 
        )
    
def all_items(request):
    items_info = '<ol>'
    for item in items:
        items_info+= f'<li>{item["name"]}. <a href="/item/{item["id"]}/" target="_blank"> Страница товара</a></li>'
    items_info += '</ol>'

    return HttpResponse(items_info)