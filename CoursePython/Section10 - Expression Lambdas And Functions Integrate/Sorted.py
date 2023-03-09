"""
Sorted(ordenar):

# OBS:
-> Não confunda, apesar do nome, com a função sort() que já estudamos em listas;
-> O sort(), só funciona em listas.
-> O sorted(), SEMPRE retorna uma Lista com os elementos do iterável ordenados.

# Podemos utilizar o sorted() com qualquer iterável.

# Como o próprio nome diz, sorted() serve para ordenar
"""


# Exemplo:
numeros = [6, 1, 8, 3, 5, 2, 5]
print(numeros)

print(sorted(numeros))

print(numeros)


# Ordenando do maior para o menor:
numeros = [6, 1, 8, 3, 5, 2, 5]
# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True))


# Exemplo:
usuarios = [
    {'username': 'misael', 'tweets': ['Eu adoro bolos', 'Eu adoro Pizza']},
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro Pizza']},
    {'username': 'karla', 'tweets': ['Eu amo gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': [], "cor": "amarelo"},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': [], "cor": "Preto", "musica": "rock"}
]

print(usuarios)

# Ordenando por username -> Ordem Alfabética:
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando por número de tweets:
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))


# Exemplo:
musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},    
    {"titulo": "Dead Skin Mask", "tocou": 2},    
    {"titulo": "Back in Black", "tocou": 4},    
    {"titulo": "Too old to rock in roll, too ynoung to die", "tocou": 32}    
]

# Ordena da menos tocada para a mais tocada:
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada:
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
