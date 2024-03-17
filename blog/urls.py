from django.urls import path
from blog.views import blog_view,single_view,test

app_name='blog'
urlpatterns = [
    path('',blog_view,name='index'),
    path('<int:pid>',single_view,name='single'),
    # path('post-<int:pid>',test,name='test'),
    

]