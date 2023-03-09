"""
Mapas:

# Conhecidos em Python como 'Dicionários'.

# Dicionários em Python são representados por chaves: {}
"""


receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Interar sobre dicionários:
for chave in receita:
    print(chave)


for chave in receita:
    print(receita[chave])


for chave in receita:
    print(f'{chave}: {receita[chave]}')


for chave in receita:
    print(f'Em {chave} recebi {receita[chave]}')


# Retornar apenas as chaves contidas no dicionário:
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])


# Retornar apenas os valores:
print(receita.values())

for valor in receita.values():
    print(valor)


# Desempacotamento de dicionários:
print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')


# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(min(receita.values()))
print(max(receita.values()))
print(len(receita))