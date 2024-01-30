
from django.urls import path
from website.views import index_view,contact, about

urlpatterns = [
    path('contact',contact),
    path('about',about),
    path('',index_view)
    
]
