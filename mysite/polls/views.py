import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from polls import models

# Create your views here.
user_list = [
    {
        "user": "jack",
        "pwd": "abc"
    },
    {
        "user": "tom",
        "pwd": "ABC"
    },
]


def index(request):
    # return HttpResponse("hello world!")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # print(username, password)
        # temp = {"user": username, "pwd": password}
        # user_list.append(temp)
        # 添加数据到数据库
        models.UserInfo.objects.create(user=username, pwd=password)
    # 从数据库中读取数据
    user_list = models.UserInfo.objects.all()

    return render(request, "index.html", {"data": user_list})


# 读取前端Book信息到数据库中
@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = models.Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as identifier:
        response['msg'] = json.load(identifier)
        response['error_num'] = 1

    return JsonResponse(response)


# 读取数据库Book信息 返回到前端Vue
@require_http_methods(["GET"])
def show_books(request):
    response = {}

    try:
        books = models.Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as identifier:
        response['msg'] = json.load(identifier)
        response['error_num'] = 1

    return JsonResponse(response)
