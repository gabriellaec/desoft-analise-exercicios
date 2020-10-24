def faixa_notas(l):
   if len(l) == 0:
        return False
   i = 0
   menor = 0
   igual = 0 
   maior = 0
   lista = 0
   lista1 = []
   lista2 = []
   lista3 = []
   while i < len(l):
        
        if l[i] < 5:
               menor += 1
        elif 5 <= l[i] <= 7:
                igual += 1
        elif l[i] > 7:
                maior += 1
          
        i +=1
   lista1.append(menor)
   lista2.append(igual)
   lista3.append(maior)
   
   lista =  lista1 + lista2 + lista3
         
   return lista


