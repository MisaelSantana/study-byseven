#*-* coding=utf-8 *-*
import re
from typing import Pattern

text = ("para entrar em Contato\n"
		  "r. Alagoas, 1049 5º e 6º andares\n"
		  "Savassi - Belo Horizonte MG Brasil\n"
		  "+55 31 3261 8083\n"
		  "contato@ancieladvogados.com.br\n"
		  "11/08/2016")

pattern = re.compile(r'^.{10,40}$', re.M)
list = pattern.findall(text)
print(list)

pattern = re.compile(r'^[a-z].{10,40}$', re.M|re.I)
list = pattern.findall(text)
print(list)

pattern = re.compile(r'^.*$', re.M|re.I|re.DOTALL)
list = pattern.findall(text)
print(list)

pattern = re.compile(r'(?mis)^.*$')
list = pattern.findall(text)
print(list)
