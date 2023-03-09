"""
Leitura de Arquivos:

# Para ler o conteúdo de um arquivo Python, utilizamos a funçao integrada open(),
que literalmente significa 'abrir'.

# open():
-> Na forma mais simples de utilização, nós passamos apenas um parâmetro de entrada,
que neste caso é o caminho para arquivo a ser lido.
-> Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

# OBS:
-> Por padrão, a função open() abre o arquivo para leitura.
-> O arquivo DEVE exister, ou então teremos o erro FileNotFoundError

"""


# Exemplo:
arquivo = open('Section13 - ReadAndWriteFiles\\texto.txt')

print(arquivo)
print(type(arquivo))

# Retorno:
#<_io.TextIOWrapper name='Section13 - ReadAndWriteFiles\\texto.txt' mode='r' encoding='cp1252'>


# Lendo o conteúdo do arquivo:
arquivo = open('Section13 - ReadAndWriteFiles\\texto.txt')

print(arquivo.read())

# OBS: O Python, utiliza um recurso para trabalhar com arquivos chamado cursor.
# Esse cursor funciona como o cursor quando estamos escrevendo.
