"""
Listas:

# Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com
a diferença de serem dinâmicos e também podermos colocar QUALQUER tipo de dado.

-> Dinâmico: Não possui tamanho fixo, ou seja, podemos criar a lista e simplesmente
ir adicionando elementos.
-> Valores: As listas não possuem tipo de dado fixo, ou seja, qualquer tipo de dado será aceito.

# As listas em python são representadas por colchetes: []

"""


type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')


# Checar se determinado valor está contido na lista:
num = 8

if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')


# Ordenação:
lista1.sort()
print(lista1)


# Contar o número de ocorrências de um valor em uma lista:
print(lista1.count(1))
print(lista2.count('e'))


# Adicionar elementos em listas:
# -> Para adicionar elementos em listas, utilizamos a função .append():
lista1.append(100)
print(lista1)
# -> OBS: Com append, nós só podemos adicionar 1 elemento por vez.


# Passando vários valores para adicionar na lista:
# Coloca a lista como elemento único, sublista.
lista1.append([100, 200, 300])
print(lista1)

if [100, 200, 300] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

# Adiciona os elementos de forma adicional a lista, sem colocar dentro de um array separado.
# extend só aceita vários valores
lista1.extend([123, 44, 67])
print(lista1)


# Podemos inserir um novo elemento na lista informando a posição do índice:
# Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
# Sintaxe:
# <variavel>.insert(<indice>, <valor>)

lista1.insert(2, 'Novo Valor')
print(lista1)


# Concatenação de listas:
lista6 = lista1 + lista2
print(lista6)

# ou, para não criar uma nova variável:
lista1.extend(lista2)
print(lista1)

# Aproveitando a variavel "lista1":
lista1 = lista1 + lista2
print(lista1)


# Retornando os valores em ordem reversa:
# Exemplo 01:
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

# Exemplo 02:
print(lista1[::-1]) # -> Exemplo utilizando slice;
print(lista2[::-1])


# Copiar uma lista:
lista6 = lista2.copy()
print(lista6)


# Validando o tamanho da lista utilizando o length:
print(len(lista1))


# Remover o último elemento de uma lista:
# O ".pop()" remove o ultimo elemento mas também o retorna na tela.
print(lista5)
lista5.pop()
print(lista5)

# Remover um elemento pelo índice:
# OBS: Os elementos á direita são deslocados para a esquerda.
lista5.pop(2)
print(lista5)


# Remover todos os elementos:
lista5.clear()
print(lista5)


# Repetir elementos em uma lista:
nova = [1, 2, 3]
print(nova)

nova *= 3
print(nova)


# Converter string para lista:

# Exemplo01:
# OBS: por padrão, o split separa os elementos da lista pelo espaço entre elas.
curso = 'Programação em Python: Essencial'
print(curso)

curso = curso.split()
print(curso)

# Exemplo02:
curso = 'Programação,em,Python:,Essencial'
print(curso)

curso = curso.split(',')
print(curso)


# Convertendo uma lista em uma string:
lista7 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista7)

# Abaixo estamos falando: Pega a lista7, coloca espaço entre cada elemento e transforma em uma string.
curso = ' '.join(lista7)
print(curso)

# Retirando o "$" e colocando um ' '(espaço) entre cada palavra:
curso = 'Programação$em$Python:$Essencial'
print(curso)
curso = curso.split('$')
print(curso)
curso = ' '.join(lista7)
print(curso)

# Colocando o "$" como entre cada palavra, como separador:
curso = '$'.join(lista7)
print(curso)


# Podemos realmente colocar qualquer tipo de data em uma lista, inclusive misturando esses dados:
lista8 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 473298432892]

print(lista8)
print(type(lista8))


# Iterando sobre lista:

# Exemplo01:
lista_iterando = [1, 2, 3]
soma = 0
lista_string = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
soma_string = ''

# Somando valores:
for elemento in lista_iterando:
    print(elemento)
    soma += elemento
print(soma)

# Concatenando strings:
for elemento in lista_string:
    print(elemento)
    soma_string += elemento
print(soma_string)

# Utilizando while:
# Ele cria uma lista vazia e armazena
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


# Criando listas utilizando variáveis:
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)


# Fazendo acesso aos elementos de forma indexada:
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Retornando de forma inversa indexada:
print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])


# For com arrays:
cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1


# Gerar indice em um for:
cores = ['verde', 'amarelo', 'azul', 'branco']

for indice, cor in enumerate(cores):
    print(indice, cor)


# Listas aceitam valores repitidos:
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)


# Outros métodos não tão importantes, mas também úteis:

# Encontrar o índice de um elemento na lista:
numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice da lista está o valor 6?
print(numeros.index(6))

# Em qual índice da lista está o valor 9?
print(numeros.index(9))

# Retorna apenas o PRIMEIRO indice:
print(numeros.index(5))


# Podemos fazer buscas dentro de um range, ou seja, qual indice começar a buscar:
print(numeros.index(5, 1))

# Podemos fazer buscas dentro de um range, inicio/fim:
print(numeros.index(8, 3, 6)) # Buscar o índice do valor 8, entre os índices 3 a 6.


# Revisão de sclicing:

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de lista com o parâmetro 'início':
lista = [1, 2, 3, 4]

print(lista[1:]) # Iniciando no índice 1 e pegando todos os elementos restantes:
print(lista[::]) # Pegando todos os elementos:
print(lista[:2]) # Começa em 0, pega até o índice 2:
print(lista[:4]) # Começa em 0, pega até o índice 4:
print(lista[1:3]) # Começa em 1, pega até o índice 3:
print(lista[1:-1]) # Começa em 1, pega até o índice 3:


# Trabalhando com slice de lista com o 'passo':

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista[:-1:2]) # Começa em 0, vai até o índice 8, pulando de 2 em 2:
print(lista[::2]) # Começa em 0, vai até o índice 11, pulando de 2 em 2:
print(lista[::3]) # Começa em 0, vai até o índice 11, pulando de 3 em 3:
print(lista[::-2]) # Começa no índice 11, e vai até o índice 0, pulando de 2 em 2 (mesma coisa só que na ordem inversa):


# Invertendo valores em uma lista, pelos indices:
nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)


# Invertendo valores em uma lista utilizando '.reverse()'
nomes = ['Geek', 'University']

nomes.reverse()
print(nomes)


# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho:

# * -> Se os valores forem todos inteiros ou reais(ponto flutuante)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum(lista))  # Soma da lista
print(max(lista))  # Valor máximo
print(min(lista))  # Valor mínimo
print(len(lista))  # Tamanho da lista


# Transformar lista em tupla:
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))


# Desempacotamento de lista:
lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS:
# -> A quantidade de elementos na lista e a quantidade de variáveis disponíveis 
# precisa ser exatamente igual, do contrário, teremos um valueError


# Copiando uma lista para outra: -> Deep Copy
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista)

# Copiando para uma nova lista:
nova_lista = lista.copy()
print(nova_lista)

# Adicionando um novo elemento na lista nova:
nova_lista.append(11)

# Imprimindo as listas:
print(lista)
print(nova_lista)


# OBS: Veja que ao utilizarmos 'lista.copy()', copiamos os dados da lista
# para uma nova lista, mas elas ficaram totalmente independentes, ou seja,
# modificando uma lista, não afeta a outra. Isso em python é chamado de
# Deep Copy (cópia profunda)


# Copiando uma lista para outra: -> Shallow Copy
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

nova_lista = lista
print(nova_lista)

nova_lista.append(11)

print(lista)
print(nova_lista)

# OBS: Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista,
# mas após realizar a modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy.
