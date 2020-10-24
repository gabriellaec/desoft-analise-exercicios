num=int(input('digite um numero: '))

def eh_primo(num):
    if num == 0 or num == 1:
        return 'False'
    if num == 2:
        return 'True'
    else:
        i=3
        while i<num:
            if num%i == 0:
                break
            i=i+2
        if num == i:
            return 'True'
        else:
            return 'False'
print(eh_primo(num))