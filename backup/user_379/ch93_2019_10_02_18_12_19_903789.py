def verifica_numero(numero):
    numero_texto=str(numero)
    soma=0
    i=0
    while i<len(numero_texto):
        soma+=(int(numero_texto[i]))**(int(numero_texto[i]))
        if soma==numero:
            return True
        if soma!=numero or numero<1:
            return False