from django.shortcuts import render, HttpResponse, redirect
from .models import Investimento
from .forms import InvestimentoForm
# Create your views here.



def investimentos(request):
    dados = {'dados':Investimento.objects.all()} #variavel dados que recebe um dicionario retornando todos os resultados do banco de dados
    return render(request,'investimentos/investimentos.html',context=dados)

def detalhe(request, id_investimento):
    dados = { 'dados':Investimento.objects.get(pk=id_investimento) } #variavel dados que recebe um dicionario retornando o resultado onde tem primarykey (id) banco de dados
    return render(request,'investimentos/detalhe.html', dados)

def novo_investimento(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST) #variavel recebe investimentoform passado no forms.py  (requisição = POST)
        #valida se os dados já estao preenchidos
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos') #redireciona para investimentos
    else:
        investimento_form = InvestimentoForm() # variavel recebe investimentoform que completa os dados de acordo com a tabela
        formulario = {'formulario': investimento_form} #dicionario recebe formulario+investimento_form
        return render(request,'investimentos/novo_investimento.html', context=formulario)


def editar(request,id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)#variavel dados que recebe um dado retornando o resultado onde tem primarykey (id) banco de dados
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento) #se o metodo for GET investimentoform recebe a instancia definida em urls.py  path(.....'investimentos')
        return render(request,'investimentos/novo_investimento.html',{'formulario': formulario})
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento) #se for metodo POST recebe instancia investimento e verifica se é valido o formulario
        if formulario.is_valid():
            formulario.save() #se for valido salva no banco
            return redirect('investimentos')#redireciona para pagina de investimentos


def excluir(request,id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento) #variavel recebe o investimento com o id(primarykey)
    if request.method == 'POST':
        investimento.delete() #variavel obtida + comando pra exclusão no banco de dados
        return redirect('investimentos')#redireciona para investimentos
    return render (request,'investimentos/confirmar_exclusao.html',{'item': investimento})#confirma se realmente quer excluir