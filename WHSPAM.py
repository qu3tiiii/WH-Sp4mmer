import time, requests, os
from colorama import Fore
os.system('pip install requests')
os.system('pip install colorama')
os.system('cls')
os.system(f'Title Spammer By Qu3ti')
print(f"""{Fore.RED}
╔╗ ┌─┐┌─┐┌┬┐  
╠╩╗├┤ └─┐ │                                          
╚═╝└─┘└─┘ ┴   
███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝                               
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
===================Webhook Spammer By Qu3ti===================
================Github: https://github.com/qu3tiiii ==========                                                             


"""+Fore.RESET)

webhook = input(Fore.RED+'Ingresa Tu Webhook: '+Fore.RESET)

username = input(f"{Fore.RED}Nombre De Webhook: "+Fore.RESET)
message = input(f"{Fore.RED}Mensaje Para Spamear: "+Fore.RESET)

data = {
	    'content': message,
	    'username': username

	}

mnd = 0
mal = 0

while True:
		r = requests.post(webhook, data=data)

		if r.status_code == 204:
			mnd += 1
			print(f"{Fore.GREEN}[$] - '{message}' Enviado Correctamente{Fore.RESET}")
			os.system(f'title Spammer By Qu3ti  - Enviados : {mnd} ^/ Errores : {mal}')
		else:
			mal += 1
			print(f"{Fore.RED}[-] - Error{Fore.RESET}")
			os.system(f'title Spammer By Qu3ti  - Enviados : {mnd} ^/ Errores : {mal}')

