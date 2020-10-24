duvida = True

while duvida:
    d = input("Você tem dúvidas?")
    if d != "não":
        print("Pratique mais")
    elif d == "não":
        print("Até a próxima")
        duvida = False