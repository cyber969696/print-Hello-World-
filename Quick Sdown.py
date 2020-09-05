# Script criado em 05/08/2020 por David Lins
# Python 3.8.5

# Importar módulos
from time import sleep

# Banner de abertura
print("\033[32m="* 77)
print("\033[1;32m{:=^77}\033[m".format(" Quick Sdown "))
print("\033[32m=\033[m"* 77)
print(" ")

# While usado para o loop
while True:
	
	# Varíavel que irá receber a resposta do usúario
	perg = input("\033[1mDeseja iniciar?\033[m (y/n): ").strip().upper()
	print(" ")
	
	
	
	# If que irá receber a resposta Y
	if perg == "Y":
		
		# Print de inicialização
		print("\033[1;32mIniciando...\033[m")
		
		# Print para espaço
		print(" ")
		
		# Sleep (2)
		sleep(2)
		
		# Varíavel para armazenar número
		perg2 = int(input("\033[1mDigite um número de \033[1;4m0\033[m a \033[1;4m101\033[m:\033[m "))
		
		# Sleep (1)
		sleep(1)
		
		# Print para espaço
		print(" ")
		
		# Varíavel para armazenar outro número
		perg3 = int(input("\033[1mDigite mais um número:\033[m "))
		
		# Print com espaço
		print(" ")
		
		# Sleep (1)
		sleep(1)
		
		# Varíavel Len
		len=perg2 + perg3
		
		# Varíavel para calcular
		calc = (perg2) + (perg3)
		
		# Segunda varíavel para calcular
		calc2 = calc /2
	
	    # Befurcação 2	
		if perg2 > 101:
			
			# Print com aviso
			print("\033[1;31mNúmeros maiores que\033[m \033[1;4m101\033[m \033[4;31mnão é permitido.\033[m")
			
			# Print com espaço
			print("")
			
			# Sleep (1)
			sleep(1)
			
		# Elif 2
		elif perg2 <0:
			
			# Print com aviso
			print("\033[1;31mNão é permitido números negativos.\033[m")
			
			# Print com espaço
			print(" ")
			
			# Sleep (1)
			sleep(1)
		
		# Befurcação 3
		elif perg3 > 101:
			
			# Print com aviso
			print("\033[1;31mNúmeros maiores que\033[m \033[1;4m101\033[m \033[4;31mnão é permitido.\033[m")
			
			# Print com espaço
			print("")
			
			# Sleep (1)
			sleep(1)
		
		# Elif 2		
		elif perg3 <0:
				
				# Print com aviso
				print("\033[1;31mNão é permitido números negativos.\033[m")
				
				# Print com espaço
				print(" ")
				
				# Sleep (1)
				sleep(1)
	
	    # Else do if 1		
		else:
			
			# Print mostrar os números inseridos
			print("\033[1;4;32mVocê inseriu dois números, primeiro número\033[m \033[4;1m{}\033[m, \033[4;1;32msegundo número\033[m \033[4;1m{}\033[m".format(perg2, perg3))
			
			# Print com espaço
			print(" ")
			
			# Sleep (2)
			sleep(2)
			
			# Print mostrar o total de números
			print("\033[4;1;32mNo total você inseriu\033[m \033[4;1m{}\033[m \033[4;1;32mnúmeros.\033[m".format(len))
			
			# Print com espaço
			print(" ")
			
			# Sleep (2)
			sleep(2)
			
			# Befurcação 3
			if perg2 > perg3:
				
				# Print mostrando o número maior
				print("\033[1;32mO número\033[m \033[1;4m{}\033[m \033[1;32mé o maior.\033[m".format(perg2))
				
				# Print com espaço
				print(" ")
			
			# Befurcação 4		
			if perg3 > perg2:
				
				# Print mostrando o número maior
				print("\033[1;32mO número\033[m \033[1;4m{}\033[m \033[1;32mé o maior.\033[m".format(perg3))
				
				# Print com espaço
				print(" ")
			
			# Befurcação 5		
			if  perg2 < perg3:
				
				# Print mostrando o número menor
				print("\033[1;31mO número\033[m \033[1;4m{}\033[m \033[1;31mé o menor.\033[m".format(perg2))
				
				# Print com espaço
				print(" ")
				
				# Sleep (2)
				sleep(2)
			
			# Elif 3		
			elif perg3 < perg2:
				
				# Print mostrando o número menor
				print("\033[1;31mO número\033[m \033[4;1m{}\033[m \033[1;31mé o menor.\033[m".format(perg3))
				
				# Print com espaço
				print(" ")
				
				# Sleep (2)
				sleep(2)
			
			# Print mostrando a soma entre as varíaveis		
				print("\033[4;1;32mA soma de\033[m \033[4;1m{}\033[m \033[4;1;32me\033[m \033[1;4m{}\033[m \033[4;32;1mé\033[m \033[1;4m{}\033[m".format(perg2, perg3, calc))
			
			# Print com espaço
				print(" ")
			
			# Sleep (2)
				sleep(2)
			
			# Print mostrando a média
				print("\033[4;1;32mA média é\033[m \033[1;4m{}\033[m".format(calc2))
			
			# Print com espaço
				print(" ")
			
			# Sleep (2)
				sleep(2)
		
	# Elif 4
	elif perg == "N":
				
				# Print com encerramento
				print("\033[1;31mEncerrando...\033[m")
				
				# Sleep (2)
				sleep(2)
				
				# Break
				break
