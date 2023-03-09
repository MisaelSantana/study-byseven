"""
Modos de abertura de arquivo:

# r:
-> Abre para leitura, padrão.

# w:
-> Abre para escrita, sobrescreve caso o arquivo já exista.

# x:
-> Abre para escrita somente se o arquivo não existir.

# a:
-> Adicionando o conteúdo para o final do arquivo(append).
"""


# Exemplo de x:
with open('Section13 - ReadAndWriteFiles\\university.txt', 'x') as arquivo:
    arquivo.write('Teste de conteúdo.\n')


# Exemplo de x:
with open('Section13 - ReadAndWriteFiles\\EntradasUsuario.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta, ou digite <sair> para sair')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
