"""
POO - Métodos:

# Métodos(funções):
-> Representam os comportamentos do objeto, ou seja, as ações que esse 
   objeto pode realizar em seu sistema.

# Em Python, dividimos os métodos, em 2 grupos:
-> Métodos de Instância;
-> Métodos de Classe.


# Métodos de Instância:
-> O método dunder init '__init__', é um método especial chamado de construtor 
   e sua função é construir o objeto a partir da classe.

# OBS: 
-> Todo elemento em Python que inicia e finaliza com duplo underline
   é chamado de dunder (Double Underline)
-> Os métodos/funções dunder em Python são chamados de métodos mágicos.

"""


# Exemplo:
class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        sel.__cor = cor
        sel.__voltagem = voltagem
        sel.__luminosidade = luminosidade


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o Valor do Produto com o desconto"""
        return(self.__valor * (100 - porcentagem)) / 100

# Executando produto com desconto:
p1 = Produto('PlayStation4', 'Video Game', 2300)

print(p1.desconto(20))


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def nome_completo(self):
        return(f'{self.__nome} {self.__sobrenome}')

# Testando:
user1 = Usuario('Misael', 'Santana', 'email_teste1@gmail.com', 'budasih87372*¨&T52')
user2 = Usuario('Thaynara', 'Lemos Negri', 'email_teste2@gmail.com', 'asdmksada.as,><*281')

print(user1.nome_completo())
print(user2.nome_completo())


# Depois de casado:
class Casamento:

    def __init__(self, nome, sobrenome, nome_casado):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__nome_casado = nome_casado

    def nome_casado(self):
        return(f'{self.__nome} {self.__sobrenome} após casado, ficará {self.__nome_casado}')

noivo = Casamento('Misael', 'Santana', 'Misael Lemos Santana')
noiva = Casamento('Thaynara', 'Lemos Negri', 'Thaynara Lemos Negri Santana')

print(noivo.nome_casado())
print(noiva.nome_casado())


# Trabalhando com criptografia de senha:
from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return(f'{self.__nome} {self.__sobrenome}')

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('As senhas não conferem...')
    exit(42)

print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso Permitido')
else:
    print('Acesso Negado')

print(f'Senha User Criptografada: {user._Usuario__senha}')  # Somente para visualizar a senha criptografada.


# Métodos de classe:
from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    # Metodo de classe:
    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema')
        8
    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    # Metodos de instancias:
    def nome_completo(self):
        return(f'{self.__nome} {self.__sobrenome}')

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

user = Usuario('Misael', 'Santana', 'misael@gmail.com', '123456')

Usuario.conta_usuarios()
