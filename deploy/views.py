# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator


def index(request):
    """部署列表
    :param request:
    """
    list = [1,2,3,4,5,6,7,8,9,0,1,2,3]
    paginator = Paginator(list, 10)
    pages = paginator.page_range
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        list = paginator.page(page)
    except:
        list = paginator.page(paginator.num_pages)
    return render(request, "deploy/index.html", locals())
