"""
Seeks e Cursors:

# seek():
-> É utilizada para movimentar o cursor pelo arquivo.
-> A função seek é utilizada para movimentação do cursor pelo arquivo.
Ela recebe um parâmetro que indica onde queremos colocar o cursor.

# cursors():
-> É o cursor para saber em que parte do texto estamos.

# readline():
-> Função que faz a leitura do arquivo linha à linha.

# readlines():
-> Lê as linhas e retorna as linhas em uma lista de strings.

# OBS:
-> Quando abrimos um arquivo com a função open(), é criada uma conexão
entre o arquivo no disco do computador e o programa. Essa conexão é chamada
de streaming. Ao finalizar os trabalhos com o arquivo, devemos fechar
essa conexão. Para isso utilizamos a função close().
"""


# Exemplo
arquivo = open('Section13 - ReadAndWriteFiles\\texto.txt')

print(arquivo.read())


# Movimentando o cursor pelo arquivo com a função seek():
arquivo.seek(0)
print(arquivo.read())


# Readline():
arquivo = open('Section13 - ReadAndWriteFiles\\texto.txt')
print(arquivo.readline())


# Readlines():
arquivo = open('Section13 - ReadAndWriteFiles\\texto.txt')
print(arquivo.readlines())


# Passo-à-passo para se trabalhar com o arquivo:

# Abrir arquivo:
arquivo = open('Section13 - ReadAndWriteFiles\\texto.txt')

# Trabalhar no arquivo:
print(arquivo.read())

# Fechar o arquivo:
arquivo.close()

# Verifica se o arquivo foi fechado:
print(arquivo.closed)


# Limitar a quantidade de caracteres que serão lidos:
arquivo = open('Section13 - ReadAndWriteFiles\\texto.txt')

print(arquivo.read(50))
