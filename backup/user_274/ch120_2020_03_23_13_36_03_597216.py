import random
d = 100
bet = int(input("Quanto você quer apostar? "))

while bet != 0:
    type = input("Aposta em número ou paridade? ")
    if type == "n":
        num = int(input("Escolha um número. "))
    elif type == "p":
        pari = input("Par ou ímpar? ")
        
    i = random.randint(0,36)
    
    if type == "n":
    	if num == i:
        	d = d + bet*35
    	else:
        	d = d - bet
    elif type == "p":
        if i % 2 == 0:
            if pari == "p":
                d = d + bet
            elif pari == "i":
                d = d - bet
        else:
            if pari == "p":
                d = d - bet
            elif pari == "i":
                d = d + bet
    bet = int(input("Quanto você quer apostar? "))