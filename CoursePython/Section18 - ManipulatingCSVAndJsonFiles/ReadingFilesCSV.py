"""
Lendo arquivos CSV com Python:

# CSV:
-> Comma Separeted Values(Valores Separados por Vírgula)


# A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
-> Reader: Permite que iteremos sobre as linhas do arquivo CSV como listas;
-> DictReader: Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;
"""


# Possível de se trabalhar, mas não é o ideal(trabalhoso):

with open('D:\\CoursePython\\Section18 - ManipulatingCSVAndJsonFiles\\Lutadores.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    print(dados)


# Reader:
from csv import reader

with open('D:\\CoursePython\\Section18 - ManipulatingCSVAndJsonFiles\\Lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pular a primera linha(cabeçalho)
    for linha in leitor_csv:
        # Cada linha é uma lista:
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')


# DictReader:
from csv import DictReader

with open('D:\\CoursePython\\Section18 - ManipulatingCSVAndJsonFiles\\Lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')  # Aqui você define qual delimitador utilizar. Default ','.
    for linha in leitor_csv:
        # Cada linha é um OrderedDict:
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")


# DictReader com outro separador:
from csv import DictReader

with open('D:\\CoursePython\\Section18 - ManipulatingCSVAndJsonFiles\\Lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict:
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")
