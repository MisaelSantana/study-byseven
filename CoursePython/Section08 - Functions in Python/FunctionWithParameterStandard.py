"""
Funções com parâmetros padrão (Default Parameters):

# Funções onde a passagem de parâmetro seja opcional.
"""



# Print: -> # Exemplo de função onde a passagem de parâmetro seja opcional:
print('Geek University')

print()


# Exemplo de função onde a passagem de parâmetro seja obrigatória(TypeError):
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado())


# Caso eu não informe a potência, ela recebe um valor padrão para elevar ao quadrado(se torna opcional):
def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2, 3)) # 2 * 2 * 2 = 8
print(exponencial(3))


# OBS: Em funções Python, os parâmetros com valores default(padrão) DEVEM sempre estar ao final da declaração:

# Errado:
#def teste(num=2, potencia):
#    return num ** potencia

#print(teste(6))

# Certo:
def teste(potencia, num=2):
    return num ** potencia

print(teste(6))


# Outros exemplos:
def soma(num1, num2):
    return num1 + num2

print(soma(2, 10))
print(soma(2))      # TypeError
print(soma())       # TypeError


# Exemplo mais complexo:
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return('Bem-Vindo instrutor Geek!')
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return(f'Olá {nome}')

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Ozzy'))


"""
# Porque utilizar parâmetros com valor default?

-> Nos permite ser mais flexíveis nas funções;
-> Evita erros com parâmetros incorretos;
-> Nos permite trabalhar com exemplos mais legíveis de código;
"""


"""
# Quais os tipos de dados podemos utilizar como valores detaul para parâmetros?

# Qualquer tipo de dado:
-> Números;
-> Strings;
-> Floats;
-> Booleanos;
-> Listas;
-> Dicionários;
-> Funções;
-> Etc...
"""


# Exemplo de funções como parâmetro:

def soma(num1, num2):
    return(num1 + num2)

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return(num1 - num2)

print(mat(2, 3))
print(mat(2, 3, subtracao))


"""
# Escopo -> Evitar problemas e confusões:

-> Variáveis globais:
-> Variáveis locais:
"""

# Variável global:
instrutor = 'Geek'

def diz_oi():
    instrutor = Python  # Variável local:
    return(f'Oi {instrutor}')

print(diz_oi())

# OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.


# Tentar chamar uma variável local fora do escopo local:
def diz_oi():
    prof = 'Geek'
    return(f'Olá {prof}')

print(diz_oi())

# print(prof) # NameError


# ATENÇÃO com variáveis globais(se puder evitar, evite!):
total = 0

def incrementa():
    total = total +1    # UnboundLocalError -> A variável local está sendo utilizada sem ter sido inicializada.
    return total

print(incrementa())

# Corrigindo:
total = 0

def incrementa():
    global total    # Avisando que queremos utilizar a variável global.
    total = total +1    # UnboundLocalError -> A variável local está sendo utilizada sem ter sido inicializada.
    return total

print(incrementa())


# Podemos ter funções que são declaradas dentro de funções e também tem uma forma especial de escopo de variável:

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
