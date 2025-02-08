from django.shortcuts import HttpResponse, render

def index(request):
    return render(request, 'index.html')
def sobre(request):
    return render(request, 'sobre.html')
def contato(resquest):
    return render(resquest, 'contato.html')
def ajuda(resquest):
    return render(resquest, 'ajuda.html')
