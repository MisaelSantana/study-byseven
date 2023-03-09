"""
StringIO:

# ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional, 
o software precisa ter permissão para:
-> Permissão de Leitura;
-> Permissão de Escrita;

# StringIO:
-> Utilizado para ler e criar arquivos em memória.
"""


# Utilizando StringIO:
from io import StringIO

mensagem = 'Esta é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo
# vazio para inserirmos textos depois

arquivo = StringIO(mensagem)

# Agora tendo o arquivo podemos utilizar tudo que já sabemos.
print(arquivo.read())
