"""
Set Comprehension:

-> Lista = [1, 2, 3, 4, 5]
-> Set = {1, 2, 3, 4, 5}
"""


# Exemplo 01:
numeros = {num for num in range(1, 7)}
print(numeros)

# Exemplo 02:
numeros = {x ** 2 for x in range(10)}
print(numeros)

# DESAFIO!: Faça uma alteração na estrutura acima para gerar um dicionário ao invés de set:
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Exemplo 03:
letras = {letra for letra in 'Geek University'}
print(letras)
