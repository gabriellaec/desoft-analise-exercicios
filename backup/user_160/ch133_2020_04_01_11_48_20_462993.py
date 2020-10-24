pergunta = input("Está funcionando?")
if pergunta == "sim":
    print ("Sem problemas")
    else:
        pergunta2 = input ("Você sabe corrigir?")
        if pergunta2 == "sim":
            print ("Sem problemas")
            else:
                pergunta3 = input("Você precisa corrigir?")
                if pergunta3 == "não":
                    print ("Sem problemas")
                    else:
                        print("Apague tudo e tente novamente")
        