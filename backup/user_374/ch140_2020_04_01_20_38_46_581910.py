def faixa_notas(lista):
   if len(lista) == 0:
        return False
   i = 0
   menor = 0
   igual = 0 
   maior = 0
   lista = 0
   lista1 = 0
   lista2 = 0
   lista3 = 0
   while i < len(lista):
        
        if lista[i] < 5:
               menor += 1
        elif 5 <= lista[i] <= 7:
                igual += 1
        elif lista[i] > 7:
                maior += 1
          

   lista1[0] = menor
   lista2[0] = igual
   lista3[0] = maior
   
   lista =  lista1 + lista2 + lista3
         
   return lista