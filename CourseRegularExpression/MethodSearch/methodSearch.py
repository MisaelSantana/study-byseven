#*-* coding=utf-8 *-*
import re

text = ("para entrar em Contato "
		  "r. Alagoas, 1049 5º e 6º andares "
		  "Savassi - Belo Horizonte MG Brasil "
		  "+55 31 3261 8083 "
		  "contato@ancieladvogados.com.br "
		  "11/08/2016")

#primeiro buscar a primeira palavra que começa com letra maiúcula
pattern = r'\b[A-Z]\w+'
match = re.search(pattern, text)
if match:
	print(match.group())
else:
	print('não casou')

#buscar data
pattern = r'\b[0-9]\w+'
match = re.search(pattern, text)
if match:
	print(match.group())
else:
	print('não casou')

#buscar o telefone
pattern = r'\+\d{2}.\d{2}.\d{4}.\d{4}'
match = re.search(pattern, text)
if match:
	print(match.group())
else:
	print('não casou')
