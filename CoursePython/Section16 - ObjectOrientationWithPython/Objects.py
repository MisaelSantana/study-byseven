"""
POO - Objetos

# Objetos:
-> São instâncias da classe, ou seja, após o mapeamento do objeto do mundo real
   para a sua representação computacional, devemos poder criar quantos objetos 
   forem necessários. Podemos pensar nos objetos/instâncias de uma classe como 
   variáveis do tipo definido na classe.
"""


# Exemplos:
class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O Cliente é {self.__cliente._Cliente__nome}')

class Cliente:
    
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz Oi!')

# Instâncias/Objetos:

# Lâmpada:
lamp1 = Lampada('branca', 220, 60)
lamp1.ligar_desligar()

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')


# Usuário:
user1 = Usuario('Misael', 'Santana', 'misaelsantana2021@hotmail.com', '123456')


# Conta Corrente e Cliente:
cli1 = Cliente('Misael', '123.123.123-00')
cc = ContaCorrente(5000, 20000, cli1)

cc.mostra_cliente()

cc._ContaCorrente__cliente.diz()
