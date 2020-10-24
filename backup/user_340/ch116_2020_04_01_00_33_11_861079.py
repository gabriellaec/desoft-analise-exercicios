def raiz_quadrada(b):
    i=1
    raiz = 0
    while b>=i:
      b-=i
      raiz+=1
      i=i+2
      return raiz
        
    