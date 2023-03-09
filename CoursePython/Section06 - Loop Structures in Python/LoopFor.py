"""
Loop for:

# Loop: Estruturas de repetição.
# For: Uma dessas estruturas.

# Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

# Exemplos  de iteráveis:
-> String:
    -> nome = 'Geek University'
-> Lista:
    -> lista = [1, 2, 3, 4, 5]
-> Range:
    -> numeros = (1, 10)
"""


nome = 'Geek University'
lista = [1, 2, 3, 4, 5]
numeros = (1, 10)

# Exemplo de for 1 (Iterando em uma string):
for letra in nome:
    print(letra)


# Exemplo de for 2 (Iterando em uma lista):
for numero in lista:
    print(numero)

"""
# Exemplo de for 3 (Iterando sobre uma range):
# range(valor_inicial, valor_final)
# OBS:
-> O valor final não é incluído(inclusive)
"""


for numero in range(1, 10):
    print(numero)


# Enumerate:
for indice, letra in enumerate(nome):
    print(nome[indice])


for indice, letra in enumerate(nome):
    print(letra)


# Quando não precisamos de um valor podemos descartá-lo usando o "_":
for _, letra in enumerate(nome):
    print(letra)


# Ele restorna os dois valores, o indice e a letra:
for valor in enumerate(nome):
    print(valor)


# Retorna apenas os valores, sem os indices:
for valor in enumerate(nome):
    print(valor[1])


# Loop for
quantidade = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, quantidade):
    num = int(input(f'Imprimindo {n}/{quantidade} valor: '))
    soma = soma + num
print(f'A soma é {soma}')


# Segundo exemplo de loop for:
nome = 'Geek University'

for letra in nome:
    print(letra, end='')


# Unicode:
# Original: U+1F60D
# Modificado : U0001F60D

for num in range(1, 11):
    print(f'\U0001F60D' * num)
