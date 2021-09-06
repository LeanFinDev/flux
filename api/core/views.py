from django.http import HttpResponse


def index(request):
    return HttpResponse("Flux API project...")
