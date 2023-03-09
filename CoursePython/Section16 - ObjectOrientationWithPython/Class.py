"""
Programação Orientada a Objetos: Classes

# Classes:
-> São modelos dos objetos do mundo real sendo representados computacionalmente.

# Imagine que você queira fazer um sistema para automatizar o controle das
  lâmpadas da sua casa.


# Classes podem conter:
-> Atributos: Representam as características do objeto, ou seja, pelos atributos
   conseguimos representar computacionalmente os estados de um objeto. No caso
   da lâmpada, possivelmente iríamos querer saber se a lâmpada é 110v ou 220v,
   se ela é branca, amarela, vermelha ou outra cor, qual é a luminosidade dela 
   e etc...
-> Métodos(funções): Representam os comportamentos do objeto, ou seja, as ações
   que esse objeto pode realiar no seu sistema. No caso da lâmpada, por exemplo,
   um comportamento que iriamos querer representar no nosso sistema é o de ligar e
   desligar a mesma.

# OBS:
-> Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda
   não está implementado.
-> Quando nomeamos nossas classes em Python, utilizamos por convenção o nome com
   a inicial em maiúscula. Se o nome for composto, utiliza-se as iniciais de ambas
   as palavras em maiúsculo, todas juntas.
-> Quando estamos planejando um software e definimos quais classes teremos que ter
   no sistema, chamamos estes objetos que serão mapeados para classes de entidade.
"""


# Exemplo Simples:
class Lampada:
    pass


lamp = Lampada()

print(lamp)
print(type(lamp))


# Exemplo de classes:
class Lampada:
    pass

class ContaCorrente:
    pass

class Produto:
    pass

class Usuario:
    pass
