from django.forms import ModelForm
from . models import Produto, Cliente, CarrinhoDeCompras

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
    
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
    
class CarrinhoDeComprasForm(ModelForm):
    class Meta:
        model = CarrinhoDeCompras
        fields = '__all__'
    