"""
Generators Expression:

# Em aulas anteriores nós estudamos:
-> List Comprehension;
-> Dictionary Comprehension;
-> Set Comprehension;

# Não vimos:
-> Tuple Comprehension, porque elas se chamam Generators.
"""


# Variável:
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

# Poderíamos ter feito utilizando Generators:
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension:
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator:
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)



# Importando lib:
# Qual é a utilidade de getsizeof()?
# -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro:
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupado em memória. Quanto maior a string,
# mais espaço ocupa.
print(getsizeof('Geek'))


# Exemplo:
from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dict_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator:
gen = getsizeof(x * 10 for x in range(1000))


print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')


# Eu posso interar no Generator Expression? Sim!
gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)
