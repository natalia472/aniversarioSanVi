from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def about(request):
    return render(request,'core/about.html')

def contacto(request):
    return render(request,'core/contact.html')


contenido_html = """
<h1>Mi primera pagina de inicio</h1>
<ul>
    <li><a href="/">Indice</a></li>
    <li><a href="/about/">Sobre mi</a></li>
"""