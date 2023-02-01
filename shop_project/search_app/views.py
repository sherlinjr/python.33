from django.shortcuts import render
from shop_app.models import product
from django.db.models import Q
# Create your views here.


def searchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request,'search.html',{'query':query, 'products': products})
