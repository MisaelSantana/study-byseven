"""
Sistemas de Arquivos Manipulação:

# 
"""


# Descobrindo se um arquivo ou diretório existe( serve tanto para arquivos como diretórios):
import os

print(os.path.exists("D:\\CoursePython\\Section13 - ReadAndWriteFiles\\"))


# Criando arquivos:
import os

# Forma 01:
open("D:\\CoursePython\\Section13 - ReadAndWriteFiles\\arquivo-teste.txt", 'w').close()

# Forma 02:
open("D:\\CoursePython\\Section13 - ReadAndWriteFiles\\arquivo-teste2.txt", 'a').close()

# Forma 03:
with open("D:\\CoursePython\\Section13 - ReadAndWriteFiles\\arquivo-teste2.txt", 'w') as arquivo:
    pass


# Criando arquivos/diretório (Nova Forma):
import os

os.mknod("D:\\CoursePython\\Section13 - ReadAndWriteFiles\\arquivo-teste2.txt")
os.mkdir("D:\\CoursePython\\Section13 - ReadAndWriteFiles\\diretorio-teste")
# NÃO FUNCIONA EM MACOS/WINDOWS


# Criando multi-diretórios:
import os

os.makedirs("D:\\CoursePython\\Section13 - ReadAndWriteFiles\\diretorio-teste\\outrodiretorio")
# Funciona em Windows!


# Renomeando arquivos/diretórios:
import os

os.rename('nome-antigo', 'novo-nome')


# Deletando arquivos:
import os

os.remove('nome-do-arquivo')
# O arquivo não pode estar em uso.


# Deletando diretórios vazios:
import os

os.rmdir('caminho-do-diretorio')


# Criar arquivos e diretórios temporários:
import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University.\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo dentro dele criando
# um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
# os arquivos temporários 'vivos', dentro dos blocos 'with'.

# Funciona em Windows!
