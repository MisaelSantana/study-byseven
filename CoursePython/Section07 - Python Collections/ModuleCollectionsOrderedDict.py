"""
Módulo Collections -> Ordered Dict:


"""


from collections import OrderedDict


# Em um dicionário, a ordem de inserção dos elementos não é garantida. 
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(dicionario)


# Utilizando Dict:
dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'Chave = {chave}: Valor = {valor}')


# Entendendo a diferença entre Dict e Ordered Dict:

# Dicionários comuns:

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)   # True -> Já que a ordem dos elementos não importa para o dicionário.

# Ordered Dict:
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # False -> Para serem iguais a ordem precisar ser a mesma.
