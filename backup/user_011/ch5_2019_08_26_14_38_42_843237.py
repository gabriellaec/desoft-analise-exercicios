def primo(num):
    

    primo = True
    a = 2
    while a < num:
        if num%a == 0:
            primo = False
        
        a+=1
    return primo

def maior_primo_menor_que(num):
    
    while num >= 2:
        if primo(num):
            return num
        num-=1
    return -1
print(maior_primo_menor_que(1))