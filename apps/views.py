from django.shortcuts import render, get_object_or_404
from .models import Product, Cartitem
import requests
from django.http import JsonResponse
import json
# Create your views here.
def home(request):
      product = Product.objects.all()
     

          

      return render(request, "index.html", {"product": product} )

# list cart
def cartview(request):
      cartitem = {}
      cartitem['dataset'] = Cartitem.objects.all().order_by("name")
      print(cartitem)
      return render(request, "cart.html", cartitem)

# add cart
def addcart(request):
      
      ids = request.get("iid")
      sess_pro_id = request.session.get("ids")
      print(sess_pro_id)      
      # data = json.loads(request.body)

      # productId = data["productId"]
      # action = data["action"]
      # customer = request.user 
      
      # print(customer)
      # print("action:", action)
      # print("productId:", productId)
      
      
      return render(request, "addcart.html")


