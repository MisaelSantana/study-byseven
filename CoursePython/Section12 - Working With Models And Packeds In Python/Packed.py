"""
Pacotes:

# Módulo: É apenas um arquivo Python que pode ter diversas funções para utilizarmos.

# Pacote: É um diretório, contendo uma coleção de módulos.

# OBS:
-> Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo
chamado __init__.py
-> Nas versões do Python 3.x, não é mais obrigatóra a utilização deste arquivo, mas
normalmente ainda é utilizado para manter a compatibilidade.

"""


# Utilizando modulos externos
from Geek import geek1, geek2

from Geek.university import geek3, geek4

# Prints das funções dos arquivos: geek1, geek2
print(geek1.pi)
print(geek1.funcao1(4, 6))
print(geek2.curso)
print(geek2.funcao2())

# Prints das funções dos arquios: geek3, geek4
print(geek3.funcao03())
print(geek4.funcao04())


# Importando apenas um arquivo do pacote e uma única função:
from Geek.geek1 import funcao1

print(funcao1(6, 9))
