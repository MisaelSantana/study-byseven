"""
Definindo Funções:

# Funções são pequenas partes de código que realizam tarefas específicas.
# Uma função pode ou não receber entradas de dados e retornar uma saída de dados.
# Muito uteis para executar procedimentos similares por repetidas vezes.

OBS: Se você escrever uma função que realiza várias tarefas dentro dela,
é bom fazer uma verificação para que a função seja simplificada.

# Já utilizamos várias funções desde que iniciamos este curso:
-> print()
-> len()
-> max()
-> min()
-> count()
-> e muitas outras;

"""


# Curso:
curso = 'Programação em Python: Essencial'

print(curso)


# Exemplo de utilização de funções:
cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()
print(cores)

cores.append('roxo')
print(cores)


# Limpar lista
cores.clear()
print(cores)


# Vizualisar documentação help:
print(help(print))


# Dry - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código.

"""
Definir funções:

# Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde: 

# nome_da_funcao
-> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case);

# parametros_de_entrada
-> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;

# bloco_de_funcao
-> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def', informando ao Python
que estamos definindo uma função. Também abrimos o bloco do código com o já conhecido dois pontos ":" que é utilizado
em Python para definir blocos.

"""


# Definindo a primeira função:

# Definição:
def diz_oi():
    print('Oi!')

"""
# OBS:

-> Dentro das nossas funções podemos utilizar outras funções;
-> Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer 'Oi!';
-> Essa função não recebe nenhum parâmetro de entrada;
-> Veja que esta função não retorna nada.
"""


# Chamada de execução:
diz_oi()


"""
ATENÇÃO:

# Nunca esqueça de utilizar o parênteses ao executar uma função:

# Errado:
diz_oi
diz_oi ()

# Certo:
diz_oi()
"""


# Exemplo 2:

# Definição:
def cantar_parabens():
    print('Parabens para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')

# Chamada da função:
cantar_parabens()

# Executando a função por meio de um for:
for cantar in range(5):
    cantar_parabens()

# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através de variável:
canta = cantar_parabens

canta()
