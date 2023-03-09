"""
POO - Método 'super()'

# O método 'super()' se refere à super classe.
"""


# Relembrando:
class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')

class Gato(Animal):

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)
        super().__init__(nome, especie)
        # O super serve para acessar qualquer elemento da classe pai
        super().faz_som('Auauauuaua')
        self.__raca = raca


# Testando a classe:
felix = Gato('Felix', 'Felino', 'Angorá')
felix.faz_som('miau')
