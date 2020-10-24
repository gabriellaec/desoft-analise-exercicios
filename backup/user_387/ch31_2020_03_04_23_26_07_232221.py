import math
def eh_primo(n):
	n = math.sqrt(n**2)
	
	if n == 0 or n == 1:
    	print(False)
    else:
        if n == 2:
            print(True)
            elif n%2 == 0:
                print(False)
                else:
                    x = 3
                    while(x < n):
                        if n % x == 0:
                            break
            		x = x + 2
                	if x == n:
                    	print(True)
                    else:
                        print(False)