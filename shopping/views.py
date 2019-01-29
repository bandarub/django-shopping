from django.shortcuts import render
from .models import Product
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from django.db.models import Q

def home(request):
    context = {
        "products":Product.objects.all()
    }
    return render( request, "shopping/home.html", context)

class ProductListView(ListView):
    model = Product
    template_name = "shopping/home.html"
    context_object_name = "products"

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'category', 'description', 'price']

def search(request):        
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(category__icontains=query) 
            results= Product.objects.filter(lookups).distinct()

            context={'books': results}

            return render(request, 'shopping/search.html', context)

        else:
            return render(request, 'shopping/search.html')

    else:
        return render(request, 'shopping/search.html')

