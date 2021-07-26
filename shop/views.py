from django.shortcuts import render, redirect, HttpResponseRedirect
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
from .models import Product
# Create your views here.

def home(request):
    products = Product.objects.all()    
    return render(request, 'product_list.html', {'products':products})


def sortLowtoHigh(request):
    products = Product.objects.all().order_by('price')
    return render(request, 'product_list.html', {'products':products})