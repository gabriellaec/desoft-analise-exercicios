def monta_mala(bagagem):
    i=0
    a=0
    k=True
    quantidade=int(input("Quantos itens na bagagem?"))
    bagagem=[]
    #Montagem da lista
    while i<quantidade:
        peso=int(input("Qual o peso do item 1?:"))
        bagagem[i]=peso
        i+=1
        #Cortando os elementos da lista
    while k:
        if bagagem[a]<=23:
            
            a+=1
        else:
            return(bagagem)
        