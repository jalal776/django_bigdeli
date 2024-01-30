from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

def contact(request):
    return HttpResponse("<h1>Contact</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")

# def json_test(request):
#     return JsonResponse({'name':'Jalal'})

def index_view(request):
    return HttpResponse('<h1>Index Page</h1>')


