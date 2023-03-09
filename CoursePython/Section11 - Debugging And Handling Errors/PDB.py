"""
Debugando com PDB:

# PDB: Python Debugger.
# Bug significa inseto.


"""

"""
# Exemplo com PDB: # -> Python Debugger:
# Para utilizar o Python Debugger, precisamos* importar a lib pdb e então utilizar a função set_trace().

# Comandos básicos do PDB:
-> l (listar onde estamos no código);
-> n (próxima linha);
-> p (imprime variável);
-> c (continua a execução - finaliza o debugging)

"""


# Exemplo utilizando o Python Debugger:

nome = 'Misael'
sobrenome = 'Santana'
# pdb.set_trace()
breakpoint()
nome_completo = nome + '' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
