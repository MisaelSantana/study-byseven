"""
Tipo String:

# Em Python, um dado é considerado do tipo string sempre que:
-> Estiver entre áspas simples:
-> 'uma string';
-> '12345';
-> 'a';
-> 'True';
-> '42.3'.

-> Estiver entre áspas duplas:
-> "uma string";
-> "12345";
-> "a";
-> "True";
-> "42.3".

-> Estiver entre áspas simples triplas:
-> '''uma string''';
-> '''12345''';
-> '''a''';
-> '''True''';
-> '''42.3'''.

-> Estiver entre áspas duplas triblas:
##### Não irei  dar exemplos para não quebrar o bloco de comentários #####
"""


# Exemplos:
nome = 'Geek University'
print(nome)
print(type(nome))


nome = "Geek University"
print(nome)
print(type(nome))


nome = '''Geek University'''
print(nome)
print(type(nome))


nome = """Geek University"""
print(nome)
print(type(nome))


nome = "Gina's Bar"
print(nome)
print(type(nome))


nome = 'Angelina \n Jolie'
print(nome)
print(type(nome))


# Transformar dados para letras maiúsculas:
nome = 'Geek University'
print(nome.upper())


## Transformar dados para letras minúsculas:
nome = 'Geek University'
print(nome.lower())


# Transforma em uma lista de strings:
nome = 'Geek University'
print(nome.split())


nome = 'Geek University'
print(nome[0:4])
print(nome[5:15])
print(nome.split()[0])
print(nome.split()[1])


# :(primeiro elemento):(ultimo elemento)-1(inverta)
# Sintaxe: print(variavel[::-1])
nome = 'Geek University'
print(nome[::-1])


# Substituição: replace()
nome = 'Geek University'
print(nome.replace('G', 'P'))


# Palíndromo
texto = 'socorram me subino onibus em marrocos'
print(texto)
print(texto[::-1])