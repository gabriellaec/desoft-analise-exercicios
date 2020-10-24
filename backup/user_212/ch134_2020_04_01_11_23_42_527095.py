def verifica_quadrado_perfeito (n, m, i):
    m= n 
    i= 1
    n=int(input("Digite um número")       
    while (m>=0):
          m -= i*2
          i += 1
    if m**2 == n**2 :
          return True 
    if m**2 != n**2:
          return False