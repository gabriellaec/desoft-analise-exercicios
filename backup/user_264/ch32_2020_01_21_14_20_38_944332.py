tem_duvidas = True

while tem_duvidas:
    p = input("tem alguma duvida?(s/não)")
    if p != "não":
        print ("Pratique mais")
        p = input("tem alguma duvida?(s/não)")
    else:
        tem_duvidas = False
print("Até a próxima")