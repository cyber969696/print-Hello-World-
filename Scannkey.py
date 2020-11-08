import socket, os # Bibliotecas Socket & Os

from time import sleep # Biblioteca Timer

print("Scannkey.py")

print("Ultima atualização em \033[32m11/04/2020\033[m \nVersão \033[32m1.0\033[m")

print('''Script criado por: David Lins
Python \033[32m3.8\033[m
\033[36mhttps://github.com/cyber969696\033[m
\033[4mjamaicaserj@gmail.com\033[m''')

print('''
███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗██╗  ██╗███████╗██╗   ██╗
██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██║ ██╔╝██╔════╝╚██╗ ██╔╝
███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╔╝ █████╗   ╚████╔╝
╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔═██╗ ██╔══╝    ╚██╔╝
███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║██║  ██╗███████╗   ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝''')

print("\033[1;4mO Scannkey só funciona com redes internas.\033[m") # Print com aviso

print(" ")

sleep(1)
 
# Armazenar resposta de inicialização
perg = input("\033[1mDeseja iniciar o Scannkey?\033[m (y/n): ").strip().upper()

sleep(1)


# Se for sim
if perg == "Y":
	
	os.system("clear")
	
	print('''
███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗██╗  ██╗███████╗██╗   ██╗
██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██║ ██╔╝██╔════╝╚██╗ ██╔╝
███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╔╝ █████╗   ╚████╔╝
╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔═██╗ ██╔══╝    ╚██╔╝
███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║██║  ██╗███████╗   ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝''')

	# Menu de opções
	print('''
[1] \033[32mVerificar portas\033[m
[2] \033[32mScannear portas\033[m''')

	# Armazenar escolha
	perg2 = input("\033[1m: \033[m")
	
	sleep(1)
	
	# Se for 1 opção
	if perg2 == "1":
		
		os.system("clear")
		
		print('''
███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗██╗  ██╗███████╗██╗   ██╗
██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██║ ██╔╝██╔════╝╚██╗ ██╔╝
███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╔╝ █████╗   ╚████╔╝
╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔═██╗ ██╔══╝    ╚██╔╝
███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║██║  ██╗███████╗   ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝''')

		print(" ")
		
		# Armazenar o ip
		ip = input("\033[1mDigite o endereço de IP\033[m: ").strip()
		
		print(" ")
		
		sleep(1)
		
		# Armazenar porta
		port = int(input("\033[1mDigite a porta\033[m: "))
		
		print(" ")
		
		sleep(1)
		
		# Criando o objeto socket IPV4/TCP
		socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		# Quando conectar 
		if socket.connect_ex((ip, port)):
			
			# Porta fechada
			print("Porta: \033[4m{}\033[m: \033[31mClose\033[m".format(port))
			
			sleep(5)
			
			os.system("clear")
			
			os.system("exit")
			
		else:
			
			# Porta aberta
			print("Porta: \033[4m{}\033[m:  \033[32mOpen\033[m".format(port))
			
			sleep(5)
			
			os.system("clear")
			
			os.system("exit")
	
	# Se for 2 opção
	elif perg2 == "2":
		
		os.system("clear")
		
		print('''
███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗██╗  ██╗███████╗██╗   ██╗
██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██║ ██╔╝██╔════╝╚██╗ ██╔╝
███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╔╝ █████╗   ╚████╔╝
╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔═██╗ ██╔══╝    ╚██╔╝
███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║██║  ██╗███████╗   ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝''')

		print(" ")

		# Armazenar o ip
		ip2 = input("\033[1mDigite o endereço de IP\033[m: ").strip()
		
		print(" ")
		
		# Aviso
		print("\033[31mEste processo pode demorar um pouco.\033[m")
		
		print(" ")
		
		sleep(1)
		
		# Laço for 
		for port2 in range(1,65535):
			
			# Criar objeto socket IPV4/TCP
			socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			
			# Quando conectar
			if socket2.connect_ex((ip2, port2)) == 0:
				
				# Mostrar as portas encontradas
				print("\033[1mEndereço\033[m:", ip2,
				"\033[1mPorta\033[m:", port2)
				
				print(" ")
				
	# Se for nada
	elif perg2 == " ":
		
		print('''
███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗██╗  ██╗███████╗██╗   ██╗
██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██║ ██╔╝██╔════╝╚██╗ ██╔╝
███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╔╝ █████╗   ╚████╔╝
╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔═██╗ ██╔══╝    ╚██╔╝
███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║██║  ██╗███████╗   ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝''')

		print(" ")

		print("\033[31mOpção inexistente!\033[m")
	
		sleep(1)
	
		os.system("clear")
	
		os.system("exit")
	
# Se for não
elif perg == "N":
	
	os.system("clear")
	
	os.system("exit")
	
# Se for nada
else:
	
	print("\033[31mNão foi possível continuar!\033[m")
	
	os.system("clear")
	
	os.system("exit")
