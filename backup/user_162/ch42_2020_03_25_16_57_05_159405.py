l = []
a = str(input())
while a!="fim":
    if a[0] == "a":
        l.append(a)
    a = str(input())
for i in l:
    print(i)