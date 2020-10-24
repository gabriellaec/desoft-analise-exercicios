c= int(input('quantos cigarros vc fuma por dia?'))
a= int(input('ha quantos anos?'))
x= (10*c*a*365)%1440
t= ((10*c*a*365)/1440)- x
print(t)
       