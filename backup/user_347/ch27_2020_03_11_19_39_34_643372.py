tem_duvidas = True
while tem_duvidas:
    duv = input("Você tem dúvidas?")
    if duv != "não":
        print("Pratique mais.")
    if duv == "não":
        tem_duvidas = False
        print("Até a próxima")