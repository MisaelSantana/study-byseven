"""
Funções de Maior Grandeza:

# Higher Order Functions(HOF):
-> Quando uma linguagem de programação suporta/permite esse conseito HOF, indica
que podemos ter funções que retornam outras funções como resultado ou mesmo que
podemos passar funções como argumentos para outras funções, e até mesmo criar 
variáveis do tipo de funções nos nossos programas.

# OBS:
-> Na seção de funções, nós utilizamos isso.

# Em Python, as funções são Cidadões de Primeira Classe, First Class Citizen.
"""


# Exemplo - Definindo as funções:
def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções:
print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))


# Nested Functions - Funções Aninhadas:
from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E aí ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa

# Teste:
print(cumprimento('Misael'))
print(cumprimento('Thaynara'))


# Retornando funções de outras funções:
from random import choice

def faz_me_rir():
    def rir():
        return choice(('kkkkkkkkkkk', 'hsuahsuahsuuhass', 'kakakakkakkak'))
    return rir()

# Teste:
rindo = faz_me_rir()
print(rindo())
print(rindo())
print(rindo())


# Inner Functions(Funções Internas), podem acessar o escopo de funções externas:
from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahaha', 'kkkkkkkkkk', 'kaskakksaksa'))
        return(f'{risada} {pessoa}')
    return dando_risada


# Teste:
rindo = faz_me_rir_novamente('Fernanda')
print(rindo())
print(rindo())
print(rindo())
