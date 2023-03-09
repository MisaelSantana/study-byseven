#*-* coding=utf-8 *-*
import re

text = ("para entrar em Contato\n"
		  "r. Alagoas, 1049 5º e 6º andares\n"
		  "Savassi - Belo Horizonte MG Brasil\n"
		  "+55 31 3261 8083\n"
		  "contato@ancieladvogados.com.br\n"
		  "11/08/2016")

pat = r'^\w+@\w+[combr.]+$'
#m = re.match(pat, text, re.MULTILINE)
m = re.search(pat, text, re.MULTILINE)
if m:
    print(m.group())
