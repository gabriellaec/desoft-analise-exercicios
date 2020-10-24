r1=str(input("Seu programa está funcionando?"))
if r1=="s":
    print ("Sem problemas!")
elif r1=="n":
    r2=str(input("Você sabe corrigir?"))
    if r2=="s":
        print ("Sem problemas!")
    elif r2=="n":
        r3=str(input("Você precisa corrigir?"))
        if r3=="s":
            print ("Apague tudo e tente novamente.")
        elif r3=="n":
            print ("Sem problemas!")
            