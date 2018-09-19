from random import randint


import os

#il codice è lungo ma tutto uguale
#Programma sorteggi torneo con squadre ICC



print("International Champions Cup, fasi finali")
squadre=["Tottenham", "Arsenal", "Inter", "Borussia Dortmund", "Liverpool", "Real Madrid", "Juventus", "Chelsea"]
print(squadre)

player=input("Scegli una squadra inserendo il numero nella lista: ")
player=int(player)

if player==1:
	
	team=squadre[0]
	print("Sarai il Tottenham")
	scelta=input("Sei sicuro?  ")
	scelta=scelta.lower()
	if scelta=="si":
		print("Procediamo")
	elif scelta=="no":
		print("Ricomincia")
		exit()
	else:
		print(scelta+" non è una risposta seria")
		exit()

elif player==2:
	
	team=squadre[1]
	print("Sarai l'Arsenal")
	scelta=input("Sei sicuro?  ")
	scelta=scelta.lower()
	if scelta=="si":
		print("Procediamo")
	elif scelta=="no":
		print("Ricomincia")
		exit()
	else:
		print(scelta+" non è una risposta seria")
		exit()


elif player==3:

	team=squadre[2]
	print("Sarai l'Inter")
	scelta=input("Sei sicuro?  ")
	scelta=scelta.lower()
	if scelta=="si":
		print("Procediamo")
	elif scelta=="no":
		print("Ricomincia")
		exit()
	else:
		print(scelta+" non è una risposta seria")
		exit()


elif player==4:
	team=squadre[3]
	print("Sarai il Borussia Dortmund")
	scelta=input("Sei sicuro?  ")
	scelta=scelta.lower()
	if scelta=="si":
		print("Procediamo")
	elif scelta=="no":
		print("Ricomincia")
		exit()
	else:
		print(scelta+" non è una risposta seria")
		exit()

	
elif player==5:
	team=squadre[4]
	print("Sarai il Liverpool")
	scelta=input("Sei sicuro?  ")
	scelta=scelta.lower()
	if scelta=="si":
		print("Procediamo")
	elif scelta=="no":
		print("Ricomincia")
		exit()
	else:
		print(scelta+" non è una risposta seria")
		exit()

	
elif player==6:
	team=squadre[5]
	print("Sarai il Real Madrid")
	scelta=input("Sei sicuro?  ")
	scelta=scelta.lower()
	if scelta=="si":
		print("Procediamo")
	elif scelta=="no":
		print("Ricomincia")
		exit()
	else:
		print(scelta+" non è una risposta seria")
		exit()

	
elif player==7:
	team=squadre[6]
	print("Sarai la Juventus")
	scelta=input("Sei sicuro?  ")
	scelta=scelta.lower()
	if scelta=="si":
		print("Procediamo")
	elif scelta=="no":
		print("Ricomincia")
		exit()
	else:
		print(scelta+" non è una risposta seria")
		exit()

	
elif player==8 :
	team=squadre[7]
	print(" Sarai il Chelsea")
	scelta=input("Sei sicuro?  ")
	scelta=scelta.lower()
	if scelta=="si":
		print("Procediamo")
	elif scelta=="no":
		print("Ricomincia")
		exit()
	else:
		print(scelta+" non è una risposta seria")
	exit()


os.system("cls")


if team==squadre[0]: #Tottenham
	print("Primo incontro tra Arsenal e Borussia Dortmund")
	print("Secondo incontro tra Tottenham e  Inter")
	print("Terzo incontro tra Real Madrid e Chelsea")
	print("Quarto incontro tra Liverpool e Juventus")
	print()
	bet=input("Vuoi scommettere sul vincitore del torneo? (ricorda lettera maiuscola) ")
	a=randint(1,2)
	b=randint(1,2)
	c=randint(1,2)
	d=randint(1,2)
	x=randint(1,7)
	print()
	print()
	print()
	print()
	print()



	if a==1:
		print("Il vincitore è l'Arsenal")
		vincitore1="Arsenal"
	elif a==2:
		print("Il vincitore è il Borussia Dortmund")
		vincitore1="Borussia Dortmund"
	
	if b==1:
		print("Il vincitore è il Liverpool")
		vincitore4= "Liverpool"
	elif b==2:
		print("Il vincitore è la Juventus")
		vincitore4= "Juventus"
	
	if c==1:
		print("Il vincitore è Il Real Madrid")
		vincitore3= "Real Madrid"
	elif c==2:
		print("Il vincitore è il Chelsea")
		vincitore3= "Chelsea"
	
	if d==1:
		print("Il vincitore è il Tottenham")
		print("Complimenti la tua squadra è passata")
		vincitore2="Tottenham"
	
	elif d==2:
		print("Il vincitore è l'Inter")
		print("Peccato, hai perso...ritenta")
		if x==1:
			print("Il vincitore del torneo è "+ vincitore1 )
			if bet==vincitore1:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore1:
				print("Non hai vinto la scommessa")
				exit()
			
			
		
		elif x==2:
			print("Il vincitore del torneo è "+ vincitore3)
			if bet==vincitore3:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore3:
				print("Non hai vinto la scommessa")
				exit()
		elif x==3:
			print("Il vincitore del torneo è "+ vincitore4)
			if bet==vincitore4:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore4:
				print("Non hai vinto la scommessa")
				exit()

		elif x==4:
			print("Il vincitore del torneo è l'Inter")
			if bet=="Inter":
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!="Inter":
				print("Non hai vinto la scommessa")
				exit()


	
	print()
	print()
	print()
	print()


	vincitori=[]
	vincitori.append(vincitore1)
	vincitori.append(vincitore2)
	vincitori.append(vincitore3)
	vincitori.append(vincitore4)

	print("Squadre vincitrici:")
	print()
	print(vincitori)
	print()
	print()

	print("Secondo incontro tra "+ vincitore1+ " e "+ vincitore2)
	print("Secondo incontro tra "+ vincitore3+ " e "+ vincitore4)
	print()
	print()

	o=randint(1,2)
	m=randint(1,2)
	l=randint(1,3)
	vincitori2=[]
	if o==1:
		print("Il vincitore è "+ vincitore1)
		vincitori2.append(vincitore1)
		print("Peccato, c'eri quasi")
		if l==1:
			print("Il vincitore del torneo è "+ vincitore1)
			if bet==vincitore1:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore1:
				print("Non hai vinto la scommessa")
			exit()
		elif l==2:
			print("Il vincitore del torneo è "+ vincitore3)
			if bet==vincitore3:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore3:
				print("Non hai vinto la scommessa")
			exit()
		elif l==3:
			print("Il vincitore del torneo è "+ vincitore4)
			if bet==vincitore4:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore4:
				print("Non hai vinto la scommessa")
			exit()


	elif o==2:
		print("Il vincitore è "+ vincitore2)
		vincitori2.append(vincitore2)
		print("Complimenti, sei in finale")

	print()


	if m==1:
		print("Il vincitore è "+ vincitore3)
		vincitori2.append(vincitore3)
	elif m==2:
		print("Il vincitore è "+ vincitore4)
		vincitori2.append(vincitore4)

	vu=input("Premi invio per continuare")
	os.system("cls")
	
	print()
	print("Finalisti:")
	print()
	print(vincitori2)
	print()
	cuz=randint(1,2)
	if cuz==1:
		print("Il vincitore del torneo è "+ vincitori2[0])
		print()
		print()
		print("COMPLIMENTI, HAI VINTO IL TORNEO E HAI VINTO IL GIOCO!!!")
		if bet==vincitori2[0]:
				print("HAI ANCHE VINTO LA SCOMMESSA!")
		elif bet!=vincitori2[0]:
			print("Però non hai vinto la scommessa")
	elif cuz==2:
		print("Il vincitore del torneo è "+ vincitori2[1])
		print()
		print()
		print("Peccato, avevi quasi vinto!! Spero che il gioco ti sia piaciuto")
		if bet==vincitori2[1]:
				print("Almeno hai vinto la scommessa!!")
		elif bet!=vincitori2[1]:
			print("Peccato, non ha vinto neanche la scommessa")
		print()
		print("TRY AGAIN")






















elif team==squadre[1]: #Arsenal
	print("Primo incontro tra  Tottenham e Borussia Dortmund")
	print("Secondo incontro tra  Arsenal e  Chelsea")
	print("Terzo incontro tra Liverpool e Inter")
	print("Quarto incontro tra  Real Madrid e Juventus")
	
	bet=input("Vuoi scommettere sul vincitore del torneo? (ricorda lettera maiuscola) ")
	
	a=randint(1,2)
	b=randint(1,2)
	c=randint(1,2)
	d=randint(1,2)
	x=randint(1,7)
	print()
	print()
	print()
	print()
	print()



	if a==1:
		print("Il vincitore è il Tottenham")
		vincitore1="Tottenham"
	elif a==2:
		print("Il vincitore è il Borussia Dortmund")
		vincitore1="Borussia Dortmund"
	
	if b==1:
		print("Il vincitore è il Liverpool")
		vincitore4= "Liverpool"
	elif b==2:
		print("Il vincitore è l'Inter ")
		vincitore4= "Inter"
	
	if c==1:
		print("Il vincitore è Il Real Madrid")
		vincitore3= "Real Madrid"
	elif c==2:
		print("Il vincitore è la Juventus")
		vincitore3= "Juventus"
	
	if d==1:
		print("Il vincitore è l'Arsenal")
		print("Complimenti la tua squadra è passata")
		vincitore2="Arsenal"
	
	elif d==2:
		print("Il vincitore è il Chelsea")
		print("Peccato, hai perso...ritenta")
		if x==1:
			print("Il vincitore del torneo è "+ vincitore1 )
			if bet==vincitore1:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore1:
				print("Non hai vinto la scommessa")
				exit()
			
			
		
		elif x==2:
			print("Il vincitore del torneo è "+ vincitore3)
			if bet==vincitore3:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore3:
				print("Non hai vinto la scommessa")
				exit()
		elif x==3:
			print("Il vincitore del torneo è "+ vincitore4)
			if bet==vincitore4:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore4:
				print("Non hai vinto la scommessa")
				exit()

		elif x==4:
			print("Il vincitore del torneo è l'Inter")
			if bet=="Inter":
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!="Inter":
				print("Non hai vinto la scommessa")
				exit()


	
	print()
	print()
	print()
	print()


	vincitori=[]
	vincitori.append(vincitore1)
	vincitori.append(vincitore2)
	vincitori.append(vincitore3)
	vincitori.append(vincitore4)

	print("Squadre vincitrici:")
	print()
	print(vincitori)
	print()
	print()

	print("Secondo incontro tra "+ vincitore1+ " e "+ vincitore2)
	print("Secondo incontro tra "+ vincitore3+ " e "+ vincitore4)
	print()
	print()

	o=randint(1,2)
	m=randint(1,2)
	l=randint(1,3)
	vincitori2=[]
	if o==1:
		print("Il vincitore è "+ vincitore1)
		vincitori2.append(vincitore1)
		print("Peccato, c'eri quasi")
		if l==1:
			print("Il vincitore del torneo è "+ vincitore1)
			if bet==vincitore1:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore1:
				print("Non hai vinto la scommessa")
			exit()
		elif l==2:
			print("Il vincitore del torneo è "+ vincitore3)
			if bet==vincitore3:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore3:
				print("Non hai vinto la scommessa")
			exit()
		elif l==3:
			print("Il vincitore del torneo è "+ vincitore4)
			if bet==vincitore4:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore4:
				print("Non hai vinto la scommessa")
			exit()


	elif o==2:
		print("Il vincitore è "+ vincitore2)
		vincitori2.append(vincitore2)
		print("Complimenti, sei in finale")

	print()


	if m==1:
		print("Il vincitore è "+ vincitore3)
		vincitori2.append(vincitore3)
	elif m==2:
		print("Il vincitore è "+ vincitore4)
		vincitori2.append(vincitore4)

	vu=input("Premi invio per continuare")
	os.system("cls")
	
	print()
	print("Finalisti:")
	print()
	print(vincitori2)
	print()
	cuz=randint(1,2)
	if cuz==1:
		print("Il vincitore del torneo è "+ vincitori2[0])
		print()
		print()
		print("COMPLIMENTI, HAI VINTO IL TORNEO E HAI VINTO IL GIOCO!!!")
		if bet==vincitori2[0]:
				print("HAI ANCHE VINTO LA SCOMMESSA!")
		elif bet!=vincitori2[0]:
			print("Però non hai vinto la scommessa")
	elif cuz==2:
		print("Il vincitore del torneo è "+ vincitori2[1])
		print()
		print()
		print("Peccato, avevi quasi vinto!! Spero che il gioco ti sia piaciuto")
		if bet==vincitori2[1]:
				print("Almeno hai vinto la scommessa!!")
		elif bet!=vincitori2[1]:
			print("Peccato, non ha vinto neanche la scommessa")
		print()
		print("TRY AGAIN")
	




elif team==squadre[2]: #Inter
	print("Primo incontro tra  Tottenham e Borussia Dortmund")
	print("Secondo incontro tra  Juventus e Arsenal")
	print("Terzo incontro tra Real Madrid e Liverpool ")
	print("Quarto incontro tra  Chelsea e Inter ")
	bet=input("Vuoi scommettere sul vincitore del torneo? (ricorda lettera maiuscola) ")
	
	a=randint(1,2)
	b=randint(1,2)
	c=randint(1,2)
	d=randint(1,2)
	x=randint(1,7)
	print()
	print()
	print()
	print()
	print()



	if a==1:
		print("Il vincitore è il Tottenham")
		vincitore1="Tottenham"
	elif a==2:
		print("Il vincitore è il Borussia Dortmund")
		vincitore1="Borussia Dortmund"
	
	if b==1:
		print("Il vincitore è il Liverpool")
		vincitore4= "Liverpool"
	elif b==2:
		print("Il vincitore è il Real Madrid")
		vincitore4= "Real Madrid"
	
	if c==1:
		print("Il vincitore è l'Arsenal")
		vincitore3= "Arsenal"
	elif c==2:
		print("Il vincitore è la Juventus")
		vincitore3= "Juventus"
	
	if d==1:
		print("Il vincitore è l'Inter")
		print("Complimenti la tua squadra è passata")
		vincitore2="Inter"
	
	elif d==2:
		print("Il vincitore è il Chelsea")
		print("Peccato, hai perso...ritenta")
		if x==1:
			print("Il vincitore del torneo è "+ vincitore1 )
			if bet==vincitore1:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore1:
				print("Non hai vinto la scommessa")
				exit()
			
			
		
		elif x==2:
			print("Il vincitore del torneo è "+ vincitore3)
			if bet==vincitore3:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore3:
				print("Non hai vinto la scommessa")
				exit()
		elif x==3:
			print("Il vincitore del torneo è "+ vincitore4)
			if bet==vincitore4:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore4:
				print("Non hai vinto la scommessa")
				exit()

		elif x==4:
			print("Il vincitore del torneo è il Chelsea")
			if bet=="Chelsea":
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!="Chelsea":
				print("Non hai vinto la scommessa")
				exit()


	
	print()
	print()
	print()
	print()


	vincitori=[]
	vincitori.append(vincitore1)
	vincitori.append(vincitore2)
	vincitori.append(vincitore3)
	vincitori.append(vincitore4)

	print("Squadre vincitrici:")
	print()
	print(vincitori)
	print()
	print()

	print("Secondo incontro tra "+ vincitore1+ " e "+ vincitore2)
	print("Secondo incontro tra "+ vincitore3+ " e "+ vincitore4)
	print()
	print()

	o=randint(1,2)
	m=randint(1,2)
	l=randint(1,3)
	vincitori2=[]
	if o==1:
		print("Il vincitore è "+ vincitore1)
		vincitori2.append(vincitore1)
		print("Peccato, c'eri quasi")
		if l==1:
			print("Il vincitore del torneo è "+ vincitore1)
			if bet==vincitore1:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore1:
				print("Non hai vinto la scommessa")
			exit()
		elif l==2:
			print("Il vincitore del torneo è "+ vincitore3)
			if bet==vincitore3:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore3:
				print("Non hai vinto la scommessa")
			exit()
		elif l==3:
			print("Il vincitore del torneo è "+ vincitore4)
			if bet==vincitore4:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore4:
				print("Non hai vinto la scommessa")
			exit()


	elif o==2:
		print("Il vincitore è "+ vincitore2)
		vincitori2.append(vincitore2)
		print("Complimenti, sei in finale")

	print()


	if m==1:
		print("Il vincitore è "+ vincitore3)
		vincitori2.append(vincitore3)
	elif m==2:
		print("Il vincitore è "+ vincitore4)
		vincitori2.append(vincitore4)

	vu=input("Premi invio per continuare")
	os.system("cls")
	
	print()
	print("Finalisti:")
	print()
	print(vincitori2)
	print()
	cuz=randint(1,2)
	if cuz==1:
		print("Il vincitore del torneo è "+ vincitori2[0])
		print()
		print()
		print("COMPLIMENTI, HAI VINTO IL TORNEO E HAI VINTO IL GIOCO!!!")
		if bet==vincitori2[0]:
				print("HAI ANCHE VINTO LA SCOMMESSA!")
		elif bet!=vincitori2[0]:
			print("Però non hai vinto la scommessa")
	elif cuz==2:
		print("Il vincitore del torneo è "+ vincitori2[1])
		print()
		print()
		print("Peccato, avevi quasi vinto!! Spero che il gioco ti sia piaciuto")
		if bet==vincitori2[1]:
				print("Almeno hai vinto la scommessa!!")
		elif bet!=vincitori2[1]:
			print("Peccato, non ha vinto neanche la scommessa")
		print()
		print("TRY AGAIN")
	








	




elif team==squadre[3]: #Borussia Dortmund
	print("Primo incontro tra Real Madrid e Borussia Dortmund")
	print("Secondo incontro tra Tottenham e  Inter")
	print("Terzo incontro tra Juventus e Chelsea")
	print("Quarto incontro tra Liverpool e Arsenal")
	bet=input("Vuoi scommettere sul vincitore del torneo? (ricorda lettera maiuscola) ")
	a=randint(1,2)
	b=randint(1,2)
	c=randint(1,2)
	d=randint(1,2)
	x=randint(1,7)
	print()
	print()
	print()
	print()
	print()



	if a==1:
		print("Il vincitore è il Tottenham")
		vincitore1="Tottenham"
	elif a==2:
		print("Il vincitore è l' Inter")
		vincitore1="Inter"
	
	if b==1:
		print("Il vincitore è il Liverpool")
		vincitore4= "Liverpool"
	elif b==2:
		print("Il vincitore è l'Arsenal ")
		vincitore4= "Arsenal"
	
	if c==1:
		print("Il vincitore è il Chelsea")
		vincitore3= "Chelsea"
	elif c==2:
		print("Il vincitore è la Juventus")
		vincitore3= "Juventus"
	
	if d==1:
		print("Il vincitore è il Borussia Dortmund")
		print("Complimenti la tua squadra è passata")
		vincitore2="Borussia Dortmund"
	
	elif d==2:
		print("Il vincitore è il Real Madrid")
		print("Peccato, hai perso...ritenta")
		if x==1:
			print("Il vincitore del torneo è "+ vincitore1 )
			if bet==vincitore1:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore1:
				print("Non hai vinto la scommessa")
				exit()
			
			
		
		elif x==2:
			print("Il vincitore del torneo è "+ vincitore3)
			if bet==vincitore3:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore3:
				print("Non hai vinto la scommessa")
				exit()
		elif x==3:
			print("Il vincitore del torneo è "+ vincitore4)
			if bet==vincitore4:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore4:
				print("Non hai vinto la scommessa")
				exit()

		elif x==4:
			print("Il vincitore del torneo è il Real Madrid")
			if bet=="Real Madrid":
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!="Real Madrid":
				print("Non hai vinto la scommessa")
				exit()


	
	print()
	print()
	print()
	print()


	vincitori=[]
	vincitori.append(vincitore1)
	vincitori.append(vincitore2)
	vincitori.append(vincitore3)
	vincitori.append(vincitore4)

	print("Squadre vincitrici:")
	print()
	print(vincitori)
	print()
	print()

	print("Secondo incontro tra "+ vincitore1+ " e "+ vincitore2)
	print("Secondo incontro tra "+ vincitore3+ " e "+ vincitore4)
	print()
	print()

	o=randint(1,2)
	m=randint(1,2)
	l=randint(1,3)
	vincitori2=[]
	if o==1:
		print("Il vincitore è "+ vincitore1)
		vincitori2.append(vincitore1)
		print("Peccato, c'eri quasi")
		if l==1:
			print("Il vincitore del torneo è "+ vincitore1)
			if bet==vincitore1:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore1:
				print("Non hai vinto la scommessa")
			exit()
		elif l==2:
			print("Il vincitore del torneo è "+ vincitore3)
			if bet==vincitore3:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore3:
				print("Non hai vinto la scommessa")
			exit()
		elif l==3:
			print("Il vincitore del torneo è "+ vincitore4)
			if bet==vincitore4:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore4:
				print("Non hai vinto la scommessa")
			exit()


	elif o==2:
		print("Il vincitore è "+ vincitore2)
		vincitori2.append(vincitore2)
		print("Complimenti, sei in finale")

	print()


	if m==1:
		print("Il vincitore è "+ vincitore3)
		vincitori2.append(vincitore3)
	elif m==2:
		print("Il vincitore è "+ vincitore4)
		vincitori2.append(vincitore4)

	vu=input("Premi invio per continuare")
	os.system("cls")
	
	print()
	print("Finalisti:")
	print()
	print(vincitori2)
	print()
	cuz=randint(1,2)
	if cuz==1:
		print("Il vincitore del torneo è "+ vincitori2[0])
		print()
		print()
		print("COMPLIMENTI, HAI VINTO IL TORNEO E HAI VINTO IL GIOCO!!!")
		if bet==vincitori2[0]:
				print("HAI ANCHE VINTO LA SCOMMESSA!")
		elif bet!=vincitori2[0]:
			print("Però non hai vinto la scommessa")
	elif cuz==2:
		print("Il vincitore del torneo è "+ vincitori2[1])
		print()
		print()
		print("Peccato, avevi quasi vinto!! Spero che il gioco ti sia piaciuto")
		if bet==vincitori2[1]:
				print("Almeno hai vinto la scommessa!!")
		elif bet!=vincitori2[1]:
			print("Peccato, non ha vinto neanche la scommessa")
		print()
		print("TRY AGAIN")




elif team==squadre[4]: #Liverpool
	print("Primo incontro tra Arsenal e Liverpool")
	print("Secondo incontro tra  Chelsea e  Inter")
	print("Terzo incontro tra Real Madrid e Tottenham ")
	print("Quarto incontro tra Borussia Dortmund e Juventus")
	bet=input("Vuoi scommettere sul vincitore del torneo? (ricorda lettera maiuscola) ")
	a=randint(1,2)
	b=randint(1,2)
	c=randint(1,2)
	d=randint(1,2)
	x=randint(1,7)
	print()
	print()
	print()
	print()
	print()



	if a==1:
		print("Il vincitore è il Tottenham")
		vincitore1="Tottenham"
	elif a==2:
		print("Il vincitore è il Real Madrid")
		vincitore1="Real Madrid"
	
	if b==1:
		print("Il vincitore è il Chelsea")
		vincitore4= "Chelsea"
	elif b==2:
		print("Il vincitore è l'Inter ")
		vincitore4= "Inter"
	
	if c==1:
		print("Il vincitore è il Borussia Dortmund")
		vincitore3= "Borussia Dortmund"
	elif c==2:
		print("Il vincitore è la Juventus")
		vincitore3= "Juventus"
	
	if d==1:
		print("Il vincitore è il Liverpool")
		print("Complimenti la tua squadra è passata")
		vincitore2="Liverpool"
	
	elif d==2:
		print("Il vincitore è l'Arsenal")
		print("Peccato, hai perso...ritenta")
		if x==1:
			print("Il vincitore del torneo è "+ vincitore1 )
			if bet==vincitore1:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore1:
				print("Non hai vinto la scommessa")
				exit()
			
			
		
		elif x==2:
			print("Il vincitore del torneo è "+ vincitore3)
			if bet==vincitore3:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore3:
				print("Non hai vinto la scommessa")
				exit()
		elif x==3:
			print("Il vincitore del torneo è "+ vincitore4)
			if bet==vincitore4:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore4:
				print("Non hai vinto la scommessa")
				exit()

		elif x==4:
			print("Il vincitore del torneo è l'Arsenal")
			if bet=="Arsenal":
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!="Arsenal":
				print("Non hai vinto la scommessa")
				exit()


	
	print()
	print()
	print()
	print()


	vincitori=[]
	vincitori.append(vincitore1)
	vincitori.append(vincitore2)
	vincitori.append(vincitore3)
	vincitori.append(vincitore4)

	print("Squadre vincitrici:")
	print()
	print(vincitori)
	print()
	print()

	print("Secondo incontro tra "+ vincitore1+ " e "+ vincitore2)
	print("Secondo incontro tra "+ vincitore3+ " e "+ vincitore4)
	print()
	print()

	o=randint(1,2)
	m=randint(1,2)
	l=randint(1,3)
	vincitori2=[]
	if o==1:
		print("Il vincitore è "+ vincitore1)
		vincitori2.append(vincitore1)
		print("Peccato, c'eri quasi")
		if l==1:
			print("Il vincitore del torneo è "+ vincitore1)
			if bet==vincitore1:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore1:
				print("Non hai vinto la scommessa")
			exit()
		elif l==2:
			print("Il vincitore del torneo è "+ vincitore3)
			if bet==vincitore3:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore3:
				print("Non hai vinto la scommessa")
			exit()
		elif l==3:
			print("Il vincitore del torneo è "+ vincitore4)
			if bet==vincitore4:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore4:
				print("Non hai vinto la scommessa")
			exit()


	elif o==2:
		print("Il vincitore è "+ vincitore2)
		vincitori2.append(vincitore2)
		print("Complimenti, sei in finale")

	print()


	if m==1:
		print("Il vincitore è "+ vincitore3)
		vincitori2.append(vincitore3)
	elif m==2:
		print("Il vincitore è "+ vincitore4)
		vincitori2.append(vincitore4)

	vu=input("Premi invio per continuare")
	os.system("cls")
	
	print()
	print("Finalisti:")
	print()
	print(vincitori2)
	print()
	cuz=randint(1,2)
	if cuz==1:
		print("Il vincitore del torneo è "+ vincitori2[0])
		print()
		print()
		print("COMPLIMENTI, HAI VINTO IL TORNEO E HAI VINTO IL GIOCO!!!")
		if bet==vincitori2[0]:
				print("HAI ANCHE VINTO LA SCOMMESSA!")
		elif bet!=vincitori2[0]:
			print("Però non hai vinto la scommessa")
	elif cuz==2:
		print("Il vincitore del torneo è "+ vincitori2[1])
		print()
		print()
		print("Peccato, avevi quasi vinto!! Spero che il gioco ti sia piaciuto")
		if bet==vincitori2[1]:
				print("Almeno hai vinto la scommessa!!")
		elif bet!=vincitori2[1]:
			print("Peccato, non ha vinto neanche la scommessa")
		print()
		print("TRY AGAIN")




elif team==squadre[5]: #Real Madrid
	print("Primo incontro tra Arsenal e Inter ")
	print("Secondo incontro tra Tottenham e Borussia Dortmund")
	print("Terzo incontro tra Real Madrid e Juventus")
	print("Quarto incontro tra Liverpool e Chelsea")
	bet=input("Vuoi scommettere sul vincitore del torneo? (ricorda lettera maiuscola) ")
	a=randint(1,2)
	b=randint(1,2)
	c=randint(1,2)
	d=randint(1,2)
	x=randint(1,7)
	print()
	print()
	print()
	print()
	print()



	if a==1:
		print("Il vincitore è l'Arsenal")
		vincitore1="Arsenal"
	elif a==2:
		print("Il vincitore è l'Inter")
		vincitore1="Inter"
	
	if b==1:
		print("Il vincitore è il Tottenham")
		vincitore4= "Tottenham"
	elif b==2:
		print("Il vincitore è il Borussia Dortmund")
		vincitore4= "Borussia Dortmund"
	
	if c==1:
		print("Il vincitore è il Liverpool")
		vincitore3= "Liverpool"
	elif c==2:
		print("Il vincitore è il Chelsea")
		vincitore3= "Chelsea"
	
	if d==1:
		print("Il vincitore è il Real Madrid")
		print("Complimenti la tua squadra è passata")
		vincitore2="Real Madrid"
	
	elif d==2:
		print("Il vincitore è la Juventus")
		print("Peccato, hai perso...ritenta")
		if x==1:
			print("Il vincitore del torneo è "+ vincitore1 )
			if bet==vincitore1:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore1:
				print("Non hai vinto la scommessa")
				exit()
			
			
		
		elif x==2:
			print("Il vincitore del torneo è "+ vincitore3)
			if bet==vincitore3:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore3:
				print("Non hai vinto la scommessa")
				exit()
		elif x==3:
			print("Il vincitore del torneo è "+ vincitore4)
			if bet==vincitore4:
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!=vincitore4:
				print("Non hai vinto la scommessa")
				exit()

		elif x==4:
			print("Il vincitore del torneo è la Juventus")
			if bet=="Juventus":
				print("Almeno hai vinto la scommessa")
				exit()
			elif bet!="Juventus":
				print("Non hai vinto la scommessa")
				exit()


	
	print()
	print()
	print()
	print()


	vincitori=[]
	vincitori.append(vincitore1)
	vincitori.append(vincitore2)
	vincitori.append(vincitore3)
	vincitori.append(vincitore4)

	print("Squadre vincitrici:")
	print()
	print(vincitori)
	print()
	print()

	print("Secondo incontro tra "+ vincitore1+ " e "+ vincitore2)
	print("Secondo incontro tra "+ vincitore3+ " e "+ vincitore4)
	print()
	print()

	o=randint(1,2)
	m=randint(1,2)
	l=randint(1,3)
	vincitori2=[]
	if o==1:
		print("Il vincitore è "+ vincitore1)
		vincitori2.append(vincitore1)
		print("Peccato, c'eri quasi")
		if l==1:
			print("Il vincitore del torneo è "+ vincitore1)
			if bet==vincitore1:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore1:
				print("Non hai vinto la scommessa")
			exit()
		elif l==2:
			print("Il vincitore del torneo è "+ vincitore3)
			if bet==vincitore3:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore3:
				print("Non hai vinto la scommessa")
			exit()
		elif l==3:
			print("Il vincitore del torneo è "+ vincitore4)
			if bet==vincitore4:
				print("Almeno hai vinto la scommessa")
			elif bet!=vincitore4:
				print("Non hai vinto la scommessa")
			exit()


	elif o==2:
		print("Il vincitore è "+ vincitore2)
		vincitori2.append(vincitore2)
		print("Complimenti, sei in finale")

	print()


	if m==1:
		print("Il vincitore è "+ vincitore3)
		vincitori2.append(vincitore3)
	elif m==2:
		print("Il vincitore è "+ vincitore4)
		vincitori2.append(vincitore4)

	vu=input("Premi invio per continuare")
	os.system("cls")
	
	print()
	print("Finalisti:")
	print()
	print(vincitori2)
	print()
	cuz=randint(1,2)
	if cuz==1:
		print("Il vincitore del torneo è "+ vincitori2[0])
		print()
		print()
		print("COMPLIMENTI, HAI VINTO IL TORNEO E HAI VINTO IL GIOCO!!!")
		if bet==vincitori2[0]:
				print("HAI ANCHE VINTO LA SCOMMESSA!")
		elif bet!=vincitori2[0]:
			print("Però non hai vinto la scommessa")
	elif cuz==2:
		print("Il vincitore del torneo è "+ vincitori2[1])
		print()
		print()
		print("Peccato, avevi quasi vinto!! Spero che il gioco ti sia piaciuto")
		if bet==vincitori2[1]:
				print("Almeno hai vinto la scommessa!!")
		elif bet!=vincitori2[1]:
			print("Peccato, non ha vinto neanche la scommessa")
		print()
		print("TRY AGAIN")







elif team==squadre[6]:
	print("Primo incontro tra Arsenal e Real Madrid")
	print("Secondo incontro tra Tottenham e  Juventus")
	print("Terzo incontro tra Liverpool e Chelsea")
	print("Quarto incontro tra Borussia Dortmund e Inter")

elif team==squadre[7]:
	print("Primo incontro tra Tottenham e Real Madrid")
	print("Secondo incontro tra Liverpool e  Juventus")
	print("Terzo incontro tra Arsenal e Chelsea")
	print("Quarto incontro tra Borussia Dortmund e Inter")




