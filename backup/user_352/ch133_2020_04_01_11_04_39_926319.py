resposta1=input("Está funcionando?")
if resposta1 == "s":
    print("Ssem problemas!")
else:
    resposta2=input("Você sabe corrigir")
    if resposta2 == "s":
        print("Sem problemas!")
    else:
        resposta3=input("Você precisa corrigir")
        if resposta3 == "s":
            print("Apague tudo e tente novamente")
        else:
            print("Sem problemas!")