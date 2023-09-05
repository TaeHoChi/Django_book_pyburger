from burgers.models import Burger
from django.shortcuts import render
from django.http import  HttpResponse

def main(request):
    return HttpResponse("안녕하세요, pyburger입ㄴㅛ요새ㅎㄴ")

def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄거버 목록: ", burgers)
    context = {
        "burgers": burgers,
    }
    return render(request, "burger_list.html", context)

def burger_search(request):
    keyword = request.GET.get("keyword")
    if keyword is not None:
        burgers = Burger.objects.filter(name__contains=keyword)
    else:
        burgers = Burger.objects.none()
    context = {
        "burgers": burgers,
    }
    return render(request, "burger_search.html", context)