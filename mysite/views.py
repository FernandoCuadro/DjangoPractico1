#from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import Template, Context

def Pagina(request):

#    doc=open("C:/Users/ferma/djangogirls/mysite/Inicio.html")
 #   pl = Template(doc.read())
  #  doc_externo.close()
    
   # documento = pl.render(Context())
    return render(request, 'Inicio.html')