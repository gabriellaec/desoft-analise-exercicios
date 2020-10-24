def raiz_quadrada(x):
    i=1
    raiz = 0
    while x>=i:
      x-=i
      raiz+=1
      i=i+2
    return raiz
        
    