tem_duvida = True
while tem_duvida:
    resp = input("Voce tem duvida? ")
    if resp == "não":
        tem_duvida = False
    else:
        print("Pratique mais")

print("Até a próxima")