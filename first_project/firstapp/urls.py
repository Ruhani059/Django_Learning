from django.conf.urls import url
from firstapp import views

urlpatterns = [
    url(r'^index',views.index,name='index'),
    url(r'^$',views.help,name='help')
]
