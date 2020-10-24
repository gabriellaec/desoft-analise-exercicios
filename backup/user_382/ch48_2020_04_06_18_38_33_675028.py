def estritamente_crescente(l1):
    if l1 == []:
        return False
    else:
        while True:
        maximo = l1[0]
        lista = [maximo]
        for i in range(len(l1)-1):
            if l1[i+1] > maximo:
                maximo = l1[i+1]
                lista.append(l1[i+1])
        if len(lista) == len(l1):
            return True
            break
        else:
            return False
            break
    
def eh_crescente(lista):
    if estritamente_crescente(lista) == False:
        return False
    else:
        return True