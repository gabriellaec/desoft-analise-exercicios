import math
encontra_cateto(cat1, hip):
    cat2 = (hip**2 - cat1**2)**(1/2)
    return cat2
a = encontra_cateto(4, 5)
print(a)