def pos_arroba(email):
    i=0
    while i< len(email):
        if email[i] == '@':
            return i
        else:
            i+=1
           
def nome_usuario (palavra):
    verifica=pos_arroba(palavra)
    i=0
    palavra2=[]
    while i < verifica:
        palavra2.append(palavra[i])
        i+=1  
    return ''.join(palavra2)