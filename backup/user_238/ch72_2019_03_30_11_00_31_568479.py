def lista_caracteres(lista):
        caracteres=[]
        i=0
        while i < len(lista):
            caracteres.append(lista[i])
            i+=1
        return caracteres
palavra='abacate'
print(lista_caracteres(palavra))