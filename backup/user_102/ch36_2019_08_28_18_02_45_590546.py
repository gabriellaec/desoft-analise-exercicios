eh_primo = True

while eh_primo:
    a = int(input("Digite Um Numero Par:"))
    if a % 2 == 0:
        eh_primo = False
    else:
        print("Tente Novamente")
        
print("Very Nice")
