def verifica_lista(lista):
    if []:
        return "misturado"
    else:
        for i in lista:
            if i%2 == 0:
                return "par"
            else:
                return "ímpar"