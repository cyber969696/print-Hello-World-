from time import sleep

while True:
	
	perg = input("\033[1mDeseja iniciar? (y/n) \033[m ").strip().upper()
	
	if perg == "Y":
		
		print("\033[4;1;32mIniciando...\033[m")
		sleep(2)
		
		perg2 = input("Digite o nome do aluno: ")
		sleep(1)
		
		perg3 = float(input("Digite a primeira nota de {}: ".format(perg2)))
		sleep(1)
		
		perg4 = float(input("Digite a segunda nota: "))
		
		
		calc = (perg3) + (perg4) /2
		
		print("\033[4;1;32mCalculando...\033[m")
		sleep(1)
		
		if calc < 5.0:
			
			print("O aluno {} foi \033[31;4;1mReprovado!\033[m".format(perg2))
			
		elif calc == 5.0 and 6.9:
			
			print("O aluno {} está de \033[7;30mRecuperação!\033[m".format(perg2))
			
		elif calc >= 7.0:
			
			print("O aluno {} foi \033[32;1;4mAprovado!\033[m".format(perg2))
		
		else:
			
			print("\033[4;1;31mNão foi possível prosseguir!\033[m")
			
	elif perg == "N":
			
			print("\033[1;4;31mEncerrando...\033[m")
			sleep(2)
			break
			
	else:
			
			print("\033[1;4;31mNão foi possível prosseguit!\033[m")
			
			
