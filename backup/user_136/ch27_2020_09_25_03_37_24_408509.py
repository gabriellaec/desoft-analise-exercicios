tentativas= True
while tentativas:
    resposta= input('tem dúvidas ? ')
    if resposta != "não":
        print ("Pratique mais")
    elif resposta == "não":
        print ("Até a próxima")
        tentativas= False