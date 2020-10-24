tem_duvidas = True

p = input("tem alguma duvida?(s/não)")

while tem_duvidas:
    if p != "não":
        print ("Pratique mais")
        p = input("tem alguma duvida?(s/não)")
    else:
        tem_duvidas = False
print("Até a próxima")