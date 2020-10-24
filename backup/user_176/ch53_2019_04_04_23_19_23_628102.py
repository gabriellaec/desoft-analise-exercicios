'''
def inverte_lista(lista):
    lista= lista[::-1]
    return lista
'''

def inverte_lista(lista):
    lista_2=[]
    i= -1
    while i >= -len(lista):
        lista_2.append(lista[-1])
        i-=1
    return lista_2