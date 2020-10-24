In = float(input())
Mn = float(input())
tax = float(input())
for i in range(1,25):
    print('{0:.2f}'.format(In*(1+tax)**i + Mn*((1+tax)**(i+1) - 1)/tax))

i = 24
print('{0:.2f}'.format(In*(1+tax)**i + Mn*((1+tax)**(i+1) - 1)/tax - 24*Mn - In))