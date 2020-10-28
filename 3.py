import random
import time

punts2=13
intents=0

numrange=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
symrange=["♥","♦","♣","♠"]

def carta():
	numcarta=numrange[num]
	symcarta=symrange[sym]
	print(numcarta,symcarta)

#	carta jugador
print("La teva carta es:")
num=random.randint(0,12)
sym=random.randint(0,3)
carta1=carta()
punts1=num

print("\nLa carta de la maquina es:")
while True:
	if punts1 == 0:
		print("no pots guanyar")
		break

	time.sleep(1)
	
	#	carta maquina
	num=random.randint(0,12)
	sym=random.randint(0,3)
	carta2=carta()
	punts2=num

	intents=intents+1

	if punts1 > punts2 and intents == 1:
		print("\nHas guanyat al primer intent")
		break
	elif punts1 > punts2:
		print("\nHas guanyat despres de",intents,"intents")
		break