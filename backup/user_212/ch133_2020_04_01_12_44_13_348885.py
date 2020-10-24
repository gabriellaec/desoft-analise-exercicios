funciona= input("O seu programa está funcionando?")
if funciona == 's':
    print ("Sem problemas!")
elif funciona == 'n':
    correção= input("Você sabe corrigir? (n/s)")
    if correção == 's':
        print ("Sem problemas!")
    elif correção == 'n':
        precisa_c=input("Você precisa corrigir?(n/s")
        if precisa_c == 's':
            print ("Apague tudo e tente novamente")
        elif precisa_c == 'n':
            print ("Sem problemas!")
        
    