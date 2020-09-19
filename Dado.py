# O Script será um jogo nomeado como dado. Um dado comum possuí 6 números, o usuário irá escolher se quer jogar em 1 pessoa ou em 2 pessoas. Cujo o número escolhido por um usuário ou dois o Script irá gerar um número aleatório e irá mostrar o número que caiu.

# Importar módulos
from random import randint
from time import sleep

# Def com menu
def menu ():
	print('''
\033[32m[1]\033[m Solo
\033[32m[2]\033[m Duo''')

# While True para ir rodando o Script em quanto for verdadeiro 
while True:
	
	# Variável que irá perguntar se o usuário deseja iniciar o jogo
	perg = input("\033[1mDeseja iniciar o jogo? \033[m(y/n): "). strip().upper()
	print(" ")
	sleep(0.4)
	
	# Berfucação de If
	if perg == "Y":
		
		# Print de inicialização
		print("\033[1;32mIniciando...\033[m")
		sleep(1)
		print(" ")
		
		# Variável que irá perguntar se ele quer jogar sozinho ou multiplayer
		print("\033[1mDeseja jogar solo ou duo?\033[m", end = " ")
		menu_um = menu()
		perg3 = input(": ")
		sleep(0.7)
		print(" ")
		
		# Berfucação para analisar resposta 
		if perg3 == "1":
			
			# Print avisando que o usuário iniciou o jogo em modo solo
			print("\033[1;32mModo solo selecionado...\033[m")
			print(" ")
			
			# Variável que irá gerar um número de 1 a 6
			gerador = randint(1, 6)
			
			# Variável que irá perguntar um número do usuário
			perg4 = int(input("\033[1mEscolha um número de \033[1;4m1\033[m a \033[1;4m6\033[m:\033[m "))
			
			# Print de carregamento
			print("\033[32;1m...\033[m")
			sleep(0.7)
			print("\033[1mO número escolhido foi:\033[m")
			sleep(0.4)
			print(gerador)
			
			# If que irá analisar se o número digitado foi igual ao número gerado
			if perg4 == gerador:
				
				# Se for igual mostra que o usuário acertou
				print("\033[32;1;4mVocê ganhou!\033[m")
				sleep(1)
				print(" ")
			
			else:
				
				# Se o usuário errou irá mostrar que ele perdeu 
				print("\033[31;1;4mVocê errou!\033[m")
				sleep(1)
				print(" ")
				
		elif perg3 == "2":
			
			# Print avisando que o usuário iniciou o jogo em modo duo
			print("\033[1;32mModo duo selecionado...\033[m")
			print(" ")
			
			# Variável que irá gerar um número de 1 a 6
			gerador2 = randint(1, 6)
			
			# Variável que irá perguntar o número dos usuários
			perg5 = int(input("\033[1mPlayer \033[4;32m1\033[m Digite um número de \033[1;4m1\033[m a \033[1;4m6:\033[m "))
			sleep(0.5)
			perg6 = int(input("\033[1mPlayer \033[4;31m2\033[m Digite um número: "))
			
			# Print de carregamento
			print("\033[32;1m...\033[m")
			sleep(0.7)
			print("\033[1mO número escolhido foi:\033[m")
			sleep(0.4)
			print(gerador2)
			
			# If que irá analisar se o número foi digitado foi igual ao número gerado
			if perg5 == gerador2:
				
				# Se o player 1 acertou mostre que ele ganhou
				print("\033[32;4;1mO Player 1 Ganhou!\033[m")
				sleep(1)
				print(" ")
				
			elif perg6 == gerador2:
				
				# Se o player 2 acertou mostre que ele ganhou
				print("\033[32;4;1mO Player 2 Ganhou!\033[m")
				sleep(1)
				print(" ")
			
			else:
				
				# Se não o jogo ganhou
				print("\033[4;32mO jogo Ganhou!\033[m")
				sleep(1)
				print(" ")
				
		else:
			
			# Print avisando que o Script não entendeu a resposta
			print("\033[1;41mNão foi possível entender!\033[m")
			print(" ")
		
	elif perg == "N":
		print("\033[1;31mEncerrando...\033[m")
		sleep(1)
		break
	
	else:
		print("\033[1;41mNão foi possível entender!\033[m")
		print(" ")	
