def inverte_lista(lista):
    i=0
    j=len(lista)-1
    palavra=[]
    while i <= j:
        palavra.append(lista[j])
        j-=1
    return palavra
x=['aaa','bbb', 'xxx']
print(inverte_lista(x))