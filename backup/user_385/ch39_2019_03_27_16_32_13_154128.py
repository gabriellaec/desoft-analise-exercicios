num =int(input('Numero:'))
s=0
while num != 0 :
    s+=num
    num= int(input('Numero:'))
    if num == 0:
print(s)