"""
POO - Abstração e Encapsulamento:

# O grande objetivo da Programação Orientada a Objeto(POO), é encapsular nosso
  código dentro de um grupo lógico e hierárquico utilizando classes.

# Encapsular:
-> Vem de cápsula, ou seja, o ato de encapsular uma classe.


# Relembrando Atributos/Métodos privados em Python:
-> Imagine que temos uma classe chamada 'Pessoa', contendo um atributo privado
   chamado '__nome' e um método privado chamado '__falar()'

-> Esses elementos privados só devem/deveriam ser acessados dentro da classe. 
   Mas Python não bloqueia este acesso fora da classe. Com Python acontece um 
   fenômeno chamado 'Name Mangling', que faz uma alteração na forma de acessar
   elementos privados, conforme:
   
   # Exemplo:
   _Classe__elemento

   instancia._Pessoa__nome
   instancia._Pessoa__falar()


# Abstração:
-> Abstração, em POO, é o aot de expor apenas dados relevantes de uma classe,
   escondendo atributos e métodos privados de usuário.

"""


# Exemplo utilizando classe com atributos públicos(NÃO UTILZAR):
# Não deve utilizar esse modelo para dados sensíveis, pois tanto podemos fazer
# a leitura dos dados, como também ALTERAÇÕES.

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


# Testando a classe:
conta1 = Conta('Misael', 150.00, 1500.00)

print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)


# Jeito certo:
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente!')
        else:
            print('O valor precisa ser positivo')


# Testando a classe:
conta1 = Conta('Misael', 150.00, 1500.00)

print(conta1.__dict__)
conta1.extrato()

# Depositar:
print(conta1.__dict__)
conta1.depositar(350)

print(conta1.__dict__)

# Sacar:
#conta1.sacar(1000)
conta1.sacar(100)

print(conta1.__dict__)


# Criar um método de transferência entre contas:
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente!')
        else:
            print('O valor precisa ser positivo')

    def transferir(self, valor, conta_destino):
        # Remover da conta de origem:
        self.__saldo = valor

        self.__saldo -= 10  # Taxa de transferência.

        # Adicionar o valor na conta de destino:
        conta_destino.__saldo += valor

# Testando:
conta1 = Conta('Misael', 300, 1000)
conta1.extrato()

conta2 = Conta('Thaynara', 500, 2000)
conta2.extrato()

conta2.transferir(150, conta1)

conta1.extrato()
conta2.extrato()
