from django.shortcuts import render
from .models import Noticia

# Create your views here.
def noticia(request):
    noticia = Noticia.objects.all()
    return render(request,'noticia/noticia.html',{'noticia':noticia})