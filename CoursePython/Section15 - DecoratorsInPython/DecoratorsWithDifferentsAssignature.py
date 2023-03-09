"""
Decorators com diferentes assinaturas:

"""


# Utilizando com a Decorator Pattern:
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return(funcao(*args, **kwargs).upper())
    return aumentar

@gritar
def saudacao(nome):
    return(f'Olá, eu sou {nome}')


@gritar
def pedido(principal, acompanhamento):
    return(f'Olá, eu gostaria de comer {principal} acompanhado de {acompanhamento}, por favor!')

print(saudacao('Misael'))

print(pedido('Macarrão', 'Carne Moída'))


# Decorator com argumentos:
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return(f'Valor incorreto! Primeiro argumento precisa ser {valor}')
            return(funcao(*args, **kwargs))
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args, **kwargs):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

# Teste de execução:
print(soma_dez(10, 12))
print(soma_dez(1, 21))

print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('sanduiche', 'pizza'))
