tem_duvida = True
while tem_duvida:
    resp = input("tem duvida? ")
    if resp != "não":
        print("Pratique mais")
    else:
        tem_duvida = False
print("Até a próxima")