from django.shortcuts import render
import numpy as np
from . models import Quote
# Create your views here.

def index(request):
    return render(request,'get_quote/index.html',{
        'quotes': Quote.objects.all()
    })
    
quote_text = []
quote_author = [] 
random_quote = [] 
def get_quote(request):
    random_quote = Quote.objects.filter(id=[np.random.choice(430, 1, replace=False)[0]][0]).first()
    quote_author = random_quote.author
    quote_text = random_quote.quote
    return render(request,"get_quote/quote.html", {
        "quote_text":quote_text,
        "quote_author": quote_author
    })

