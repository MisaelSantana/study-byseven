"""
Try, Except, Else, Finally:

# Dica de quando e onde tratar código:
-> TODA entrada deve ser tratada!

# OBS:
-> A função do usuário é DESTRUIR seu sistema.
"""


# Exemplo:
num = 0

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')    
print(f'Você digitou {num}')


# Exemplo utilizando else:
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')    
else:
    print(f'Você digitou {num}')

# Else é executado somente se não ocorrer o erro.


# Exemplo utilizando Finally:
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor valido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é SEMPRE executado, independente se houve exceção ou não.
# O finally, geralmente, é utilizado para fechar os deslocar recursos.


# Exemplo mais complexo:
# Você é responsável pelas entradas das suas funções. Então, trate-as!

# Tratamento específico
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return('Valor Incorreto')
    except ZeroDivisionError:
        return('Não é possível realizar uma divisão por zero')

num1 = input('Informe o primeiro número')
num2 = input('Informe o segundo número')

print(dividir(num1, num2))

# Tratamento semi-genérico
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return('Valor Incorreto')
    except (ValueError, ZeroDivisionError) as erro:
        return(f'Ocorreu um problema: {erro}')

num1 = input('Informe o primeiro número')
num2 = input('Informe o segundo número')

print(dividir(num1, num2))
