def eh_primo(x):
    b = True
    while b:
        if x % 2 == 0:
        	b = False
        else:
            print("Tente Novamente")
            
numero = int(input("Digite Um Numero:"))

print(eh_primo(numero))
print("Very Nice")
