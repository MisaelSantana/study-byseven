"""
Levantando os próprios erros com raise:

# Raise:
-> Lança exeções;
-> O Raise não é uma função. É uma palavra reservada, assim como 'def' ou qualquer outra em Python.

# Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exeções
e mensagens de erro.

# A forma geral de utilização é:
-> raise TipoDoErro('<Mensagem de erro>')
"""


# Exemplo de uso:
def colore(texto, cor):
    cores = ('Verde', 'Amarelo', 'Azul', 'Preto',)
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek', 3)
colore(4, 3)
colore('Geek', 'Branco')
# Correto:
colore('Geek', 'Azul')
