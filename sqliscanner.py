import requests
import json

print('''
    Basic SQLi Scan
    Github: n3wf4g
    Discord: N3wf4g#2717
    ## This script don't use multi-threading ## 



''')
def scan():
    lists = input('Site list> ')
    lists = open(lists, 'r').readlines()
    lists = [line.replace('\n',"") for line in lists]
    for line in lists:
        data = line.split('\n')
        http = requests.get(data[0] + "'").text

        if http.find('You have an error in your SQL syntax;') == -1:
            print('✘ Not vuln (SQLi)> ' + data[0])
        else:
            print('✔ Vuln (SQLi)> ' + data[0])
            print(data[0], file=open("vulns.txt", "a+"))
scan()





