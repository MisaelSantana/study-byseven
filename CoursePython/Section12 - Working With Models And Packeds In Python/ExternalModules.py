"""
Módulos externos:

# Utilizamos o gerenciador de pacotes Python chamado 'Pip'(Python Installer Package)

# Sintaxe para instalar algum pacote utilizando pip:
-> pip install <nomde_do_pacote>

# Colorama:
-> Ele é utilizado para permitir impressão de texto coloridos no terminal.

"""


# Importando o colorama:
from colorama import (
    Fore, 
    Back, 
    Style
)

init()

print(Fore.GREEN + 'Misael Santana')
print(Fore.CYAN + 'Misael Santana')
print(Fore.MAGENTA + 'Misael Santana')
print(Back.RED + 'Misael Santana')
print(Style.DIM + 'Misael Santana')
print(Style.RESET_ALL + 'Misael Santana')


# Criando um arquivo PDF:
import pydf

pdf = pydf.generate_pdf('<h1>Misael Santana</h1><br/><br/><strong>Teste</strong>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
