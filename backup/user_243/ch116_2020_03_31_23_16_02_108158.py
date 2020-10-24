def raiz_quadrada(x):
    i=1
    num=0
    while x>=i:
        x=x-i
        i+=2
        num+=1
        print(num)