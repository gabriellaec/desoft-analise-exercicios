def func(num):
    if num > 2:
        for i in range(2,num):
            if (num % i) == 0:
                return False
                
            else:
                return True
                
    elif num == 2:
        return True
       
    else:
        return False

            
def maior_primo_menor_que(num):
    x = num -3
    if func(num):
        return num
    elif num<2:
        return -1
    else:
        while x<num:
            if func(x):
                return x
                break
            else:
                return x+1
