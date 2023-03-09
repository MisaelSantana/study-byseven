"""
Zip:

# zip():
-> Cria um iterável (Zip Object) que agrega elemento em cada um dos iteráveis passados como entrada em pares.
"""


# Exemplo:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla ou dicionário:
print(list(zip1))
print(tuple(zip1))
print(set(zip1))
print(dict(zip1))

# OBS: O zip() utiliza como parâmetro, o menor valor em iterável. Isso significa que se estiver
# trabalhando com iteráveis de tamanhos diferentes, irá para quando os elementos do menor
# iterável acabar:
lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)

print(list(zip1))


# Podemos utilizar diferentes iteráveis com zip:
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15,}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))


# Exemplos mais complexos:
prova1 = [80, 91, 78]
prova2 = [98, 81, 53]
alunos = ['Maria', 'Pedro', 'Carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)


# Podemos utilizar o map():
prova1 = [80, 91, 78]
prova2 = [98, 81, 53]
alunos = ['Maria', 'Pedro', 'Carla']


final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))
