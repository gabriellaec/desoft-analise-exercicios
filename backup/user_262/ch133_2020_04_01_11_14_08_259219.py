fun=input("está funcionando?")
if fun=='n':
    fun=input("você sabe corrigir?")
    if fun=='n':
        fun=input("você precisa corrigir?")
        if fun=='s':
            print("Apague tudo e tente novamente")
        else:
            print("sem problemas!")
    else:
        print("sem problemas!")
else:
    print("sem problemas!")