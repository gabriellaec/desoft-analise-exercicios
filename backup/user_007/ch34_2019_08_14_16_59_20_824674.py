dep = float(input())
tax = float(input())
tax = tax*0.01
for i in range(0,25):
    print('{0:.2f}'.format(dep*(1+tax)**i))
    
print('{0:.2f}'.format(dep*(1+tax)**24 - dep))