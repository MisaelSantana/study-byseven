"""
Block Try/Except:

# Utilizamos o blocl try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim
que o programa pare de funcionar e o usuário recebe mensagens de erro inesperadas.

# A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema


"""


# Exemplo 01: # -> Tratando um erro genérico:
try:
    geek()
except:
    print('Deu algum problema aqui!')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.
# OBS: Tratar erro de forma genérica, não é a melhor forma de tratamento de erros. O ideal
# é SEMPRE tratar de forma específica.


# Exemplo 02: # -> Tratando um erro específico:
try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 03: # -> Tratando um erro específico com detalhes do erro:
try:
    len(5)
except TypeError as erro:
    print(f'A aplicação gerou o seguinte erro: {erro}')


# Podemos efetuar diversos tratamentos de uma vez:
try:
    geek()
    len(5)
except TypeError as erro1:
    print(f'Deu TypeError: {erro1}')
except NameError as erro2:
    print(f'Deu NameError: {erro2}')
except ValueError as erro3:
    print(f'Deu ValueError: {erro3}')
except:
    print('Deu um erro diferente')


# Criando uma função com try/except:
# Caso gere um KeyError, ele irá retornar como 'None:
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None

dic = {'nome': 'Misael Santana'}

print(pega_valor(dic, 'mascicis'))
