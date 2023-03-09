"""
Entendendo o *args:

# O *args é um parâmetro, como outro qualquer. Isso signica que você poderá chamar 
de qualquer coisa, desde que começe com asterisco.

# Exemplo:
-> *xis

# Mas por convenção, utiliamos *args para definí-lo

# Mas o que é o *args?
-> O parâmetro *args em uma função, coloca os valores extras informados como entrada
em uma tupla. Então desde já, lembre-se, que tuplas são imutáveis.

"""


# Exemplos:

def soma_todos_numeros(num1=0, num2=0, num3=0):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 7, 9))


# Entendendo o *args:
def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(10))
print(soma_todos_numeros(10, 20))
print(soma_todos_numeros(13, 123, 14))
print(soma_todos_numeros(1, 3, 4, 5, 6,))
print(soma_todos_numeros(12.5, 76.4))


# Outro exemplo de utilização de *args:
def verifica_info(*args):
    """Função que verifica se Geek University está contido"""
    if 'Geek' in args and 'University' in args:
        return('Bem-vindo Geek!')
    return('Eu não tenho certeza de quem você é...')

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.14))


# Desempacotador:
def soma_todos_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7]

print(soma_todos_numeros(*numeros))

# OBS: O asterosco serve para que informemos ao Python que estamos passado 
# como argumento uma coleção de dados. Desta forma ele saberá que precisará
# desempacotar esses dados.