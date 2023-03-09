"""
Entendendo Iterators e Iterables:

# Iterators:
-> É um objeto que pode ser iterado.
-> Um objeto que retorna um dado sendo um elemento por vez, quando uma 
função 'next()' é chamada.

# Iterables:
-> Um objeto que irá retornar um iterator a função 'iter()' for chamada.

"""


# Exemplo:
nome = 'Misael'
numeros = [1, 2, 3, 4, 5, 6]

print(next(nome))  # TypeError: 'str' object is not an iterator

# Transformando em iterator:
nome = 'Misael'
numeros = [1, 2, 3, 4, 5, 6]

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
