from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Topic,Webpage,AccessRecord

from . import forms
# from forms import FormName

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    my_dict = {'insert_me':'Hello Ruhani. Today is your Birthday... This is views.py!'}
    return render(request,'firstapp/index.html',context=date_dict)

def help(request):
    help_dict = {'help_insert':'Help Page'}
    return render(request,'firstapp/help.html',context=help_dict)

def form_name_view(request):
    form = forms.FormName()
    return render(request,'form_name_html',{'form':form})
