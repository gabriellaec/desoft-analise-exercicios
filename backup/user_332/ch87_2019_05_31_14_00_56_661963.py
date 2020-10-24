with open('churras.txt') as ch:
    sum = 0
    for line in ch:
        f = line.readline()
        a = f.split(",")
        prod = a[1] * a[2]
        sum += prod
        