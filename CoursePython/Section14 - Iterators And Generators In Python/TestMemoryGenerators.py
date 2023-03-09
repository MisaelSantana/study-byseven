"""
Teste de memória com Generators:

# 
"""


# Exemplo utilizando listas:
def fib_lista(max):
    nums = []
    a, b, = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Teste
for n in fib_lista(100000):
    print(n)


# Exemplo utilizando geradores:
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1

# Teste de execução:
for n in fib_gen(100000):
    print(n)
