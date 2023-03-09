"""
Módulo Collections -> Named Tuple:

# Recapitulando Tupla:

# Sintaxe:
tupla = (1, 2, 3)
print(tupla[1])


# Named Tuple: São tuplas, diferenciadas, onde, especificamos um nome para a mesma
e também parãmetros.
"""


# Importação do Named Tuple
from collections import namedtuple


# Precisamos definir o nome e parâmetros:

# Forma 1: -> # Declaração Named Tuple:
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2: -> # Declaração Named Tuple:
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3: -> # Declaração Named Tuple:
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])


# Uso:
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

# Acessando os dados:

# Forma 1:
print(ray)      # All Tuple;
print(ray[0])   # Idade;
print(ray[1])   # Raça;
print(ray[2])   # Nome;

# Forma 2:
print(ray.idade)    # Idade;
print(ray.raca)     # Raça;
print(ray.nome)     # Nome;

# Qual é o índice?:
print(ray.index('Chow-Chow'))

# Quantas ocorrências tem determinado valor:
print(ray.count('Chow-Chow'))
