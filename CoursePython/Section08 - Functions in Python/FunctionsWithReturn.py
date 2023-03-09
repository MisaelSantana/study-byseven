"""
Funções com retorno:

# OBS:
-> Em Python, quando uma função não retorna nenhum valor, o retorno é 'None';
-> Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return;
-> Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos 
passar a execução da função para outras funções.

# OBS: Palavra reservada 'return'
-> Ela finaliza a função, ou seja, ela sai da execução da função;
-> Podemos ter em uma função, diferentes returns;
-> Em uma função, podese-se retornar qualquer tipo de dado e até mesmo múltiplos valores;
"""


# Exemplo de função com e sem retorno: 
numeros = [1, 2, 3]

retorno_pop = numeros.pop()

print(f'Retorno de pop: {retorno_pop}')

retorno_print = print(numeros)  # Print não retorna nada 'None'.
print(f'Retorno de print: {retorno_print}')


# Exemplo de função:
def quadrado_de_7():
    print(7 * 7)

ret = quadrado_de_7()
print(ret)

# O print apenas imprime, mas ele não retorna nenhum valor.


# Refatorando a função para retornar o valor:
def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o valor da função:
ret = quadrado_de_7()
print(f'Retorno {ret}')

# Exemplos menores de retorno:
print(f'Retorno {quadrado_de_7()}')


# Refatprando a função quadrado de 7:
def quadrado_de_7():
    return 7 * 7

print(f'Retorno do quadrado de 7 é: {quadrado_de_7()}')


# Refatorando a primeira função 'diz_oi'
def diz_oi():
    return('Oi!')

print(f'Retorno de diz_oi: {diz_oi()}')


# Após o return, ele faz o retorno e para a execução, podemos testar execudando o exemplo abaixo:

# Exemplo 1:
def diz_oi():
    print('Estou sendo executado antes do return')
    return 'OI!!!!'
    print('Estou sendo executado após o return...')

print(diz_oi())

# Exemplo 2: Vários return:
def nova_funcao():
    varialvel = True
    if varialvel:
        return 4
    elif varialvel is None:
        return 3.2
    return 'b'

print(nova_funcao())

# Exemplo 3: Imprimindo vários valores em várias variáveis
def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)


# Vamos criar uma função para jogar a moeda:
from random import random

def joga_moeda():
    """Gera um número pseudo-randômico entre 0 e 1"""
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

# Refatorando:
def joga_moeda():
    """Gera um número pseudo-randômico entre 0 e 1"""
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())
