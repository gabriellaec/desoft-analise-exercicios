def is_int (num):
    return num == int(num)

def eh_primo (num):
    if is_int(num /2):
        return False
    else:
        i = 3
        while i < num:
            if is_int(num / i):
                continue
            else:
                return True
            
            i += 2
