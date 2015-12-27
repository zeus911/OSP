# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from django.http import JsonResponse
from cmdb.models import Update


def index(request):
    """部署列表
    :param request:
    """
    list = Update.objects.all().order_by("-pk")
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


def deploy(request):
    if request.POST:
        did = request.POST.get('did')
        return HttpResponse(did)
    return HttpResponse(1)
