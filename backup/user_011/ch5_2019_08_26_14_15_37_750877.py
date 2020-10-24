primo = True
a = 2
num = 13127
while a < num:
    if num%a == 0:
        primo = False
        
    a+=1
print(primo)