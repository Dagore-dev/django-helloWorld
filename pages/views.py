from django.http import HttpRequest, HttpResponse


# Create your views here.
def home_page_view(request: HttpRequest):
    return HttpResponse('¡Hola mundo!')
