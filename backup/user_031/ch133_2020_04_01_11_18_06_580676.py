pergunta= str(input("Está funcionando?(s/n) ")).strip().lower()
if pergunta == "s":
    print("Sem problemas!")
elif pergunta == "n":
    pergunta2= str(input("Você sabe corrigir?(s/n) ")).strip().lower()
    if pergunta2 == "s":
        print("Sem problemas!")
    elif pergunta2 == "n":
        pergunta3= str(input("Você precisa corrigir?(s/n) ")).strip().lower()
        if pergunta3 == "s":
            print("Apague tudo e tente novamente!")
        else:
            print("Sem problemas!")