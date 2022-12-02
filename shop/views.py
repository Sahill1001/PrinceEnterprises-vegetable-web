from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order
from math import ceil
import json


# Create your views here.
def index(request):
    prod=Product.objects.all()
    params={'allProd':prod }
    return render(request,"shop/index.html", params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject=request.POST.get('subject','')
        desc= request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,subject=subject)
        contact.save()
    return render(request, 'shop/contact.html')


def prodPage(request,myId):
    product=Product.objects.filter(id=myId).first()
    related=Product.objects.filter(category=product.category)
    params={"product":product,"related":related}
    return render(request,"shop/product-single.html", params)

def shop(request):
    prod=Product.objects.all()
    params={'allProd':prod}
    return render(request,"shop/shop.html",params)


def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query= request.GET.get('search')
    prod=Product.objects.all()
    prodr = [item for item in prod if searchMatch(query, item)]
    if len(prodr) != 0:
        prod=prodr
        params={'allProd':prod,"msg": ""}
    if len(prodr) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html',params)
         
def cart(request):
    return render(request,"shop/cart.html")

def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        last_name=request.POST.get('last_name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city','')
        zip_code=request.POST.get('zip', '')
        phone=request.POST.get('phone', '')

        order = Order(items_json= items_json, name=name, last_name =last_name, email=email, address= address, city=city,zip_code=zip_code, phone=phone)
        order.save()
        
        thank=True
        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'shop/checkout.html')





# def stationery(request):
#     prod=Product.objects.filter(category="electronics")
#     params={'allProd':prod }
#     return render(request,"shop/index.html", params)

# def beauty(request):
#     prod=Product.objects.filter(category="beuty")
#     params={'allProd':prod }
#     return render(request,"shop/index.html", params)

#def wishlist(request):
#    return render(request, "shop/wishlist.html")