dep = float(input())
tax = float(input())
tax = tax*0.01
for i in range(0,24):
    print('{0:.2f}'.format(dep*(1+tax)**i - dep))
    
print('{0:.2f}'.format(dep*(1+tax)**24 - dep))