i = float(input())
m = float(input())
j = float(input())
n = 2
E = i*1.005
print (round(E,2))
while n < 25:
    E = ((E+m)*1.005)
    print(round(E,2)) 
    n = n + 1
print(round((E-(i+m*23)),2))
