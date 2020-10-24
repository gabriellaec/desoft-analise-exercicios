duv = input("Você têm dúvidas?")
if duv == "não":
    print("Até a próxima")
else:
    print("Pratique mais")
    while duv != "não":
        duv = input("Você têm dúvidas?")