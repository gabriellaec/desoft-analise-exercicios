ciclo = True
resposta_inicial = input("O código está executando?")


while ciclo == True:
    while resposta_inicial != "s":
        print("Corrija o código e tente de novo")
        resposta_inicial = input("Código está executando?")
    
    resposta_final = input("O código produz o resultado correto?")
    while resposta_final != "s": 
        print("Corrija o código e tente de novo e volte para o começo de tudo.")
        resposta_inicial = input("Código está executando?")
        while resposta_inicial != "s":
            print("Corrija o código e tente de novo")
            resposta_inicial = input("Código está executando?")
        resposta_final = input("O código produz o resultado correto?")
    print("Parabéns!")   
    ciclo = False   