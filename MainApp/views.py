from django.shortcuts import render
from django.http import HttpResponse
from MainApp.models import Item


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
    
def item_info(request, item_id:int):
    try:
        item = Item.objects.get(id=item_id)
        context = {"item": item}
        return render (request, "item.html", context)
    except Item.DoesNotExist:
        return HttpResponse(f'<h2>Товар с id={item_id} не найден</h2> <br> <a href="/items"> Обратно к списку товаров </a>')

    
def all_items(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)