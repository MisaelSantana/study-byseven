import re

string = '100 NORTH BROAD ROAD'
scopy = string.replace('ROAD', 'RD. ')
print(scopy)

m = re.sub(r'ROAD$', 'RD. ', string)
print(m)


text = ("para entrar em Contato\n"
		  "r. Alagoas, 1049 5º e 6º andares\n"
		  "Savassi - Belo Horizonte MG Brasil\n"
		  "+55 31 3261 8083\n"
		  "contato@ancieladvogados.com.br\n"
		  "11/08/2016")

m = re.sub(r'(\d\d)\/(\d\d)\/(\d{4})', r'\g<2>-\g<1>-\g<3>', text)
print(m)
