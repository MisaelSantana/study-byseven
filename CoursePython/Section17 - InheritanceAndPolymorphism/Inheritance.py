"""
POO - Herança(Inheritance):

# A ideia de herança é a de reaproveitar código. Também extender nossas classes.

# OBS:
-> Com a herança, a partir de uma classe existente, nós extendemos outra classe
   que passa a herdar atributos e métodos da classe herdada.
-> Quando uma classe herda de outra classe, ela herda TODOS os atributos e métodos
   da classe herdada.

# Super():
-> Utiliza-se 'super().__init__(*args)' para realizar acesso aos atributos/metodos 
   da classe 'pai'

# Cliente:
-> nome;
-> sobrenome;
-> cpf;
-> renda;

# Funcionário:
-> nome;
-> sobrenome;
-> cpf;
-> matricula;


# Quando uma classe herda de outra classe, a classe herdada é conhecida por:
-> [Pessoa]
    -> Super Classe;
    -> Classe Mãe;
    -> Classe Pai;
    -> Classe Base;
    -> Classe Genérica;

# Quando uma classe herda de outra classe, ela é chamada:
-> [Cliente, Funcionario]
    -> Sub Classe;
    -> Classe Filha;
    -> Classe Específica;
"""


# Criando as classes:
class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return(f'{self.__nome} {self.__sobrenome}')

class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return(f'{self.__nome} {self.__sobrenome}')


# Testando:

cliente = Cliente('Misael', 'Santana', '123.123.123-00', '10000')
funcionario = Funcionario('Thaynara', 'Lemos Negri', '123.123.123-00', '20202909')

print(cliente.nome_completo())
print(funcionario.nome_completo())


# Refatorando:

class Pessoa:
    
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return(f'{self.__nome} {self.__sobrenome}')


class Cliente(Pessoa):
    """Cliente herda os atributos de 'Pessoa'"""

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda os atributos de 'Pessoa'"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


# Testando:

cliente = Cliente('Misael', 'Santana', '123.123.123-00', '10000')
funcionario = Funcionario('Thaynara', 'Lemos Negri', '123.123.123-00', '20202909')

print(cliente.nome_completo())
print(funcionario.nome_completo())

print(cliente.__dict__)
print(funcionario.__dict__)
