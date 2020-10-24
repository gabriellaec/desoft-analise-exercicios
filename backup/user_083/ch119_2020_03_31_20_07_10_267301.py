def calcula_euler(y):
    e=3
    x=1
    n=1
    y=e**x
    while x>0 and n>1:
        y=1+x+x**n/n
        n+=1
        x=1
    print(y)