"""
Json e Pickle:

# JSON:
-> Significa JavaScript Object Notation.

# API's:
-> São meios de comunicação entre os serviços oferecidos por empresas(Twitter, Facebook, 
   Youtube) e terceiros (nós desenvolvedores)
"""

# Trabalhando com json: # -> Formatando as aspas '' para "" utilizando 'json.dumps()':
import json

ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220v', 2340)}])
print(type(ret))
print(ret)


# Transformando em JSON:
class Gato:
    
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Siames')
print(felix.__dict__)

ret = json.dumps(felix.__dict__)
print(ret)


# Integrando o JSON com o Pickle:
# Execute 'pip install jsonpickle' para fazer a instalação da biblioteca.


import jsonpickle

class Gato:
    
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Siames')

ret = jsonpickle.encode(felix)
print(ret)


with open('D:\\CoursePython\\Section18 - ManipulatingCSVAndJsonFiles\\Felix.json', 'w') as arquivo:
    # Modela para o formato 'jsonpickle:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)


# Lendo o arquivo json/pickle:

import jsonpickle

class Gato:
    
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


with open('D:\\CoursePython\\Section18 - ManipulatingCSVAndJsonFiles\\Felix.json', 'r') as arquivo:
    # Modela para o formato 'jsonpickle:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
