"""
Filter(Filtrar):

# filter():
-> Serve para filtrar dados de uma determinada coleção;

"""


# Exemplo:

valores = (1, 2, 3, 4, 5, 6)

media = (sum(valores) /len(valores))
print(media)


# Biblioteca para trabalhar com dados estatísticos:
import statistics

# Dados coletados de algum sensor:
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Média: {media}')


# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função ou iterável:

res = filter(lambda valor: valor > media, dados)
print(list(res))
print(type(res))

print(f'Novamente: {list(res)}')

# OBS: Assim como na função map(), após serem utilizados os dados de filter(), eles são excluídos da memória.


# Exemplo:
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(lambda pais: pais != '', paises)
res = filter(None, paises)
print(list(res))

"""
# A diferença entre map() e filter() é:

-> map(): Recebe dois parâmetros, uma função e um iterável, e retorna um objeto mapeando 
a função para cada elemento do iterável.
-> filter(): Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas
os elementos de acordo com a função.

# A grande diferença que temos é que a função filter(), retorna em formato boolean.
# No map(), retorna todos os valores.
"""


# Exemplo mais complexo:
usuarios = [
    {'username': 'Misael', 'tweets': ['Eu adoro bolos', 'Eu adoro Pizza']},
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro Pizza']},
    {'username': 'Karla', 'tweets': ['Eu amo gato']},
    {'username': 'Jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': []}
]

print(usuarios)

# Forma 01:
inativos1 = list(filter(lambda u: len(u['tweets']) == 0, usuarios))

# Forma 02:
inativos2 = list(filter(lambda u: not u['tweets'], usuarios))

print(inativos1)
print(inativos2)


# Combinar filter() e map():
nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres.
lista = list(map(lambda nome: f'Sua instrutura é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
