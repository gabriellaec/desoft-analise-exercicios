def PiWallis(n):
    i=1
    num = (2/1)
    while i <n:
        num = num*(num/(i+2))*((num+2)/(i+2))
        i+=1
    Pi =num*2
    return Pi