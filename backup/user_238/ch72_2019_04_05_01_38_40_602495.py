def lista_caracteres(string):
        caracteres=[]
        i=0
        while i < len(string):
            caracteres.append(string[i])
            i+=1
        return caracteres
palavra='abacate'
print(lista_caracteres(palavra))