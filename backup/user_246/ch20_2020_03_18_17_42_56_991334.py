x=int(input('Vai anda quanto?'))
if x<= 200:
    y=x*0.5
elif x>200:
    y=(x-200)*0.45+100
print('R${0:.2f}'.format(y))