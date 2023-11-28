from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponsePermanentRedirect,HttpResponseNotFound, JsonResponse

def main(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    return HttpResponse(f'Главная страница сайта.Имя магазина {name}.Магазину {age} лет')

def news(request):
    # return HttpResponse('Новости')
    return HttpResponseRedirect('/shop/')
def cart(request, id):
    return HttpResponse(f'Корзина пользователя {id}')

def order(request, id):
    # return HttpResponse(f'Мои заказы.Пользователь {id}')
    return  HttpResponsePermanentRedirect('/shop/products/3/cart')
def product(request, id,pk):
    return HttpResponse(f'Страница с описанием продукта №{id}')
def faq(request):
    return HttpResponse('Помощь')
def index(request,id):
    people = ['Tom','Max','Edd']
    if id in range(0,len(people)):
        return HttpResponse(f'Наш победитель {people[id]}')
    else:
        return HttpResponseNotFound('Нет победителя')

def test(request):
    dict= {
        'name':'Vasya',
        'age': 18,
        'interests': 'games'
    }
    return  JsonResponse(dict)
def set(request):
    username = request.GET.get("username",None)
    response = HttpResponse(f'Добрый день {username}')
    response.set_cookie('username',username)
    return response

def get(request):
    username = request.COOKIES['username']
    return HttpResponse(username)