"""
Any e All:

# All:
-> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

# Any:
-> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False.

"""


# Exemplo all()
print(all([0, 1, 2, 3, 4])) # Todos os números são verdadeiros? False

print(all([1, 2, 3, 4])) # Todos os números são verdadeiros? True

print(all([])) # Todos os números são verdadeiros? True


nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))


# Exemplo de Any:

print(any([0, 1, 2, 3, 4])) # Todos os números são verdadeiros? True

print(any([1, 2, 3, 4])) # Todos os números são verdadeiros? True

print(any([])) # Todos os números são verdadeiros? False



# Exemplo Any:
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristinaa', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))
