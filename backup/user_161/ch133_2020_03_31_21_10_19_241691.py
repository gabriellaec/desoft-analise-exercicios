x = input("Esta funcionando?")
if x == "s":
    print("Sem problemas!")
else:
    x = input("Você sabe corrigir?")
    if x == "s":
        print("Sem problemas!")
    else:
        x = input("Você precisa corrigir?")
        if x == "s":
            print("Apague tudo e tente novamente")
        else:
            print("Sem problemas!")
