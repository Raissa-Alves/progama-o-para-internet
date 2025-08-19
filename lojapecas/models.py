from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_cpf_cnpj.fields import CPFField, CNPJField


class Clientes(models.Model):
  nome = models.CharField(max_length=100)
  cpf = models.CPFField(masked=True)
  telefone = PhoneNumberField()
  email = models.CharField(max_length=200)
  endereco = models.CharField(max_length=200)

class Funcionarios(models.Model):
  nome = models.CharField(max_length=100)
  cpf = CPFField(masked=True)
  email = models.CharField(max_length=200)
  cargo = models.CharField(max_length=50)
  data_admissao = models.DateField(auto_now=True)

class Fornecedores(models.Model):
  empresa = models.CharField(max_length=100)
  cnpj = CNPJField(masked=True)
  endereco = models.CharField(max_length=200)
  telefone = PhoneNumberField()
  email = models.CharField(max_length=200)
  gerente = models.CharField(max_length=100)

class Pecas(models.Model):
  nome = models.CharField(max_length = 100)
  codigo_barras = models.CharField(max_length=200)
  fabricante = models.CharField(max_length=70)
  preco = models.FloatField()
  Q_estoque = models.PositiveIntegerField()
  fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE)

class Vendas(models.Model):
     data_venda = models.DateTimeField(auto_now_add=True)
     total = models.FloatField()
     cliente = models.ForeignKey(Clientes, on_delete=models.SET_NULL, null=True)
     funcionario = models.ForeignKey(Funcionarios, on_delete=models.SET_NULL, null=True)
     pecas = models.ManyToManyField(Pecas)
