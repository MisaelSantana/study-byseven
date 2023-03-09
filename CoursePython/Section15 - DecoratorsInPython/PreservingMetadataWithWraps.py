"""
Preservando Metadata com Wraps:

# Metadados:
-> São dados intrísecos em arquivos.

# Wraps:
-> São funções que envolvem elementos com diversas finalidades.
"""


# Problema:
def ver_log(funcao):
    def logar(*args, **kwargs):
        """Função logar dentro de outra"""
        print(f'Você está chamado {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return(logar)

@ver_log
def soma(a, b):
    """Faz a soma entre dois números."""
    return(a + b)

print(soma(10, 30))

print(soma.__name__)
print(soma.__doc__)


# Resolver o problema:
from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Função logar dentro de outra"""
        print(f'Você está chamado {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return(logar)

@ver_log
def soma(a, b):
    """Faz a soma entre dois números."""
    return(a + b)

print(soma(10, 30))

print(soma.__name__)
print(soma.__doc__)
