"""
Trabalhando com Módulos Builtin:

# Módulos Builtin são módulos integrados, que já vem instalados no Python.

------------------------
|Python/Módulos builtin|
------------------------


"""


# Utilizando alias(apelidos) para módulos/funções:
import random as rdm

print(rdm.random())


# Podemos importar todas as funções de um módulo, utilizando o '*':
from random import *

print(random())


# Utilizando alias(apelidos) para módulos/funções:
from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())


# Fazendo vários imports:
from random import random, randint, shuffle, choice


# Utilizando tuple para colocar múltiplos imports de um mesmo módulo:
from random import (
    random, 
    randint, 
    shuffle, 
    choice
)

print(random())
print(randint(3, 7))
lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)
print(choice('Univerity'))
