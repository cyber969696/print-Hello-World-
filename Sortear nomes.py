# Python 3.8.5 Script criado por David Lins 02/08/2020 às 02:10 AM

# Importar módulos
from time import sleep
from random import randint

# Banner em Print
print("{:=^77}".format(" Sortear nomes "))

# Lista para armazenar os nomes
lista_de_nomes = []

# Loop em while
while True:
	
	# Varíavel que irá receber a resposta do usúario
	perg = input("\033[1mDeseja iniciar?\033[m (y/n): ").strip().upper()
	
	# Início da befurcação (1)
	if perg == "Y":
	
		# Loop de inicialização com sleep de 2 segundo
		print("\033[1;32mIniciando...\033[m")
		sleep(2)
	
		# Varíavel que irá perguntar ao usúario se ele quer saber como o programa funciona
		perg2 = input("\033[1mQuer saber como o programa funciona?\033[m (y/n): ").strip().upper()
		
		# Befurcação (2)
		if perg2 == "Y":
			
			# Print descrevendo o programa
			print('''\033[4;32mVocê terá que digitar 5 nomes, o programa irá sortear algum destes nomes.\033[m''')
			sleep(3)
			
			# Varíaveis que irá armazenar o nome dos usúarios
			nome = input("\033[1mDigite o primeiro nome:\033[m ")
			sleep(1)
			nome2 = input("\033[1mDigite o segundo nome:\033[m ")
			sleep(1)
			nome3 = input("\033[1mDigite o terceiro nome:\033[m ")
			sleep(1)
			nome4 = input("\033[1mDigite o quarto nome:\033[m ")
			sleep(1)
			nome5 = input("\033[1mDigite o quinto nome:\033[m ")
			
			# Processo de adicionar os nomes a lista
			lista_de_nomes.append(nome)
			lista_de_nomes.append(nome2)
			lista_de_nomes.append(nome3)
			lista_de_nomes.append(nome4)
			lista_de_nomes.append(nome5)
			
			print(lista_de_nomes)
			# Loop de processamento
			print("\033[1;32mProcessando...\033[m")
			sleep(1)
			
			# Varíavel que irá coletar a resposta do usúario
			perg3 = input("\033[1mDeseja sortear?\033[m (y/n): ").strip().upper()
			
			# Início da befurcação (3)						
			if perg3 == "Y":
				
				# Processo de sorteio
				processo = randint(0, 4)
				
				# Mostrar o resultado do sorteio
				print("O nome sorteado foi \033[4;1;32m{}\033[m".format(lista_de_nomes[processo]))
				sleep(1)
				break
			
			elif perg3 == "N":
				
				# Encerramento do programa
				print("\033[1;31mEncerrando...\033[m")
				sleep(2)
				break
				
			else:
				
				# Print avisando que o programa não entendeu
				print("\033[31mNão foi possível entender!\033[m")
				
		elif perg2 == "N":
			
			# Varíaveis que irá armazenar o nome dos usúarios
			nome = input("\033[1mDigite o primeiro nome:\033[m ")
			sleep(1)
			nome2 = input("\033[1mDigite o segundo nome:\033[m ")
			sleep(1)
			nome3 = input("\033[1mDigite o terceiro nome:\033[m ")
			sleep(1)
			nome4 = input("\033[1mDigite o quarto nome:\033[m ")
			sleep(1)
			nome5 = input("\033[1mDigite o quinto nome:\033[m ")
			
			# Processo de adicionar os nomes a lista
			lista_de_nomes.append(nome)
			lista_de_nomes.append(nome2)
			lista_de_nomes.append(nome3)
			lista_de_nomes.append(nome4)
			lista_de_nomes.append(nome5)
			
			print(lista_de_nomes)
			# Loop de processamento
			print("\033[1;32mProcessando...\033[m")
			sleep(1)
			
			# Varíavel que irá coletar a resposta do usúario
			perg3 = input("\033[1mDeseja sortear?\033[m (y/n): ").strip().upper()
			
			# Início da berfucação (4)
			if perg3 == "Y":
				
				# Processo de sorteio
				processo = randint(0, 4)
				
				# Mostrar o resultado do sorteio
				print("O nome sorteado foi \033[4;1;32m{}\033[m".format(lista_de_nomes[processo]))
				sleep(1)
				break
			
			elif perg3 == "N":
				
				# Encerramento do programa
				print("\033[1;31mEncerrando...\033[m")
				sleep(2)
				break
			
	elif perg == "N":
		
		# Encerramento do programa
		print("\033[1;31mEncerrando...\033[m")
		sleep(2)
		break
	
	else:
		
		# Print avisando que o programa não entendeu a resposta
		print("\033[31mNão foi possível entender!\033[m")
		
		
	
	
	
	
