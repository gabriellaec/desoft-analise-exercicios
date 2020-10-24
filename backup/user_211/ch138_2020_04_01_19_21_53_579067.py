executa='n'
correto='n'

while(executa=='n'):
    while(correto=='n'):
        executa=input("O código está executando?(s/n)")
        if(executa=='n'):
                print("Corrija o código e tente de novo")
        elif(executa=='s'):
            correto=input("O código produziu o resultado correto?(s/n)")
            if(correto=='s'):
                print('Parabéns!')
                break
            elif(correto=='n'):
                print("Corrija o código e tente de novo e volte para o começo de tudo")






