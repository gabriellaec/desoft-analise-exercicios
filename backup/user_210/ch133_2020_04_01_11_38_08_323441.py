while True:
    resp = input("Está funcionando? ")
    if resp == "s":
        print("Sem problemas!")
        break

    resp = input("Você sabe corrigir? (n/s) ")
    if resp == "s":
        print("Sem problemas!")
        break

    resp = input("Você precisa corrigir? (n/s) ")
    if resp == "s":
        print("Apague tudo e tente novamente")
    else:
        print("Sem problemas!")
    
    break