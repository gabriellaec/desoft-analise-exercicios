def verifica_lista(lista):
    teste = []
    for i in lista:
        y = (-1)**i
        teste.append(y)
        print (teste)
        for n in range(len(teste)-1):
            if teste[n] == teste[n+1] and n == 1:
                return "par"
            elif teste[n] == teste[n+1] and n == -1:
                return "impar"
            else:
                return "misturado" 