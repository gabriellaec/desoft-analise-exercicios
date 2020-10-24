#comoiniciar um n?
n=1
def calcula_tamanho(n):
    tamanho=1
    while n!=1:
        if n%2==0:
            n=n/2
            tamanho+=1
        else:
            n=3*n+1
            tamanho+=1
    return tamanho
tamanhomaior=1
nmaior=1
while n<1000:
    tamanho=calcula_tamanho(n)
    if tamanho>tamanhomaior:
        tamanhomaior=tamanho
        nmaior=n 
    n+=1
print (tamanhomaior,' ',nmaior)