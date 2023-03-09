"""
Block With:

# O bloco with é utilizado para criar um contexto de trabalho onde
os recursos utilizados são fechados após o block with.
"""


# Block With:
with open('Section13 - ReadAndWriteFiles\\texto.txt') as arquivo:
    print(arquivo.read())

# Validando se o arquivo realmente foi encerrado:
print(arquivo.closed)
