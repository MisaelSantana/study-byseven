"""
Teste de velocidade com expressões geradoras:

# 
"""


# Generators (geradores):
def nums():
    for num in range (1, 10):
        yield num

ge1 = nums()
print(ge1)  # Generator


# Generator Expression (Expressão Geradora):
ge2 = (num for num in range(1, 10))

print(ge2)


# Realizando teste de velocidade:
import time

# Generator Expression:
gen_inicio = time.time()
print(sum(num for num in range(100000000)))  # 100 milhões
gen_tempo = time.time() - gen_inicio

# List Comprehension:
list_inicio = time.time()
print(sum([num for num in range(100000000)]))  # 100 milhões
list_tempo = time.time() - list_inicio

# Imprimindo:
print(f'Generator Expression levou {gen_tempo}')
print(f'List Expression levou {list_tempo}')
