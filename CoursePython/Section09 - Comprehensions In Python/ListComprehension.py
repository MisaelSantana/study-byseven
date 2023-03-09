"""
List Comprehension:

# Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir
de outro iterável

# Sintaxe da List Comprehension:

[ dado for dado in iterável ]

"""


# Exemplos:

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

"""
# Para enteder melhor o que está acontecendo, devemos dividir a expressão em duas partes:

-> Primeira parte: for <variavel> in <iteravel>
-> Segunda parte: <variavel> * 10

"""


# Quadrado:

res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)


# List Comprehension versos Loop:

# Loop:
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)


# List Comprehension:
numeros = [1, 2, 3, 4, 5]

print([numero * 2 for numero in numeros])


"""
List Comprehension: Parte 02:

# Nós podemos adicionar estruturas condicionais lógicas as nossas List Comprehension.
"""


# Exemplo:

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0 ]
impares = [numero for numero in numeros if numero % 2 == 0 ]

print(pares)
print(impares)

# Refatorar:
numeros = [1, 2, 3, 4, 5, 6]

# Qualquer número par módulo de 2 é 0 e 0 em Python é False. Not False = True;
pares = [numero for numero in numeros if not numero % 2]

# Qualquer número impar módulo de 2 é 1 e 1 em Python é True;
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)
