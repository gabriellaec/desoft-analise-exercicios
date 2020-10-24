x=int(input('deposito inicial?:'))
y=int(input('taxa?:'))
z=(((y/100)+1))
n=1
while n <24:
    zek=x*z**n
    print('%.2f' %zek)
    n+=1
print('%.2f' %zek)



