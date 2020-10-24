def verifica_lista(lista):
    for i in lista:
        if i%2 == 0 :
            return "par"
        elif i%2 != 0 :
            return "impar"
        else: 
            return "misturado" 