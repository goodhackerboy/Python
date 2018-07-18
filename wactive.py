from requests import post
import os

print('''
    Ativador Windows10
    Discord: N3wf4g#2717
    Info: [Script criado para ativar o windows sem nenhum esforço, é um script automatizado ou seja você só aperta enter e a magica acontece]

''')
print('Digite !ver para escolher a edição do seu windows\nTemos keys para as seguintes edições\n[Professional]\n[Enterprise]\n[Enterprise 2015 LTSB]\n[Home/Core]')
s = input("> ")
if s == '!ver':
    os.system('cls')
    os.system('title Ativador W10')
    print('[1] Professional\n[2] Enterprise\n[3] Enterprise 2015 LTSB\n[4] Home/Core')
    d = input('> ')
    if d == '1':
        os.system('cls')
        os.system('cscript slmgr.vbs /ipk "W269N-WFGWX-YVC9B-4J6C9-T83GX"')
        os.system('cls')
        os.system('cscript slmgr.vbs /skms kms.lotro.cc')
        os.system('cls')
        os.system('cscript slmgr.vbs /ato')
        exit()
    elif d == '2':
        os.system('cls')
        os.system('cscript slmgr.vbs /ipk "NPPR9-FWDCX-D2C8J-H872K-2YT43"')
        os.system('cls')
        os.system('cscript slmgr.vbs /skms kms.lotro.cc')
        os.system('cls')
        os.system('cscript slmgr.vbs /ato')
        exit()
    elif d == '3':
        os.system('cls')
        os.system('cscript slmgr.vbs /ipk "WNMTR-4C88C-JK8YV-HQ7T2-76DF9"')
        os.system('cls')
        os.system('cscript slmgr.vbs /skms kms.lotro.cc')
        os.system('cls')
        os.system('cscript slmgr.vbs /ato')
        exit()
    elif d == '4':
        os.system('cls')
        os.system('cscript slmgr.vbs /ipk "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"')
        os.system('cls')
        os.system('cscript slmgr.vbs /skms kms.lotro.cc')
        os.system('cls')
        os.system('cscript slmgr.vbs /ato')
        exit()
        


