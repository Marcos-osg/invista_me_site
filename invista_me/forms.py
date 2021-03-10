from django.forms import ModelForm
from .models import Investimento #importa a classe investimento onde tem a tabela

class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento  #define que o model é a classe investimento
        fields = '__all__'