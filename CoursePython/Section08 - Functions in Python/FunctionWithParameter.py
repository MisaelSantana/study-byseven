"""
Funções com Parâmetro(de entrada):

# Funções que recebem dados para serem processados dentro da mesma.

# Se a gente pensar em um programa qualquer, temos:
-> Entrada;
-> Processamemto;
-> Saída;

# Se a gente pensar em uma função, já sabemos que temos que:
-> Não possuem entrada;
-> Não possuem saída;
-> Possuem entra mas não possuem saída;
-> Não possuem entrada, mas possuem saída;
-> Possuem entrada e saída;

"""


# Refatorando uma função:

# Exemplo 1:

def quadrado(numero):
    return numero * numero

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

# Exemplo 2:

def quadrado(numero):
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))


# Refatorando função 'cantar parabens'
def cantar_parabens(aniversariante):
    print('Parabens para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}')

cantar_parabens('Marcos')


# Funções podem ter 'n' parâmetros de entrada, ou seja, podemos receber como entrada
# em uma função, quantos parâmetros forem necessários. Eles são separados por vírgula.

# Exemplo 1:
def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

# Retornos:
print(soma( 2, 8))
print(multiplica( 5, 8))
print(outra(3, 2, 'Geek '))

# OBS: Se a gente informar um número errado de parâmetro ou argumentos, teremos um TypeError.


# Nomeando parâmetros:

def nome_completo(nome, sobrenome):
    return (f'Seu nome completo é: {nome} {sobrenome}')

print(nome_completo('Misael', 'Santana'))

"""
# Diferença entre parâmetros e argumentos:

-> Parâmetros: São variáveis declaradas na definição de uma função;
    Ex:
    def nome_completo(<parametro1>, <parametro2>):

-> Argumentos: São dados passados durante a execução de uma função:
    Ex:
    print(nome_completo('<argumento1>', '<argumento2>'))

# OBS:
-> A ordem os parâmetros IMPORTA.
"""


# Argumentos nomeados (keyword Arguments):
# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem:

nome = 'Thaynara'
sobrenome = 'Lemos Negri'

print(nome_completo(nome='Misael', sobrenome='Santana'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Santana', nome='Misael'))


# Erro comum na utilização do return:

def soma_impares(numeros):
    """Função utilizada para realizar a soma."""
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
        return total


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
