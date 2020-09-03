from time import sleep

print("{:=^77}".format("="))
print("{:=^84}".format(" \033[1mConversor de dias\033[m "))
print("{:=^77}".format("="))
print(" ")
perg = input("\033[1mDeseja iniciar?\033[m (y/n): ").strip().upper()
print(" ")
if perg == "Y":
	
	print("\033[1;32mIniciando...\033[m")
	sleep(2)
	
	while True:
		print(" ")
		perg2 = int(input("\033[1mDigite o dia:\033[m "))
		
		print(" ")
		calc = perg2 *24
		calc2 = perg2 *1440
		
		print("\033[32;1mConvertendo...\033[m")
		sleep(2)
		print(" ")
		print("O dia \033[4;32m{}\033[m foi convertido para \033[4;32m{}\033[m  Horas, e \033[4;32m{}\033[m Minutos".format(perg2, calc, calc2))
		print(" ")
		perg3 = input("\033[1mDeseja iniciar novamente?\033[m (y/n): ").strip().upper()
		
		if perg3 == "Y":
			
				while True:
					print(" ")
					perg2 = int(input("\033[1mDigite o dia:\033[m "))
					print(" ")
					calc = perg2 *24
					calc2 = perg2 *1440
					
					print("\033[32;1mConvertendo...\033[m")
					sleep(2)
					print(" ")
					print("O dia \033[4;32m{}\033[m foi convertido para \033[4;32m{}\033[m Horas, e \033[4;32m{}\033[m Minutos".format(perg2, calc, calc2))
					print(" ")
					perg4 = input("\033[1mDeseja iniciar novamente?\033[m (y/n): ").strip().upper()
					
					if perg4 == "Y":
			
							while True:
								print(" ")
								perg2 = int(input("\033[1mDigite o dia:\033[m "))
								print(" ")
								calc = perg2 *24
								calc2 = perg2 *1440
								print("\033[32;1mConvertendo...\033[m")
								sleep(2)
								print(" ")
								print("O dia \033[4;32m{}\033[m foi convertido para \033[4;32m{}\033[m Horas, e \033[4;32m{}\033[m  Minutos".format(perg2, calc, calc2))
								print(" ")
								perg5 = input("\033[1mDeseja iniciar novamente? (y/n): ").strip().upper()
								
								if perg5 == "Y":
									
													while True:
														print(" ")
														perg2 =int(input("\033[1mDigite o dia:\033[m "))
														print(" ")
														calc = perg2 *24
														calc2 = perg2 *1440
														print("\033[32;1mConvertendo...\033[m")
														sleep(2)
														print(" ")
														print("O dia {} foi convertido para {} Horas, e {} Minutos".format(perg2, calc, calc2))
								
								elif perg5 == "N":
							  			print('\033[1;31mEncerrando...\033[m"')
							  			sleep(2)
							  			break
					elif perg4 == "N":
								print("\033[1;31mEncerrando...\033[m")
								sleep(2)
								break
		
		elif perg3 == "N":
			print("\033[1;31mEncerrando...\033[m")
			sleep(2)
			break
			
elif perg == "N":
		print("\033[1;31mEncerrando...\033[m")
		sleep(2)
