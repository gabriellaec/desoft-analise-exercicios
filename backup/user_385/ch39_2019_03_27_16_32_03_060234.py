num =float(input('Numero:'))
s=0
while num != 0 :
    s+=num
    num= float(input('Numero:'))
    if num == 0:
print(s)