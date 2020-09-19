# Python 3.8.3

# Bibliotecas usadas.
from random import randint
from time import sleep

# Print com loop de carregamento.
print("\033[1;32mCarregando...\033[m")
sleep(3)

# Definir varíavel com o randint.
valor = int(randint(0, 10))

# While True com ifs.
while True:
	
	perg_1 = str(input("Deseja iniciar o jogo? (y/n) ")).strip().		upper()
	
	if perg_1 == "Y":
		perg_2 = str(input("Antes de iniciar, deseja saber como o jogo funciona? (y/n) ")).strip().upper()
		
		if perg_2 == "Y":
			perg_3 = str(input("\033[1;32mO jogo irá gerar um número aleatório de 1 a 10. Seu objetivo é achar o número gerado. Se entendeu digite y para prosseguir ou n para repetir. (y/n) \033[m")).strip().upper()
			
			if perg_3 == "Y":
				
				perg_4 = int(input("Digite um número: "))
				
				if perg_4 < valor:
					print("\033[1;4mNúmero muito baixo.\033[m")
				
				elif perg_4 > valor:
					print("\033[1;4mNúmero muito alto.\033[m")
					
				elif perg_4 == valor:
					print("\033[1;32mVocê ganhou!\033[m")
					break
				
			elif perg_3 == "N":
					print("\033[1;32mO jogo irá gerar um número aleatório de 1 a 10. Seu objetivo é achar o número gerado.\033[m")
					sleep(3)
	
		elif perg_2 == "N":
			perg_5 = int(input("Digite um número: "))
			
			if perg_5 < valor:
				print("\033[1;4mNúmero muito baixo.\033[m")
			
			elif perg_5 > valor:
				print("\033[1;4mNúmero muito alto.\033[m")
			
			elif perg_5 == valor:
				print("\033[1;32mVocê ganhou!\033[m")
				break
				
	elif perg_1 == "N":
		print("\033[1;31mEncerrando...\033[m")
		sleep(3)
		break
