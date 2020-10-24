

def quantos_uns(lista):
   listar = lista
   for i in lista:
       
       if len(listar) > 2:
           if listar[2] - listar[1] == listar[1] - listar[0]:
               return 'PA'
           elif listar[2]/listar[1] == listar[1]/listar[0]:
               return 'PG'
           else: 
               return 'NA'
       
       elif len(listar) == 2:
           if listar[0] != 0:
               if listar[1]%listar[0] != 0:
                   return 'PA'
               else:
                   return 'AG'
           else:
               return 'AP'
       
       elif len(listar) == 1:
           return 'NA'
           
           