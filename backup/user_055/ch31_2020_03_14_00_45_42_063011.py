n = int(input()) 
x = 1
while x < (n - 2):
    x += 2
def eh_primo(n):
    if n % 2 == 0 and n != 2 or n % x == 0 and n != 2 or n == 0 or n == 1:
        return False
    if n == 2:
        return True
    else:
        return True
eh_primo(n)