def libras_para_kg(milhas):
    km= 1.609344
    y= milhas*km
    return y

a= 10
b= libras_para_kg(a)
print ('{0} km'. format(b))