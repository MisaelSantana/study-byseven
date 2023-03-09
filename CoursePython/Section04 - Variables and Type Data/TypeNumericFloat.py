"""
Tipo Float:

# Tipo real/decimal;
# Casas decimais;
OBS: O separador de casas decimais na programação é o ponto e não a vírgula.
"""


# Errado do ponto de vista de valores Float, mas gera uma tupla:
valor_tupla = 1, 44
print(f'{valor_tupla}')
print(type(valor_tupla))


# Certo do ponto de vista do Float:
valor_float = 1.44
print(f'{valor_float}')
print(type(valor_float))


# É possível fazer dupla atribuição:
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))


# Podemos converter um Float para um int:
"""
# OBS:
-> Ao converter valores float para inteiros, nós perdemos precisão
do resultado desses valores
"""
resultado = int(valor_float)
print(resultado)
print(type(resultado))


# Podemos trabalhar com números complexos:
variavel_complexa = 5j
print(variavel_complexa)
print(type(variavel_complexa))