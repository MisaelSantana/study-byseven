"""
Programação Orientada a Objetos: Atributos

# Atributos:
-> Representamos as características do objeto, ou seja, pelos atributos nós
   conseguimos representar computacionalmente os estados de um objeto.

# Em Python, dividimos os atributos em 3 grupos:
-> Atributos de Instância;
-> Atributos de Classe;
-> Atributos Dinâmicos;

# Atributos de instância:
-> São atributos declarados dentro do método construtor.


# OBS:
-> Método Construtor é um método especial utilizado para construção do objeto.

# Em Python, por convenção, ficou estabelecido que todo atribudo de uma classe
  é público, ou seja, pode ser acessado em todo o projeto. Caso queiramos
  demostrar que determinado atributo deve ser tratado como privado, ou seja
  que deve ser acessado/utilizado somente dentro da própria classe onde está
  declarado, utiliza-se __duplo underscore no início do seu nome.
  Isso é conhecido também como Name Mangling
"""


# Classes com atributo de Instância Público:
class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos públicos e Atributos Privados:
class Acesso:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha


"""
# OBS:
-> Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python
   não vai impedir que façamos acesso aos atributos sinalizados como privados 
   fora da classe
"""


# Exemplo (Name Mangling):
class Acesso:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def mostrar_email(self):
        print(self.__email)

    def mostrar_senha(self):
        print(self.__senha)

user = Acesso('user@gmailcom', '123456')

# print(user.email)

# print(user.senha)  # AttributeError

print(user._Acesso__senha)  # Temos acesso, porem não deveríamos fazer este acesso.

user.mostrar_email()
user.mostrar_senha()


"""
# Atributos de instância:

-> Significa que ao criarmos instâncias/objetos de uma classe, todas as 
   instâncias terão estes atributos.
"""


user1 = Acesso('user1@gmail.com', '12376231')
user2 = Acesso('user2@gmail.com', 'mkasdiq8wqe32432')

user1.mostrar_email()
user2.mostrar_email()


"""
# Atributos de Classe:

-> São atributos que são declarados diretamente na classe, ou seja,
   fora do construtor. Geralmente já inicializamos um valor, e este
   valor é compartilhado entre todas as instâncias da classe. Ao invés
   de cada instâncias da classe ter seus próprios valores como é o 
   caso dos atributos de instância, como os atributos de classe todas 
   as instâncias terão o mesmo valor para este atributo.
"""


# Refatorando classe Produto:
class Produto:

    # Atributo de classe:
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        # Atributo de instância:
        self.id = Produto.contador +1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('PlayStation4', 'Vídeo Game', 2300)
p2 = Produto('Xbox S', 'Vídeo Game', 4500)

print(p1.imposto)  # Acesso possível, mas incorreto de um atributo de classe.
print(p2.imposto)  # Acesso possível, mas incorreto de um atributo de classe.

print(p1.valor)  # Acesso possível, mas incorreto de um atributo de classe.
print(p2.valor)  # Acesso possível, mas incorreto de um atributo de classe.

# OBS: Não precisamos criar uma instância de uma classe para fazer
# acesso a um atributo de classe.

print(Produto.imposto)  # Acesso correto de um atributo de classe.

print(p1.id)
print(p2.id)


"""
# Atributos Dinâmicos:

-> Um atributo de instância que pode ser criado em tempo de execução.

# OBS:
-> O atributo dinâmico será exclusivo da instância que o criou.
"""


p1 = Produto('PlayStation4', 'Vídeo Game', 2300)
p2 = Produto('Xbox S', 'Vídeo Game', 4500)


# Criando um atributo dinâmico em tempo de execução:

p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso.

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Peso: {p2.peso}')


# Deletando atributos:
print(p1.__dict__)
print(p2.__dict__)

del p2.peso

print(p1.__dict__)
print(p2.__dict__)
