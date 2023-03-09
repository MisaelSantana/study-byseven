"""
**Kwargs:

# Poderiamos chamar este parâmetro de **xis, mas por convenção chamamos de **kwargs;

# Este é só um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla,
o **kwargs exige que utilizamos parâmetros nomeados, e transforma esses parâmetros extras
em um dicionário.

"""


# Exemplo simples:

def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco',)


# Exemplo 2:
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco',)

# OBS: Os parâmetros *args e **kwargs não são obrigatórios:

cores_favoritas()
cores_favoritas(Misael='preto')


# Exemplo mais complexo:

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return('Você recebeu um cumprimento Pythônico Geek')
    elif 'geek' in kwargs:
        return(f"{kwargs['geek']} Geek")
    return('Não tenho certeza quem você é...')

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='Especial'))

"""
# Nas nossas funções, podemos ter:

-> Parâmetros obrigatórios;
-> *args;
-> Parâmetros default (Não obrigatórios);
-> **kwargs;
"""


# Exemplo de função:

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(f'{args}')
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(f'{kwargs}')

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 6, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 4, 5, 6, java=False, python=True)


# Entenda porque é importante manter a ordem dos parâmetros na declaração:

def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo= 'Instrutor'))


# Desempacotamento com **kwargs:

def mostrar_nomes(**kwargs):
    return(f"{kwargs['nome']} {kwargs['sobrenome']}")

nomes = {'nome': 'Misael', 'sobrenome': 'Santana'}

print(mostrar_nomes(**nomes))


# Soma:

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# OBS:
# -> Os nomes da chave em um dicionário, devem ser os mesmos dos parâmetros da função.
