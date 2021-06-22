from django.shortcuts import render
import numpy as np
from . models import Quote
from django.http import JsonResponse

# Create your views here.

def index(request):
    quote = Quote.objects.first()
    return render(request,"get_quote/quote.html", {
        "quote_text":quote.quote,
        "quote_author": quote.author
    })
    

def get_quote(request):
    random_quote = Quote.objects.filter(id=[np.random.choice(430, 1, replace=False)[0]][0]).first()
    return render(request,"get_quote/quote.html", {
        "quote_text":random_quote.quote,
        "quote_author": random_quote.author
    })
 
def id_quote(request):
    quotes = Quote.objects.all()
    return render(request,"get_quote/index.html", {
        "quotes":quotes
    })


def n_quotes(request, *args, **kwargs):
    data = Quote.objects.all().count()
    return JsonResponse(data)    

