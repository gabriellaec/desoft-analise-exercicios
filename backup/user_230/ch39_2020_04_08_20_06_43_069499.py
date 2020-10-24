def par_impar(n):
    if n%2==0:
        return n/2
    elif n==0:
        return 1
    else:
        return n*3 + 1
    
def collatz(n):
    lista=[]
    while True:
        a=par_impar(n)
        lista.append(a)
        if a==1:
            break
        n=a
        return len(lista)
    
tamanho=[]
i=0
while i<1000:
    tamanho.append(collatz(i))
    i+=1
print(tamanho.index(max(tamanho)))