import math
correto='n'
while(correto=='n'):
    executa=input("O código está executando?")
    if(executa=='n'):
        while(executa=='n'):
            print("Corrija o código e tente de novo")
            executa=input("O código está executando?")
    elif(executa=='s'):
        correto=input("O código produziu o resultado correto?")
        if(correto=='s'):
            print('Parabéns!')
        elif(correto=='n'):
            print("Corrija o código e tente de novo e volte para o começo de tudo")



