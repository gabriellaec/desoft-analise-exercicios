primeira_pergunta = input("O programa está funcionando?(s ou n)")

if primeira_pergunta == 's':
    print("Sem problemas!")
elif primeira_pergunta == 'n':
    segunda_pergunta = input("Você sabe corrigir?(s ou n)")
    if segunda_pergunta == 's':
        print("Sem problemas!")
    elif segunda_pergunta == 'n':
        terceira_pergunta = input("Você precisa corrigir?")
        if terceira_pergunta == 'n':
            print("Sem problemas!")
        elif terceira_pergunta == 's':
            print("Apague tudo e tente novamente")
            