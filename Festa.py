# ////////////////////////////////////////////////////////
# Python 3.8.3 
# Script criado em 16/09/2020 as 14:41
# Desenvolvido por David Lins
# Link do Github: https://www.github.com/cyber969696/Beemo/tree/master/Beemo%201.0.py
# Script criado para estudo, com a função de treinar a manipular listas. Este código estará no meu Github, caso queira analísar outros projetos feitos por mim.
# Meio de contato: 
# Email: jamaicaserj@gmail.com
#Facebook: David lins
# Telefone: 11959723596
# ////////////////////////////////////////////////////////

# Importar módulos
from time import sleep

# Lista dos convidados
lista = []

# Def com Sleep de 1 segundo
def loop ():
	sleep(1)

# Programa com loop de while 
while True:
	
	# Print de inicialização
	print("\033[1;32mIniciando programa...\033[m")
	print(" ")
	loop()
	
	# Varíavel perguntando se o usúario deseja ver a lista de convidados
	perg4 = input("\033[1mDeseja ver a lista de convidados?\033[m (y/n): ").strip().upper()
	print(" ")
	
	# Se a resposta for sim
	if perg4 == "Y":
		sleep(0.5)
		print(lista)
		print(" ")
	
	# Se a resposta for não
	elif perg4 == "N":
		loop()
	
	# Se for nada 
	else:
		print("\033[1;4;31mNão foi possível prosseguir!\033[m")
		loop()
		break
	
	# Varíavel perguntando ao úsuario se ele quer digitar os nomes dos convidados
	perg = input("\033[1;32mDeseja digitar o nome dos convidados?\033[m (y/n): ").strip().upper()
	print(" ")
	
	# Se for sim
	if perg == "Y":
		
		# While com o programa
		while True:
			
			# Falar para o úsuario digitar os nomes dos convidados
			perg2 = input("\033[1mDigite o nome do convidado:\033[m ").strip().capitalize()
			
			# Função que irá exportar os nomes para a lista
			lista.append(perg2)
			print(" ")
			
			# Perguntar se o úsuario deseja adicionar outro nome
			perg3 = input("\033[1mDeseja adicionar outro convidado?\033[m (y/n): ").strip().upper()
			print(" ")
			
			# Se for sim
			if perg3 == "Y":
				sleep(0.5)
				
			# Se for não
			elif perg3 == "N":
				print("\033[1;31mVoltando...\033[m")
				print(" ")
				loop()
				break
				os.system("clear")
			
			# Se for nada
			else:
				print("\033[1;4;31mNão foi possível prosseguir!\033[m")
				print(" ")
				sleep(1)
				break
	
	# Se tudo isso for não
	elif perg == "N":
			print("\033[1;31mEncerrando o programa...\033[m")
			print(" ")
			loop()
			break
			os.system("clear")
	
	# Ou se for nada
	else:
		print("\033[1;4;31mNão foi possível prosseguir!\033[m")
		loop()
		break
