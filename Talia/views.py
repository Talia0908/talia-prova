from django.shortcuts import render, redirect
from . models import Produto, Cliente, CarrinhoDeCompras
from . forms import ProdutoForm, ClienteForm, CarrinhoDeComprasForm

def home(request):
    return render (request, 'home.html')

def produto_list(request):
    produtos = Produto.objects.all()
    return render (request, 'produto/list.html', {'produtos': produtos})

def produto_show(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    return render (request, 'produto/show.html', {'produto': produto})

def produto_form(request):
    if (request.method == "POST"):
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/primeira/produto/')
        else:
            return render (request, 'produto/form.html', {'form': form})
    else:
        form = ProdutoForm()
        return render (request, 'produto/form.html', {'form': form})

def produto_delete(request,produto_id):
    produto = Produto.objects.get(pk=produto_id)
    produto.delete()
    return redirect('/primeira/produto/')

def produto_editar(request,produto_id):
    if(request.method=='POST'):
        produto = Produto.objects.get(pk=produto_id)
        form = ProdutoForm(request.POST, instance = produto)
        if form.is_valid():
            form.save()
            return redirect('/primeira/produto/list')
        else:
            return render(request,'produto/editar.html',{'form':form, 'produto_id':produto_id})       
    else:
        produto = Produto.objects.get(pk=produto_id)
        form = ProdutoForm(instance=produto)
        return render(request,'produto/editar.html',{'form':form, 'produto_id':produto_id})


def cliente_list(request):
    clientes = Cliente.objects.all()
    return render (request, 'cliente/list.html', {'clientes': clientes})

def cliente_show(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    return render (request, 'cliente/show.html', {'cliente': cliente})

def cliente_form(request):

    if (request.method == "POST"):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/primeira/cliente/')
        else:
            return render (request, 'cliente/form.html', {'form': form})
    else:
        form = ClienteForm()
        return render (request, 'cliente/form.html', {'form': form})

def cliente_delete(request,cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    cliente.delete()
    return redirect('/primeira/cliente/')

def cliente_editar(request,cliente_id):
    if(request.method=='POST'):
        cliente = Cliente.objects.get(pk=cliente_id)
        form = ClienteForm(request.POST, instance = cliente)
        if form.is_valid():
            form.save()
            return redirect('/primeira/cliente/')
        else:
            return render(request,'cliente/editar.html',{'form':form, 'cliente_id':cliente_id})       
    else:
        cliente = Cliente.objects.get(pk=cliente_id)
        form = ClienteForm(instance=cliente)
        return render(request,'cliente/editar.html',{'form':form, 'cliente_id':cliente_id})


def carrinho_list(request):
    carrinhos = CarrinhoDeCompras.objects.all()
    return render (request, 'carrinho/list.html', {'carrinhos': carrinhos})

def carrinho_show(request, carrinho_id):
    carrinho = Carrinho.objects.get(id=carrinho_id)
    return render (request, 'carrinho/show.html', {'carrinho': carrinho})

def carrinho_form(request):
    if (request.method == "POST"):
        form = CarrinhoDeComprasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/primeira/carrinho/')
        else:
            return render (request, 'carrinho/form.html', {'form': form})
    else:
        form = CarrinhoDeComprasForm()
        return render (request, 'carrinho/form.html', {'form': form})

def carrinho_delete(request,carrinho_id):
    carrinho = CarrinhoDeCompras.objects.get(pk=carrinho_id)
    carrinho.delete()
    return redirect('/primeira/carrinho/list')

def carrinho_editar(request,carrinho_id):
    if(request.method=='POST'):
        carrinho = Carrinho.objects.get(pk=carrinho_id)
        form = CarrinhoForm(request.POST, instance = carrinho)
        if form.is_valid():
            form.save()
            return redirect('/primeira/carrinho/')
        else:
            return render(request,'carrinho/editar.html',{'form':form, 'carrinho_id':carrinho_id})       
    else:
        carrinho = Carrinho.objects.get(pk=carrinho_id)
        form = CarrinhoForm(instance=carrinho)
        return render(request,'carrinho/editar.html',{'form':form, 'carrinho_id':carrinho_id})
