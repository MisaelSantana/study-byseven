"""
Módulo Collections -> Default Dict:

# Default Dict: Ao criar um dicionário utilizando o 'Default Dict', nós informamos
um valor default, podendo utilizar um lambda para isso. Este valor será utilizado
sempre que não houver um valor definido. Caso tentemos acessar uma chave que não
existe, essa chave será criada e o valor default será atribuído.

# Lambdas:
-> São funções sem nome que podem ou não receber parâmetros de entrada e retornar valores.

"""


# Recapitulando:

# Dicionário:
dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)
print(dicionario['curso'])

# Importando Default Dict:
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)

# Retornar uma chave que não existe:
print(dicionario['outro'])

# -> Com Default Dict, ele retorna o valor da lambda.
# -> Em dicionários comuns, retornaria um KeyError.

print(dicionario)
# Ele adiciona o valor que não existe no dicionário (cria o objeto):
# Retorno = "defaultdict(<function <lambda> at 0x0000025817221EE8>, {'curso': 'Programação em Python: Essencial', 'outro': 0})"
