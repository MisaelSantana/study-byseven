"""
Tipo Booleano:

# Álgebra Booleana, criada por George Boole.

# 2 Constantes, Verdadeiro ou Falso:
-> True = Verdadeiro;
-> False = Falso;

OBS:
# Sempre com a inicial maiúscula.
# Errado:
-> true;
-> false;

# Certo:
-> True;
-> False;
"""

"""
Operações básicas:

# Negação (not):
-> Fazendo a negação, se o valor booleano for verdadeiro, o resultado será falso;
-> Se for falso, o resultado será verdadeiro. Ou seja, sempre o contrário.
"""


ativo = True
print(ativo)
print(not(ativo))


"""
Operações básicas:

# Ou (or):
-> É uma operação binária, ou seja, depende de dois valores;

-> Ou um ou outro, deve ser verdadeiro:
-> True or True = True;
-> True or False = True;
-> False or True = True;
-> False or False = False.
"""


logado = False
print(ativo or logado)


"""
Operações básicas:

# E (and):
-> Também é uma operação binária, sou seja, depende de dois valores;

-> Ambos os valores devem ser verdadeiro:
-> True or True = True;
-> True or False = False;
-> False or True = False;
-> False or False = False.
"""