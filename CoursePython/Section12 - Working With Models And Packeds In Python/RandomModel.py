"""
Módulo Random e o que são módulos:

# Em Python, módulos são outros arquivos Python:

# Módulo Random:
-> Possui várias funções para geração de números pseudo-aleatório.

"""


# OBS: Existem duas formas de se utilizar um módulo ou função deste.

# Forma 01: # -> Importanto todo o módulo(Não Recomendado).
import random

"""
# OBS:

-> Ao realizar um import de todo o módulo, todas as funções, atributos, 
classes e propriedades que estiverem dentro do módulo, ficarão 
disponíveis (ficará em memória).

-> Caso você saiba quais funções você precisa utilizar deste módulo, 
estão não seria a forma ideal de utilização. Nós veremos uma for 
melhor na 'Forma 02'
"""


# Forma 02:
from random import random


# Exemplo de utilização:
for i in range(10):
    print(random())


# uniform(): # -> Gerar um número pseudo-aleatório entre valores estabelecidos:

# Importar uniform():
from random import uniform

for i in range(10):
    print(uniform(3, 7))  # 7 não é incluído.


# randint(): # -> Gera valores inteiros, pseudo-aleatórios entre os valores estabelecidos:

# Gerador de apostas para a Mega-Sena:
from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')  # Começa em 1 e vai até 60.


# choice(): # -> Mostra um valor aleatório entre um iterável:
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))


# shuffle(): # -> Tem a função de embaralhar dados:
from random import shuffle

cartas = ['k', 'q', 'j',]

print(cartas)
shuffle(cartas)
print(cartas)

print(cartas.pop())
