from django.shortcuts import render

from .models import nextid

# Create your views here.
from django.http import HttpResponse

def index(request):
    idlist=nextid.objects.order_by('-nextid_time')[0:5]
    context = {
        'idlist': idlist,
    }
    if request.is_ajax():
        idlist=nextid.objects.order_by('-nextid_time')[0:5]
        context = {
            'idlist': idlist,
        }
        return render(request, 'index_subtemplate.html',context)
    else:
        return render(request, 'index1.html', context)