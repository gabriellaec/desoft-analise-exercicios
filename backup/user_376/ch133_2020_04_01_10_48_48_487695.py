a=str(input("Está funcionando ?"))
if ["s"] in a:
    print("Sem problemas!")
elif ["n"] in a:
    b=str(input("Você sabe corrigir? (n/s)"))
    if ["s"] in b:
        print("Sem problemas!")
    elif ["n"] in b:
        c=str(input("Você precisa corrigir? (n/s)"))
        if ["s"] in c:
            print("Apague tudo e tente novamente")
        elif ["n"] in c:
            print("Sem problemas!")