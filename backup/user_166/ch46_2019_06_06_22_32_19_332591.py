palavra= input("digite uma palavra")
lista=[]
contador=0
while palavra != "fim":
    if palavra not in lista:
        lista.append(palavra)
        palavra= input("digite uma palavra")
		if palavra[0] == "a":
         	print(palavra)
    
        
        