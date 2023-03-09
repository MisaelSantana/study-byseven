"""
Recebendo dados do usuário.

# input():
# Todo dado recebido via input é do tipo String:

# Em Python, string é tudo que estiver entre:
-> Aspas simples;
-> Aspas duplas;
-> Aspas simples triplas;
-> Aspas duplas triplas;

# Exemplos:
-> Aspas simples = 'Misael'
-> Aspas duplas = "Misael"
-> Aspas simples triplas = '''Misael'''
-> Aspas duplas triplas = ""Misael"" (não foi colocado a ultima aspa porque
vai quebrar o comentário)
"""

# Input antigo:
"""
# Entrada de dados;
print('Qual seu nome?')
nome = input() # Input -> Entrada

# Exemplo de print "antigo" 2.x
print('Seja bem-vindo(a) %s' % nome.title())

print("Qual a sua idade?")
idade = input()

# Processamento;

# Saída de dados;
print('%s tem %s anos' % (nome.title(), idade))
"""

# Input 'moderno':
"""
# Exemplo de print "moderno" 3.x:
print('Qual seu nome?')
nome = input() # Input -> Entrada

print('Seja bem-vindo(a) {0}'.format(nome.title()))


print("Qual a sua idade?")
idade = input()

print('{0} tem {1} anos'.format(nome.title(), idade))
"""

# Input atual:
"""
print('Qual seu nome?')
nome = input() # Input -> Entrada

print(f'Seja bem-vindo(a) {nome.title()}')


print("Qual a sua idade?")
idade = input()

print(f'{nome.title()} tem {idade} anos')

# int(idade) => cast

Cast é a conversão de um tipo de dado para outro.

print(f'{nome.title()} nasceu em {2021 - int(idade)}')
"""

# Último modelo:
nome = input('Qual seu nome? ')
print(f'Seja bem-vindo(a) {nome.title()}')

idade = int(input('Qual a sua idade? '))
print(f'{nome.title()} tem {idade} anos')

print(f'{nome.title()} nasceu em {2021 - idade}')
