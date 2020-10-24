dep = float(input())
tax = float(input())

t = 1
sald = dep

while t <= 24:
    
    sald = sald + (sald * (tax / 100))
    print ("Sald do t %d é de Rs%5.2f." % (t, sald))
    t += 1
print ("luc Rs%8.2f." % (sald-dep))

    
    
