"""
Escopo de variáveis

# Dois casos de escopo:
# [1] Variáveis globais:
-> Variáveis globais, são as variáveis que são reconhecidas em todo o programa.

# [2] Variáveis locais:
-> Variáveis locais são reconhecidas apenas no bloco onde foram declaradas,
ou seja, o seu escopo está limitado ao bloco onde foi declarada;

# Python é uma linguagem  de tipagem dinâmica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuímos um valor à mesma.
"""


# Para declarar variáveis em Python, fazemos:
nome_da_variavel = 'valor_da_variavel'
numero = 42
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))


# Declaração de variável local "novo":
numero = 42

if numero > 10:
    novo = numero + 10
    print(novo)
