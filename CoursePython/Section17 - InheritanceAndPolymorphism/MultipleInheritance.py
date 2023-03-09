"""
POO - Herança Múltipla:

# Herança Múltipla nada mais é do que a possibilidade de uma classe herdar
  de múltiplas classes, fazendo com que a classe filha herde todos os atributos
  e métodos de todas as classes herdades.


# A herança múltipla pode ser feita de duas maneiras:
-> Por Multiderivação Direta;
-> Por Multiderivação Indireta;


# OBS:
-> Não importa se a derivação é direta ou indireta. A classe que realizar a
   herança, herdará todos os atributos e métodos da super classe.
"""


# Exemplo Multiderivação Direta:

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class MultiDerivada(Base1, Base2, Base3):
    pass


# Exemplo Multiderivação Indireta:

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada(Base3):
    pass
