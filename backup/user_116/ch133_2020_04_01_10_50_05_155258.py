i=True
while i==True:
    p1=input("esta funcionando? ")
    if p1=="s":
        print("sem problemas")
        i=False
    elif p1== "n":
        p2=input("voce sabe corrigir? ")
        if p2=="s":
            print("sem problemas")
            i=False
        elif p2== "n":
            p3=input("voce precisa corrigir? ")
            if p3 == "s":
                print("apague tudo e tente novamente")
            elif p3== "n":
                print("sem problema")
                i=False