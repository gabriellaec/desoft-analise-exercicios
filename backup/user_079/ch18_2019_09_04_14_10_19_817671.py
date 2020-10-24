def encontra_cateto(cat2,hip):
    cat1= (hip**2-cat2**2)**(1/2)
    return cat1
cat2=int(input('cat2: '))
hip=int(input('hip: '))
x=encontra_cateto(cat2,hip)
print(x)
