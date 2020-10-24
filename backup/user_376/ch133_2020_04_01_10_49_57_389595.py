a=str(input("Está funcionando ?"))
if a in ["s"]:
    print("Sem problemas!")
elif a in ["n"]:
    b=str(input("Você sabe corrigir? (n/s)"))
    if b in ["s"]:
        print("Sem problemas!")
    elif b in ["n"]:
        c=str(input("Você precisa corrigir? (n/s)"))
        if c in ["s"]:
            print("Apague tudo e tente novamente")
        elif c in ["n"]:
            print("Sem problemas!")