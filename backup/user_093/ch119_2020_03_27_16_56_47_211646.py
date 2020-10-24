import math

list=[]
def calcula_euler(x,a):
    a=0
    i=0
    while i!=19:
        a+=(x/(math.factorial(i)))
        list.append(a)
        b=list[0]+1
        i+=1
        return b
        

print(calcula_euler(2,3))
