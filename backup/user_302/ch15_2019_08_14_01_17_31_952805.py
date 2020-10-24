import math 
def volume_da_pizza(z,a):
	y = 2*(math.pi*z**2)+(2*math.pi*z*a)
	return y
d = 10
b = 3
c = volume_da_pizza(d,b)
print(c)