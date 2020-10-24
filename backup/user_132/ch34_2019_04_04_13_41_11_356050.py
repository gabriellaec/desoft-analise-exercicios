c = int(input("deposito"))
j = int(input("juros"))
t = 0

while t < 23:
    r = c * j ** t
    t = t + 1
    print(r)
print(r)