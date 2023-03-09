"""
Estruturas condicionais:

# Condicionais
-> if;
-> else;
-> elif
"""

idade = int(input('Qual a sua idade?'))

if idade < 18:
    print('Menor de idade')
else:
    print('Maior de idade')


# Utilizando elif
idade = int(input('Qual a sua idade?'))

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')
