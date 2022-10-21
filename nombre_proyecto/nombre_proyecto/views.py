
from django.shortcuts import render

def index(request):
    return render(request,'index.html', {
      'variable': 'producto',
      'var1': 89
          #contexto
        } )

def contact(request):
  return render(request,'contact.html')
  
    