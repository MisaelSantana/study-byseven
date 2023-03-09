"""
POO - Métodos Mágicos:

# Métodos Mágicos, são todos os métodos que utilizam deunder.

# Dunder Init:
-> Iniciar um objeto: '__init__()'

# Dunder Repr:
-> Representação do objeto: '__repr__'

# Dunder Str:
-> Representação do objeto em formato de string: '__str__'
"""


# Exemplo:

class Livro:
    
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return(self.titulo)

    def __str__(self):  # '__str__' tem prioridade na execução entre '__repr__'
        return(self.titulo)

    def __len__(self):
        return(self.paginas)

    def __add__(self, outro):
        return(f'{self} - {outro}')

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return(msg)
        return('Não posso multiplicar!')

    def __del__(self):
        print('Um objetodo do tipo Livro foi deletado da memória')


livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

# Testes:

print(livro1)
print(len(livro1))


print(livro2)
print(len(livro2))


print(livro1 + livro2)
# print(livro1 * 'Geek') #  Não posso multiplicar!
print(livro1 * 3)
print(livro2 * 2)
