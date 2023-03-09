"""
Geradores:

# Geradores(Generators) são Iterators(Iteradores).

# OBS:
-> O contrário não é verdadeiro, ou seja, nem todo iterator é um generator.

# Outras informações:
-> Generators podem ser criados com funções geradoras;
-> Funções geradoras utilizam a palavra reservada yield;
-> Generators podem ser criados com Expressões Geradoras;

# Diferenças entre Funções e Generator Functions(Funções Geradoras):
-----------------------------------------------------------------------------------------
| Funções                               | Generator Functions                           |
-----------------------------------------------------------------------------------------
|-> Utilizam Return                     |-> Utilizam yield                              |
-----------------------------------------------------------------------------------------
|-> Retorna uma vez                     |-> Podem utilizar yield múltiplas vezes        |
-----------------------------------------------------------------------------------------
|-> Quando executada, retorna um valor  |-> Quando executada, retorna um generator      |
-----------------------------------------------------------------------------------------

"""


# Exemplo Generator Function:
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

# Uma Generator Function não é um Generator. Ela gera um generator. Validando:
gen = conta_ate(5)

print(type(gen))

for num in gen:
    print(num)
