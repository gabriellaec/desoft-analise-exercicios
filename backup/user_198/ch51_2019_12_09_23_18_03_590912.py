def cresc(num):
    cresc=[]
    primeiro=num[0]
    cresc.append(primeiro)
    maior = primeiro
    for i in range (1,len(num)):
        proximo=num[i]
        if proximo > maior:
            cresc.append(proximo)
            maior = proximo
        
        
    return cresc

num=[1,3,2,3,4,6,5]
x=cresc(num)
print(x)