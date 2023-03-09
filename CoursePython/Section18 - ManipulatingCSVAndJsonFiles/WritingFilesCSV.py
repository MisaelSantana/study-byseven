"""
Escrevendo em arquivos CSV:

# writer():
-> Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos 
   o método 'writerow()' para escrever cada linha. Este método recebe uma
   lista.
"""


# Utilizando writer():

from csv import writer

with open('D:\\CoursePython\\Section18 - ManipulatingCSVAndJsonFiles\\FilmesWriter.csv','w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])


# DictWriter:

from csv import DictWriter

with open('D:\\CoursePython\\Section18 - ManipulatingCSVAndJsonFiles\\FilmesDictWriter.csv','w') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração do filme em minutos: ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})
