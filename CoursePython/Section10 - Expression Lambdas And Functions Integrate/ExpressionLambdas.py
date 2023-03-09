"""
Utilizando Lambdas:

# Conhecidas por expressões Lambdas ou simplesmente Lambdas, são funções sem nome,
ou seja, funções anônimas.


# Função em Python:

def soma(a ,b):
    return a + b

# Sintaxe:
-> lambda <parametro1>, <parametro2>: <retorno>

"""


# Relembrando função em Python:
def funcao(x):
    return 3 * x + 1

print(funcao(4))


# Expressão Lambda:
lambda x: 3 * x + 1


# Como utilizar a expressão Lambda?
calc = lambda x: 3 * x + 1

print(calc(4))


# Podemos ter expressões Lambdas com mútiplas entradas:
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('Misael  ', ' SANTANA'))


# Exemplo: # -> Ordenando pelo sobrenome, usando expressão Lambdas:
autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


# Função quadrática:
# f(x) = a* x ** 2 + b * x + c

# Definindo a função:
def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a*x** 2 + b * x + c"""
    return lambda x: a*x** 2 + b * x + c

print(geradora_funcao_quadratica(2, 3, -5)(2))
