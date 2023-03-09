"""
Módulo Collections -> Counter:

# Collections:
-> High-performance Container Datetypes.

# Counter:
-> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter
que é parecido com um dicionário, contendo como chave o elemento da lista passada
como parâmetro e como valor a quantidade de ocorrências desse elemento.

"""


# Exemplo 1:

# Realizando o import:
from collections import Counter

# Pode ser qualquer iterável:
lista = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 54, 324, 25, 63]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor
# a quantidade de ocorrências:

# Retorno:
# Counter({1: 12, 3: 9, 4: 9, 54: 1, 324: 1, 25: 1, 63: 1})


# Exemplo 2:

print(Counter('Geek University'))

# Para cada caractere, cria-se uma chave onde o valor é o número de ocorrências:
# Exemplo de retorno:
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})


# Exemplo 3:

texto = """A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue 
estabelecido na internet sob o princípio wiki. Tem como propósito fornecer um conteúdo livre, 
objetivo e verificável​​, que todos possam editar e melhorar. O projeto é definido pelos princípios 
fundadores e o conteúdo é disponibilizado sob a licença Creative Commons BY-SA e pode ser 
reutilizado sob a mesma licença, desde que respeitando os termos de uso. Todos podem publicar 
conteúdo on-line desde que criem uma conta e sigam as regras básicas, como verificabilidade ou notoriedade."""

# Transformando cada palavra em um elemento de uma lista:
palavras = texto.split()
# print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrência no texto:
print(res.most_common(5))