
lista=[]
for i in range(0,10):
    x=random.randint(0,10)
    lista.append(x)
def verifica_progressao():
	if lista[10]-lista[0]==10:
        return "PA"
	elif lista[0]/lista[10]>1:
        return "PG"
	else:
        return "AG"
	return verifica_progressao
    