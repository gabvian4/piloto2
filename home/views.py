from django.shortcuts import HttpResponse, render

def index(request):
    return render(request, 'index.html')
def sobre(request):
    return render(request, 'sobre.html')
def contato(resquest):
    return render(resquest, 'contato.html')
def ajuda(resquest):
    return render(resquest, 'ajuda.html')
def local(request):
    return render(request, 'local.html')
def exibirItem(request,id):
    return render(request,'exibir_item.html',{'id':id})
def perfil(request,usuario):
    return render(request,'perfil.html',{'usuario':usuario})

