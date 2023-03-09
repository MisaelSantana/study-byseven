"""
Reversed:

# OBS:
-> Não confunda com a função reverse() que estudamos nas listas;
-> A função reverse() só funciona em listas;

# A função reversed() funciona em qualquer iterável.
# Sua função é inverter o iterável.

# A função reversed() retorna um iterável chamado 'list_reverseiterator'.
"""


# Exemplos:
lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))


# Podemos converter o elemento retornado para uma lista, tupla ou conjunto:
print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista)))  # Em conjuntos, não definimos a ordem dos elementos.


# Podemos interar sobre reversed():
for letra in reversed('Geek University'):
    print(letra, end='')  # (end='') serve para retirar a quebra de linha.

print('\n')
# Podemos fazer o mesmo sem o uso do for:
print(''.join(list(reversed('Geek University'))))

# Invertendo com slice de strings:
print('Geek University'[::-1])


# Podemos também utilizar o reversed() para fazer um loop for reverso:
for n in reversed(range(0,11)):
    print(n)

# Apesar que também já vimos como fazer isso utilizando o próprio range():
for n in range(10, -1, -1):
    print(n)
