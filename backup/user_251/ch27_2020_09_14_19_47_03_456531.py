tem_duvida = True
a = input("Você tem alguma dúvida?" )
while tem_duvida == True:
    if a != "não":
        print("Pratique mais")
        a = input("Você tem alguma dúvida?" )
    else:
        tem_duvida = False
        print("Até a próxima")
        
        
