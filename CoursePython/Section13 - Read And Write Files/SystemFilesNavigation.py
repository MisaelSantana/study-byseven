"""
Sistemas de Arquivos e Navegação:

# Para fazer uso de manipulação de arquivos do sistema operacionl, precisamos 
importar e fazer uso do módulo 'os':

# os:
-> Operating System(Sistema Operacional)

# getcwd():
-> Pega o current work directory (diretório de trabalho corrente)

"""


# Fazer o import:
import os

# getcwd():
print(os.getcwd())

# Para mudar de diretório, podemos utilizar o chdir():
os.chdir('..')
print(os.getcwd())


# Podemos checar se um diretório é relativo ou absoluto:
print(os.path.isabs('D:\\CoursePython'))


# Podemos identificar o sistema operacional com o módulo OS:
print(os.name)

# Podemos ter mais detalhes do sistema operacional:
print(os.uname())  # Não funciona em Windows.


# Sys platform:
import sys

print(sys.platform)


# Juntando diretório em Python:
import os

os.chdir("D:\\CoursePython\\Section13 - ReadAndWriteFiles\\")
print(os.getcwd())

res = os.path.join(os.getcwd(), 'Geek')
os.chdir(res)
print(os.getcwd())


# Listar diretórios ou arquivos:
import os

print(os.listdir("D:\\CoursePython\\Section13 - ReadAndWriteFiles\\"))  # Retorna uma lista.


# Listar diretórios ou arquivos com mais detalhes:
import os

scanner = os.scandir("D:\\CoursePython\\Section13 - ReadAndWriteFiles\\")
arquivos = list(scanner)

print(arquivos)

scanner.close()
