#def quantos_uns(numero):
 #   soma = 0
  #  for i in numero:
   #     if i == 1:
    #        soma+=1
    #return soma
    
def quantos_uns(n):
    qntos = 0
    n = str(n)
    for i in n:
        if i == '1':
            qntos += 1
    return qntos