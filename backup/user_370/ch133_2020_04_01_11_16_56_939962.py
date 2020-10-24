perg1=input("Está funcionando?(s/n): ")
if perg1 == "s" :
    print("Sem problemas!")
else:
    perg2=input("Você sabe corrigir?(s/n): ")
    if perg2 == "s":
        print(" Sem problemas!")
    else:
        perg3=input("Você precisa corrigir?(s/n): ")
        if perg3 == "s" :
            print("Apague tudo e tente novamente")
        else:
            print("Sem problemas!")