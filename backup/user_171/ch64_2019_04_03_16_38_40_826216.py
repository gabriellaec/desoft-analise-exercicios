def nome_usuario(x):
    x= "usuario@insper.edu.br"
    i=0
    arrobobas = -1
    while i<len(x):
        if x[i]=='@':
        	arrobobas = i
        i+=1
    cont=0
    nome="" 
    while cont<arrobobas:
        nome+=x[cont]
        cont+=1
 	return nome
