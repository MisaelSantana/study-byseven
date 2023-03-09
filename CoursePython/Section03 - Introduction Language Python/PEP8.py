"""
PEP -> Python Enhancement Proposals / Propostas de Aprimoramento do Python;
Segue link para a documentação PEP Index 'https://www.python.org/dev/peps/';

-> Poema python
import this;

A ideia de PEP8 é que possamos escrever códigos python de forma organizada,
respeitando a ideia de clean code;
"""

# Utilize Camel Case(primeira letra maiúscula) para nomes de classes;
class Calculadora:
    pass


class CalculadoraCientifica:
    pass


# Utilize nomes em minúsculo, separados por underline para funções ou variáveis;
def soma():
    pass


def soma_dois():
    pass


numero = 4
numero_impar = 5


# Utilize 4 espaços para identação;
if 'a' in 'banana':
    print('tem')


# Linha em branco:
# -> Separar funções e definições de classe com duas linhas em branco;

# -> Métodos dentro de uma classe devem ser separados com uma única linha em branco;
class Classe:
    pass


class OutraClasse:
    pass


# Imports devem ser sempre feitos em linhas separadas:

# -> Import Errado;
import sys, os


# -> Import Certo;
import sys
import os


# -> Não há problemas em utilizar:
from types import StrinType, ListType


# -> Caso tenha muitos imports do mesmo pacote, recomenda-se  fazer:
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)


# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer
# comentários ou docstrings e antes de constantes ou variáveis globais;


# Espaços em expressões e instruções;

# -> Não faça:
funcao( algo[ 1 ], { outro: 2 } )


# -> Faça:
funcao(algo[1], {outro: 2})


# -> Não faça:
algo (1)


# -> Faça:
algo(1)


# -> Não faça:
dict ['chave'] = lista [indice]


# -> Faça:
dict['chave'] = lista[indice]


# -> Não faça:
x              = 1
y              = 3
variavel_longa = 5


# -> Faça:
x = 1
y = 3
variavel_longa = 5


# Termine sempre uma instrução com uma nova linha;
class NomeDaClasse():
    pass
