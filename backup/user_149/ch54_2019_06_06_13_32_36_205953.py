
lista_nome = ['diogo','pedro']
lista_sobrenome = ['cintra','araujo']

def junta_nome_sobrenome(lista_nome, lista_sobrenome):
    
    junta = []
    i = 0
    while i <len(lista_nome):
        junta.append(lista_nome[i]+lista_sobrenome[i])
        i+=1
    return junta