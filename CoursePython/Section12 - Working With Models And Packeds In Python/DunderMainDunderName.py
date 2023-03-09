"""
Dunder Name e Dunder Main:

# Dunder Name: __name__
# Dunder Main: __main__

# Dunder: Double Under.

# Em Python, são utilizados dunder para criar funções, atributos, propriedades 
e etc, utilizando Double Under para não gerar conflito com os nomes desses 
elementos na programação.

# Em Python, se executarmos um módulo Python diretamente na linha de comando,
internamente o Python atribuirá à variável __name__ o valor __main__ indicando
que este módulo é o módulo de execução principal.

# Main significa principal.
"""


# Ajustando o arquivo para não importar a execução:

from FunctionWithParameter import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6]))
