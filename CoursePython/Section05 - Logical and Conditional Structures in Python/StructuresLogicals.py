"""
Estruturas Lógicas:
# and (e);
# or (ou);
# not (não);
# is (é).

# Operadores unários:
-> not

# Operadores binários:
-> and;
-> or;
-> is.

# Para o "and":
-> Ambos os valores precisam ser "True".

# Para o "or":
-> Apenas um dos valores precisa ser "True".

# Para o "not":
-> O valor do booleano é invertido. Se for "True" vira "False", se for "False" vira "True".

#Para o "is":
-> O valor é comparado com um segundo valor.
"""


# Exemplo "and":
ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')


# Exemplo "not":
ativo = True
logado = False

if not ativo:
    print('Você precisa ativar sua conta. Por favor, verifique seu e-mail!')
else:
    print('Bem vindo ao sistema')


# Exemplo somente com if:
ativo = True
logado = False

if ativo:
    print('Você precisa ativar sua conta. Por favor, verifique seu e-mail!')
else:
    print('Bem vindo ao sistema')


# Exemplo "is":
ativo = True
logado = False

if ativo is False:
    print('Você precisa ativar sua conta. Por favor, verifique seu e-mail!')
else:
    print('Bem vindo ao sistema')
# ativo é True?
print(ativo is True)