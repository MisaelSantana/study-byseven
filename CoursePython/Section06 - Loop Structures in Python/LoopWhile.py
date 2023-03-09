"""
Loop While:


# Sintaxe:

while expressão_booleana:
    //execução do loop

# OBS: O bloco do while será repetido enquanto a expressão booleana for verdadeira.
    -> Expressão Booleana é toda expressão onde o resultado é verdadeiro ou falso.
"""


# Exemplo de while:
numero = 1

while numero < 10:
    print(numero)
    numero += 1

# Em um loop while, é importante que cuidemos do critério de parada


# Exemplo 02:
resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica?')
