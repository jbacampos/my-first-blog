from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, guys! We are at the polls index")


# Create your views here.
