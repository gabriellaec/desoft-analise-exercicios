n = 0
num = input("número: ")
def eh_primo(num):
    if num%2 != 0 and num/2 != 1:
        while n < num:
            if num%n != 0:
                print('é primo')
    