from django.http import HttpResponse

def saludo(request): # Primera vista

    return HttpResponse("¡Hola mundo! ¡Este es nuestro primer trabajo con Django!")

