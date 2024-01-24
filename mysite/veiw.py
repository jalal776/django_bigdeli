from django.http import HttpResponse,JsonResponse

def html_test(request):
    return HttpResponse("<h1>test_html</h1>")

def json_test(request):
    return JsonResponse({'name':'Jalal'})
