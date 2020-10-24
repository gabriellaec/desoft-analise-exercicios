#Solução com while
#def fatorial(n):
 #   a=1
  #  while True:
   #   if n != 0:
    #        a= a * n
     #       n= n - 1
      #else:
       #     break
    #return a
#Solução com for
def fatorial(n):

    fatorial= 1
    for k in range(1,n+1):
        fatorial= fatorial*n
        n= n - 1
    return fatorial