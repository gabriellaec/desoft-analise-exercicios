def eh_primo():
    b = True
    while b:
        numero = int(input("Digite Um Numero:"))
        if numero % 2 == 0:
        	b = False
        else:
            print("Tente Novamente")
print(eh_primo())      
print("Very Nice")
