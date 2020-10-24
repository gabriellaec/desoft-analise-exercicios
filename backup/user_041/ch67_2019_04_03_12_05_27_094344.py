def alunos_impares(lista):
    lista_vazia=[]
    cont=1
    while cont%2==0 and cont!=1:
        lista_vazia.append(lista[cont])
    return lista_vazia
    