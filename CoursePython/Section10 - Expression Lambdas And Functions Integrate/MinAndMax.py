"""
Min e Max:

# max():
-> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos;

# min():
-> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos;

"""


# Exemplo de uso simples:

# Lista:
lista = [32, 8, 4, 99, 34, 129]

print(max(lista))  # 129
print(min(lista))  # 4

# Tupla:
tupla = (32, 8, 4, 99, 34, 129)

print(max(tupla))  # 129
print(min(tupla))  # 4

# Conjunto:
set = {32, 8, 4, 99, 34, 129}

print(max(set))  # 129
print(min(set))  # 4

# Dicionário:
dict = {'a': 32, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}

print(max(dict))  # f
print(min(dict))  # a
# Imprimindo os valores:
print(max(dict.values()))  # 129
print(min(dict.values()))  # 4


# Faça um programa que receba dois valores do usuário e mostre o maior:
val1= int(input('Informe o primeiro valor'))
val2= int(input('Informe o segundo valor'))

print(max(val1, val2))


# Exemplo de uso do min():

# Faça um programa que receba dois valores do usuário e mostre o menor valor:
val1= int(input('Informe o primeiro valor'))
val2= int(input('Informe o segundo valor'))

print(min(val1, val2))


# Outros exemplos:
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander',]

print(max(nomes))  # Tim
print(min(nomes))  # Arya

print(max(nomes, key=lambda nome: len(nome)))  # Ollivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim


# Exemplo:
musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},    
    {"titulo": "Dead Skin Mask", "tocou": 2},    
    {"titulo": "Back in Black", "tocou": 4},    
    {"titulo": "Too old to rock in roll, too ynoung to die", "tocou": 32}    
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Imprimar apenas o nome:
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# Encontrar a música mais tocada e menos tocada sem utilizar o min(), max() e lambda:
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])


min = 0
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])
