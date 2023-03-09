"""
Módulo Collections -> Deque:

# Podemoss dizer que o deque é uma lista de alta performance.

"""


# Importando o Deque:
from collections import deque


# Criando Deques:
deq = deque('Geek')

print(deq)


# Adicionando elementos no deque:
deq.append('y')
print(deq)

# Adiciona no início (left = esquerda)
deq.appendleft('k')
print(deq)


# Remove e retorna o último elemento:
print(deq.pop())
print(deq)

# Remove e retorna o primeiro elemento:
print(deq.popleft())
print(deq)
