yesno=input(print("Está funcionando? (n/s)"))

if (yesno == "sim"):
    print("Sem problemas!")
else:
    yesno = input(print("Você consegue consertar? (n/s)"))

    if (yesno == "sim"):
        print("Sem problemas!")
    else:
        yesno=(input(print("Você precisa consertar? (n/s)")))
    
        if (yesno == "sim"):
            print("Apague tudo e tente novamente")
        else:
            print("Sem problemas!")
