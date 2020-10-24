lista = []
def maior_primo_menor_que:
    
	for num in range(2, n+1):
   	if num >= 3:
  	     for i in range(2,num):
   	        if (num % i) == 0:
   	            break
   	    else:
   	         lista.append(num)
            
        
print(lista[-1])