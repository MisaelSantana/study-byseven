"""
Len, Abs, sum, Round:

# Len:
-> len(): Retorna o tamanho (ou seja, o número de itens) de um iterável.

# Abs:
-> abs(): Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

# Sum:
-> sum(): Recebe como parâmetro um iterável inteiro ou real. De forma básica seria o seu valor real
sem o sinal e retorna a soma dos elementos, incluindo o valor inicial.

# Round:
-> round() -> Retorna o número arredondado para n digito de precisão após a casa decimal.
Se a precisão não for informada, retorna o inteiro mais próximo da entrada.
"""


# Revisão de len():
print(len('Geek University'))
print(len([1, 2, 3, 4, 5]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2 , 3, 4, 5}))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,}))
print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:

# Dunder len:
print('Misael Santana'.__len__())


# Exemplo de uso Abs:
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))


# Exemplo de Sum:
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))

print(sum([1.24, 2.34, 3.22, 4.34, 5.2342]))

print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))


# Exemplo de Round:
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.213132123121213, 2))
print(round(1.2199999999999, 2))