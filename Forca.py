#///////////////////////////////////////////////////////////////////
# Python 3.8.3 
# Script criado em 17/09/2020 as 20:20
# Desenvolvido por David Lins
# Link do Github: https://www.github.com/cyber969696/Beemo/tree/master/Beemo%201.0.py
# Script criado para estudo, com a função de treinar. Este código estará no meu Github, caso queira analísar outros projetos feitos por mim fique a vontade!
# Meio de contato: 
# Email: jamaicaserj@gmail.com
#Facebook: David lins
# Telefone: 11959723596
#///////////////////////////////////////////////////////////////////

# Importar módulos
import os
from time import sleep

# Função def que irá armazenar o código
def jogar ():
	
	# Lista com a palávra 
	palavra_secreta = ["P", "Y", "T", "H", "O", "N"]
	
	# Varíavel usada para o return final
	a = " "
	
	# Lista com todas as letras que for descoberta
	letras_descobertas = []
	
	# For que irá puxar a lista com a palávra
	for i in range(0, len(palavra_secreta)):
		
		# Lista com as letras descobertas irá receber um traço de acordo ao tamanho da palávra
		letras_descobertas.append("-")
	
	# Varíavel booleana False	
	acertou = False
	
	# Se varíavel booleana for False o while entra em loop
	while acertou == False:
		
		print(" ")
		
		# Varíavel que irá armazenar as letras digitadas pelo usúario
		letra = input("\033[1mDigite alguma letra\033[m: ").upper().strip()
		
		print(" ")
		
		# For puxando a palávra
		for i in range(0, len(palavra_secreta)):
			
			# If para verificar se a letra que o usúario digitou está na palávra
			if letra == palavra_secreta[i]:
				
				# Lista de letras descobertas irá receber a letra que o usúario digitou
				letras_descobertas[i] = letra
			
			sleep(0.1)
			
			# Mostrar a lista com as letras descobertas
			print(letras_descobertas[i])
		
		# Varíavel booleana irá se tornar True se tudo isso acíma for completada
		acertou = True
		
		# If que irá veríficar se a lista de letras descobertas está igual a palávra
		if letras_descobertas == palavra_secreta:
			print(" ")
			
			# Se estiver irá mostrar uma parabenização, com a palávra logo após
			print("\033[1;32mParabéns!\033[m \033[1mA palávra é\033[m: \033[4mPython\033[m")
		
		# For para puxar a lista de letras descobertas
		for x in range(0, len(letras_descobertas)):
			
			# Se está lista ainda tiver traços
			if letras_descobertas[x] == "-":
				
				# A varíavel booleana se tornará False novanente
				acertou = False
	
	# Return a para a finalização do Def
	return a
				
# While para dar inicialização ao programa, e chamar o Def		
while True:
	
	print(" ")
	
	# Varíavel que irá perguntar se o usúario deseja iniciar o programa
	perg = input("\033[1mDeseja jogar?\033[m (y/n): ").strip().upper()
	
	# Se a resposta for Y de Sim
	if perg == "Y":
		
		print(" ")
		
		# Print de inicialização
		print("\033[1;32mIniciando...\033[m")
		sleep(1.3)
		
		# O sistema irá dar um clear no código acíma
		os.system("clear")
		
		# Armazenar o Def em uma varíavel
		chama = jogar()
		
		# Chamar o Def
		print(chama)
	
	# Se for N de Não 
	elif perg == "N":
		
		print(" ")
		
		# Print com encerramento
		print("\033[1;31mEncerrando...\033[m")
		sleep(1.3)
		
		# O sistema irá limpar tudo acíma
		os.system("clear")
		
		# Logo após um Break para encerrar o loop
		break
		
	else:
		
		print(" ")
		
		# Print mostrando que o programa não entendeu a resposta
		print("\033[4;1mNão foi possível entender!\033[m")
		sleep(1)				
