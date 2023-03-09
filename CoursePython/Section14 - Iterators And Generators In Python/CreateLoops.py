"""
Criando sua própria versão de Loop:

# 
"""


# Exemplo:

nome = 'Geek University'
numero = [1, 2, 3, 4, 5]

for num in numero:
    print(num)


for letra in nome:
    print(letra)

iter(nome)
iter(numero)


# Meu for:
def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for([1, 2, 3, 4, 5])
meu_for('Geek University')
