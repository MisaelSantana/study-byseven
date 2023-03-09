"""
Dicionários:

# OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

# Dicionários são coleções do tipo chave/valor.

# OBS: Sobre dicionários:
-> Chave e valor são separados por ':', '<chave>: <valor>';
-> Tanto a chave quanto valor, podem ser de qualquer tipo de dado;
-> Podemos misturar tipos de dados.
"""


# Validar se o tipo de dado é um dicionário:
print(type({}))


# Criação de Dicionário:

# Forma 1 (mais comum):
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (menos comum):
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))


# Acessando elementos:

# Forma 1: Acessando via chave, da mesma forma que lista/tupla.
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises['br'])
print(paises['eua'])
print(paises['py'])

# OBS: Caso tentamos fazer acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2: Acessando via get(recomendado):
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises.get('br'))
print(paises.get('eua'))
print(paises.get('py'))


# Exemplo 1:
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

russia = paises.get('ru')

if russia:
    print('Encontrei o país')
else:
    print('Não encontrei o país')


# Exemplo 2:
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

pais = paises.get('py')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')


# Exemplo 3: -> Podemos definir um valor padrão caso o valor passado não seja encontrado:
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

pais = paises.get('ru', 'não encontrado')

print(f'País {pais}')

# Caso o get não encontre o objeto com a chave informada, será retornado o valor 'None' e não será gerado KeyError.


# Verificando se uma chave se encontra no dicionário
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)
print('py' in paises)

if 'ru' in paises:
    russia = paises['ru']


# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionário,
# como chaves de dicionários.

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionários,
# pois as mesmas são imutáveis:

localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.2345, 45.2344): 'Escritório em Nova York',
    (12.1234, 78.2888): 'Escritório em Nova Zelândia',
    (23.3234, 12.2312): 'Escritório em Joinville'
}

print(localidades)
print(type(localidades))


# Adicionar elementos em um dicionário:
receita = {'jan': 100, 'fev': 200, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1(mais comum):
receita['abr'] = 400
print(receita)

# Forma 2:
novo_dado = {'mai': 500}    # receita.update({'mai': 500})

receita.update(novo_dado)
print(receita)


# Atualizando dados em um dicionário:

# Forma 1:
receita['mai'] = 550
print(receita)

# Forma 2:
receita.update({'mai': 600})
print(receita)

# CONCLUSÃO:
# -> A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# -> Em dicionários, NÃO podemos ter chaves repetidas.


# Remover dados de um dicionário:

# Forma 1 (mais comum):
receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita)

ret = receita.pop('mar')
print(ret)

print(receita)

# OBS:
# -> É obrigatório passar a chave, e caso não encontre o elemento, um KeyError é retornado.
# -> Ao removermos um objeto, o valor deste objeto é sempre retornado.
# -> Se tentar remover um valor que não existe, um KeyError será gerado.

# Forma 2:
del receita['fev']

print(receita)

# OBS: Neste caso, ao utilizar o 'del', o valor removido não é retornado.


# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras,
# na qual adicionamos produtos:

"""
Carrinho de compras:

    produto 1:
        nome;
        quantidade;
        preço;

    produto 2:
        nome;
        quantidade;
        preço;

    produto 3:
        nome;
        quantidade;
        preço;
"""
# Exemplo utilizando Lista:

carrinho = []

produto1 = ['playstation 4', 1, 2300.00]
produto2 = ['God Of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o índice de cada informação retornada no produto.

# Exemplo utilizando Tupla:

produto1 = ('playstation 4', 1, 2300.00)
produto2 = ('God Of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)


# Exemplo utilizando Dicionário:

carrinho = []

produto1 = {'nome': 'playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God Of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Dessa forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto,
# podemos ter a certeza sobre cada informação, conseguimos ver mais facilmente sobre o que é
# cada valor.


"""
# Métodos de dicionários:

-> clear;
-> copy;
-> fromkeys;
-> get;
-> items;
-> keys;
-> pop;
-> popitem;
-> setdefault;
-> update;
-> values;

"""


# Dicionário
d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar dicionário (zerar dados):
d.clear()
print(d)

# Copiando um dicionário para outro:

# Forma 1: -> # Deep Copy
novo = d.copy()
print(novo)

novo['d'] = 4
print(d)
print(novo)

# Forma 2: -> # Shallow Copy
novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)


# Forma não usual de criação de dicionário:
outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))


usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')

print(usuario)
print(type(usuario))

# O método 'fromkeys' recebe dois parâmetr0s: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
