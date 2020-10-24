def eh_primo (num):
    resto = num%2
    divisor = 3
    if num==0 or num==1:
        return False
    if num== 2 or num == 3:
        return True
    while divisor < num:
        divisor += 2
        if resto != 0:
            return True
        elif resto == 0:
            return False
    
    
   