num=[1,2,3]
def soma_valores(num):
    soma=0
    i=0

    while i<len(num):
        soma=soma+num[i]
        i+=1
    return(soma)

print(soma_valores(num))


