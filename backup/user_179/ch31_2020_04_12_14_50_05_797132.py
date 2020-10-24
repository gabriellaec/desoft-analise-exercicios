def eh_primo (n):
    i = 1
    if n == 2:
        return True
    else:
        while i <= n and n!= 0 and n!= 1:
            if n%i == 0 and n==i:
                return True
            else:
                i = i + 2
            return False