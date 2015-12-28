from django.shortcuts import render
from django.http import JsonResponse
from .models import Update


def select(request):
    data = {}
    if request.POST:
        did = request.POST.get('did')
        ret = Update.objects.get(pk=did)
        data['status'] = ret.status
        data['project'] = ret.update_project
    return JsonResponse(data)
