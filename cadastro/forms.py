from django.forms import ModelForm
from .models import Pessoa

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

    def __init__(self, *args, **kwars):
        super().__init__(*args, **kwars)
        self.fields['cpf'].widget.attrs.update({'class':'mask-cpf'})
        self.fields['telefone'].widget.attrs.update({'class':'mask-telefone'})