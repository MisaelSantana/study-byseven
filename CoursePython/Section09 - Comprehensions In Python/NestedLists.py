"""
Listas Aninhadas (Nested Lists):

# Algumas linguagens de programação possuem uma estrutura de dados chamadas de array:
-> Unidimensionais (Array/Vetores);
-> Multidimensionais (Matrizes);

# Em Python nós temos as Listas:

numeros = [1, 2, 3, 4, 5]

"""


# Exemplos:

listas = [[1, 2 , 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3.

print(listas)
print(type(listas))


# Como fazemos para acessar os dados:
print(listas[0])

# Para acessar um elemento dentro dessa lista:
print(listas[0][1])


# Iterando com loops em uma lista aninhada:
for lista in listas:
    for num in lista:
        print(num)


# List Comprehension:
[[print(valor) for valor in lista] for lista in listas]
