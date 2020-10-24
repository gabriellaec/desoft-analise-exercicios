def fatorial(n):
    if n < 2:
        return 1
    else:
        return n * fatorial(n-1)
def fatorial(z):
   produto=1
   termos=range(1,z+1)
   for o in termos:
       produto*=o
   return produto