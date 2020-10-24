def eh_primo(n):    
    if n < 0:        
        print(\"Número inválido. Digite apenas valores positivos\")    
    if n == 0 or n == 1:
        print("%d é um caso especial.\" % n)    
     else:        
          if n == 2:\n            
              print(\"2 é primo\")       
           elif n%2 == 0:\n            
              print(\"%d não é primo, pois 2 é o único número par primo.")     
            else:          
                 x = 3\n           
            while(x < n):
                  if n % x == 0:                  
                      break              
                      x = x + 2            
                  if x == n:
                    print("%d é primo" )           
                  else:
                    print("%d não é primo, pois é divisível por " % (n, x))")