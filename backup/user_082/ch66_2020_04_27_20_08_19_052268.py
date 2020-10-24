def lista_sufixos(string):
    sufixo=[]
    palavra= string
    i=0
    while i < string:
        palavra = palavra - palavra[i]
        sufixo.append(palavra)
        i+=1
    return sufixo
   

        