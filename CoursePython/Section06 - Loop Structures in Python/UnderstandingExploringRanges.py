"""
Ranges:

-> Precisamos conhecer o loop for para usar os ranges.
-> Precisamos conhecer o range para trabalhar melhor com loops for.

# Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

# Formas gerais:


# Forma 01:

-> range(valor_de_parada)
# OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)


# Forma 02:

-> range(valor_de_inicio, valor_de_parada)
# OBS: valor_de_parada não inclusive (início específicado pelo usuário, e passo de 1 em 1)


# Forma 03:

-> range(valor_de_inicio, valor_de_parada, passo)
# OBS: valor_de_parada não inclusive (início específicado pelo usuário, e passo específicado pelo usuário)


# Forma 04:

-> range(valor_de_parada, valor_de_inicio, -passo)
# OBS: valor_de_parada não inclusive (início específicado pelo usuário, e passo específicado pelo usuário na ordem inversa)
"""

# Forma 01:
for num in range(11):
    print(num)


# Forma 02:
for num in range(0, 11):
    print(num)


# Forma 03:
for num in range(0, 11, 3):
    print(num)


# Forma 04:
for num in range(55, 0, -5):
    print(num)

lista = list(range(10))