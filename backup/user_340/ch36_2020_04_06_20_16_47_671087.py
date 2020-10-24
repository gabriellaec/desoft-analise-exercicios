lista=[]
def fatorial(n):
    i=0
    while i!=n:
        b=(n-i)
        lista.append(b)
        i+=1
    return lista
for e in lista:
  e*=e
  print(e)
    
    