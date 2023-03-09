"""
Escrevendo em arquivos:

# OBS:
-> Ao abrir um arquivo para leitura, não podemos realizar a escrita nele, apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente
escrever nele.
-> Ao abrir um arquivo para escrita, ele irá criar um novo arquivo. Se tiver o mesmo
nome de outro arquivo, o mesmo será sobscrito.
"""


# Exemplo de escrita:
with open('Section13 - ReadAndWriteFiles\\texto.txt', 'w') as arquivo:
    arquivo.write('Escrevendo no final do arquivo.\n')
    arquivo.write('Pode-se escrever várias linhas.\n')
    arquivo.write('Esta é a ultima linha.')
    print(arquivo.read())


# Recebendo dados do usuário e colocando no arquivo:
with open('Section13 - ReadAndWriteFiles\\EntradasUsuario.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
