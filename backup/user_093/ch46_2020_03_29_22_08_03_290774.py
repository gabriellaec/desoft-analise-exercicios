list =[0,1,3,3]
lista =[ ]
def numero_no_indice(list):
	lista =[]
	if list[0]==0:
		lista.append(list[0])
	elif list[1]==1:
		lista.append(list[1])
	elif list[2]==2:
		lista.append(list[2])
	elif list[3]==3:
		lista.append(lista[3])
	else:
		return False
    
print(len(lista))