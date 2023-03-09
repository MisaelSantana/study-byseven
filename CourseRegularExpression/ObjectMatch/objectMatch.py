#*-* coding=utf-8 *-*
import re

text = ("para entrar em Contato "
		  "r. Alagoas, 1049 5º e 6º andares "
		  "Savassi - Belo Horizonte MG Brasil "
		  "+55 31 3261 8083 "
		  "contato@ancieladvogados.com.br "
		  "11/08/2016")

pat = r'\b(\d{2})\/(\d{2})\/(\d{4})'
m = re.search(pat, text)

if m:
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
