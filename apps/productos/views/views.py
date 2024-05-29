from django.shortcuts import render

# Create your views here.

def productosV(request):
    return render(request, 'productosV.html')