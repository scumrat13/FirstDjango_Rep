from django.shortcuts import render
from django.http import HttpResponse

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

def home(request):
    context = {
        "name": "Привет Приветович",
        "email": "privet@mail.pr"
    }
    return render(request, "index.html", context)

def about(request):
    context= {
    "first_name": "Иван",
    "middle_name": "Петрович",
    "last_name": "Иванов",
    "phone": "8-923-600-01-02",
    "email": "vasya@mail.ru"
    }
    return render(request, "about.html", context)
    
def item_info(request, item_id):
    item = None
    for i in items:
        if i['id'] == item_id:
            item = i
            break
    if item:
        context = {
            "item_name": item["name"],
            "item_quantity": item["quantity"]
        }
        return render(request, "item.html", context)
    return HttpResponse(f'<h2>Товар с id={item_id} не найден</h2> <br> <a href="/items"> Обратно к списку товаров </a>')

    
def all_items(request):
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)