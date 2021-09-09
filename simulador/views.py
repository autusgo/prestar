from django.http import HttpResponse


def index(request):
    return HttpResponse("Acá va a estar el simulador")