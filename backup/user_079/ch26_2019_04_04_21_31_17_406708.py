def eaemen(d,h,m,s):
    x= d*24*60*60+h*60*60+m*60+s
    return x
d= int(input('d: '))
h= int(input('h: '))
m= int(input('m: '))
s= int(input('s: '))
x= eaemen(d,h,m,s)
print (x)