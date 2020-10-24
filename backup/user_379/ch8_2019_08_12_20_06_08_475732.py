
lista=[]
for i in range(0,10):
    x=random.randint(0,10)
    lista.append(x)
def verifica_progressao():
	if lista[10]-lista[0]==10:
        print("PA")
	elif lista[0]/lista[10]>1:
        print("PG")
	else:
        print("AG")
	return verifica_progressao
    