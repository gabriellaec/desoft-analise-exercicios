n = int() 
x = 1
while x < (n - 2):
    x += 2
def eh_primo(n):
    if n % 2 == 0 and n != 2 and n != 3 or n % x == 0 and n != 2 and n != 3 or n == 0 or n == 1:
        print (False)
    else:
        print (True)
eh_primo(n)
