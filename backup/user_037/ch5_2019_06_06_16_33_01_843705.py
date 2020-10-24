lista = []
n = 11
print("Prime numbers lower than", n )

for num in range(2, n+1):
   # prime numbers are greater than 1
   if num >= 3:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
            lista.append(num)
            
        
print(lista[-1])