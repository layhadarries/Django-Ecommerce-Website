# views handles requests n responses

from django.http import HttpResponse

def hello_geeks(request):
    # you can straight up inject html.
    # i think this is where you design what you want the website to produce, like the visuals
    return HttpResponse("Abooga wooga")