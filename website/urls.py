
from django.urls import path
from website.views import index_view,contact, about

app_name='website'
urlpatterns = [
    path('contact',contact,name='contact'),
    path('about',about,name='about'),
    path('',index_view,name='index')
    
]
