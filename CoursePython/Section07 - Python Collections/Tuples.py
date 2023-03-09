"""
Tuplas(tuple):

# Tuplas são bastante parecidas com listas.

# Existem basicamente duas diferenças:
-> As tuplas são representadas por parênteses: ()
-> As tuplas são imutáveis. Isso significa que ao criar uma tupla ela não muda.
Toda operação em uma tupla gera uma nova tupla.

"""


# CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))


# CUIDADO 2: Tuplas com 1 elemento:

tupla3 = (4)    # Isso NÃO é uma tupla!
print(tupla3)

print(type(tupla3))

tupla4 = (4,)   # Isso é uma tupla!
print(tupla4)

print(type(tupla4))

tupla5 = 5,   # Isso é uma tupla!
print(tupla5)

print(type(tupla5))

# CONCLUSÃO: Tuplas são definidas pela VÍRGULA e não pelo uso de parênteses.


# Gerando uma tupla com range:
tupla = tuple(range(11))

print(tupla)
print(type(tupla))


# Desempacotamento de tupla
tupla = ('Geek', 'University')

nome1, nome2 = tupla

print(nome1)
print(nome2)


# Métodos para adição, remoção de elementos nas tuplas não existem, dado ao fato das tuplas serem imutáveis.


# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho:
# * -> Se os valores forem todos inteiros ou reais
# Tamanho: Não importa qual o tipo de valor, pois o que ele pega são os campos da tupla.

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))


# Concatenação de tuplas:
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)

# Fazendo a junção de 2 tuplas:
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

tupla3 = tupla1 + tupla2
print(tupla3)

# Fazendo a junção e alterando os valores(sobrescrever) da tupla1:
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

tupla1 = tupla1 + tupla2
print(tupla1)


# Validar se determinado elemento está contido na tupla:
tupla = (1, 2 ,3)

print(3 in tupla) # Retorna True ou False


# Iterando sobre uma tupla:
tupla = (1, 2 ,3)

for i in tupla:
    print(i)

for indice, valor in enumerate(tupla):
    print(indice, valor)


# Contando elementos dentro de uma tupla:
tupla = ('a', 'b', 'c', 'd', 'a', 'c')

print(tupla.count('a'))
print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))


# Dicas na utilização de tuplas:
# -> Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção.

# Exemplo 1:
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

# Acesso a elementos de uma tupla também é semelhante a de uma lista:
print(meses[10]) # Novembro

# Iterar com While:
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual índice o elemento está na tupla:
print(meses.index('junho'))
print(meses.index('junho', 4)) # Validar a partir do indice 4

# OBS: Caso o elemento não exista, será gerado um erro, pois não será possível acessar ao índice.


# Slicing:
# tupla[<inicio>:<fim>:<passo]
print(meses[5])     # Pega o índice 5.
print(meses[5:9])   # Pega do índice 5 até 9.
print(meses[5:9:2]) # Pega do índice 5 até 9, de 2 em 2.
print(meses[::2])   # Do início ao fim, de 2 em 2.


# Porque utilizar tuplas?
# -> Tuplas são mais rápidas do que listas(performance).
# -> Tuplas deixam seu código mais seguro*.

# * Isso porque trabalhar com elementos imutáveis traz mais segurança para o código.


# Copiando uma tupla para a outra:
tupla = (1, 2, 3)
print(tupla)

nova = tupla    # Na tupla não temos o problema de Shallow Copy(alterar os dados copiados tanto na cópia como no original)

print(tupla)
print(nova)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)
