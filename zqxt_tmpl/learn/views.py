from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    # display_str = u"我在自强学堂学习Django，用它来建网站!"
    # return render(request, 'home.html', {"displayStr": display_str})
    # tutorail_list = ["HTML", "CSS", "jQuery", "Python", "Django"]
    # return render(request, "home.html", {'TutorialList': tutorail_list})
    # dict_info = {'site': u'zqxt', 'content': u'gezhong it jishu jiaocheng'}
    # return render(request, 'home.html', {'dict_info': dict_info})
    # list = map(str, range(100))
    list = []
    return render(request, 'home.html', {'num_list': list})


def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def numset(request):
    num = 50
    return render(request, 'home.html', {'num_set': num})
