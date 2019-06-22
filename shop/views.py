from math import ceil

from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render

from . models import Product,Contact
# Create your views here.

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)




def about(request):

    #return HttpResponse("hey about")
    return render(request, 'shop/about.html')

def contact(request):
    #return HttpResponse("hey contact ")
    if request.method =="POST":

      name = request.POST.get('name', '')
      email = request.POST.get('email', '')
      #phone = request.POST.get('phone')
      subject = request.POST.get('subject')
      message = request.POST.get('message')
      contact = Contact(name=name, email=email, subject=subject,  message=message)
      contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    #return HttpResponse("hey tracker")
    return render(request, 'shop/tracker.html')

def search(request):
    #return HttpResponse("hey search")
    return render(request, 'shop/search.html')

def checkout(request):
    #return HttpResponse("hey checkout")
    return render(request, 'shop/checkout.html')

def productview(request, id):
    #fetching product from id
    product= Product.objects.filter(id=id)
    return render(request, 'shop/productview.html', {'product': product[0]})
