lista=[]
cont = 0
def acha_bigramas(string):
    while cont < len(string) - 2:
        lista.append(string[cont:cont+2])
        cont+=1