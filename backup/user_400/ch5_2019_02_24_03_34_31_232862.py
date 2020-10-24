def func(num):
    if num > 2:
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
            else:
                return True
                break
    elif num == 2:
        return True
       
    else:
        return False
            
def maior_primo_menor_que(num):
    if func(num):
        return num
    elif num<2:
        return -1
    else:
        while i<num:
            if func(i):
                return i
            else:
                return i+1
        
