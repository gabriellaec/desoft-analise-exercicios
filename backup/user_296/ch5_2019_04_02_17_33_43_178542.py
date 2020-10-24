def maior_primo_menor_que(n):
    if n % 2 ==0 or n%3 == 0 or n%5 == 0 or n% 7 ==0:
        return True
    elif n -1 % 2 != 0 or n-1 % 3 != 0 or n-1 % 5 != 0 or n-1 % 7 != 0:
        return False
        return n-1
    elif n -2 % 2 != 0 or n-2 % 3 != 0 or n-2 % 5 != 0 or n-2 % 7 != 0:
        return False
        return n-2
    elif n -3 % 2 != 0 or n-3 % 3 != 0 or n-3 % 5 != 0 or n-3 % 7 != 0:
        return False
        return n-3
    else:
        return -1
a = int(input())
print(maior_primo_menor_que(a))
    
        