fun=input("Está funcionando?")
if fun=='s':
    print("Sem problemas")
else:
    fun=input("Você sabe corrigir?(n/s)")
    if fun=='s':
        print("Sem problemas!")
    else:
        fun=input("Você precisa corrigir?(n/s)")
        if fun=='s':
            print("Apague tudo e tente novamente"
        else:
            print("Sem problemas!")