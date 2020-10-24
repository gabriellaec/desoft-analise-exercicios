def eh_crescente(lista):
    for i in range(0, len(lista)):
        ver = []
        ver.append(lista[i])
        if ver[i]>lista[i]:
            return True
        elif ver[i]<lista[i]:
            return False