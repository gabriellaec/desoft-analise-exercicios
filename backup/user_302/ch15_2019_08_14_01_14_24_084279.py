import math 
    def volume_da_pizza(r,h):
        y = 2*(math.pi*r**2)+(2*math.pi*r*h)
        return y
    a = 10
    b = 3
    c = volume_da_pizza(a,b)
    print(c)