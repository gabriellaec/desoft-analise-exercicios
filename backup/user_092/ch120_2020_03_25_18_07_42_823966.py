import random
dinheiro = 100
pode_apostar = True
while(pode_apostar == True):
    if dinheiro > 0:
    	print(dinheiro)
    	a = int(input('quanto quer apostar'))
    	if a != 0:
            b = input('numero ou par/impar')
            if b == 'n':
                n = random.randit(1,36)
                c = int(input('numero entre 1 e 36'))
                if c == n:
                	dinheiro += 35*a
                else:
                	dinheiro = dinheiro - a
            elif b == 'p':
                n = random.randit(0,36)
                p = n%2==0
                d = input('p ou i')
                if d == 'p':
                    if p == True:
                        dinheiro += a
                    else:
                        dinheiro = dinheiro - a
                else:
                    if p == False:
                        dinheiro += a
                    else:
                        dinheiro = dinheiro - a
    else:
        pode_apostar = False