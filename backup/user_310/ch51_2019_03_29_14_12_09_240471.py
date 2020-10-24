def estritamente_crescente(l):
    lista_resposta=[]
    maior_numero=l[0]
    i=1
    
    while i<len(l):
        if l[i]>maior_numero:
            lista_resposta.append(l[i])
            maior_numero=l[i]
        i+=1
    return lista_resposta

#funcionou para todos os testes
#da pra melhorar