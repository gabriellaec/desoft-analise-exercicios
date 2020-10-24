def eh_primo():
    b = True
    while b:
        numero = int(input("Digite Um Numero Par:"))
        if numero % 2 == 0:
        	b = False
    	else:
            print("Tente Novamente")
            return numero
        
print("Very Nice")
