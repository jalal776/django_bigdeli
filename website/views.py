from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

def contact(request):
    # return HttpResponse("<h1>Contact</h1>")
    return render(request, 'website/contacts.html')

def about(request):
    # return HttpResponse("<h1>About</h1>")
    return render(request, 'website/about.html')

# def json_test(request):
#     return JsonResponse({'name':'Jalal'})

def index_view(request):
    # return HttpResponse('<h1>Index Page</h1>')
    return render(request, 'website/index.html')


