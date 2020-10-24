def raiz_quadrada(numero):
  i=1
  x=numero-i
  c=1
  if x!=0:
        while x!=0:
            x=numero-1
            i+=2
            c+=1
  if x==0:
    return c
print (raiz_quadrada(49))
       
        
    