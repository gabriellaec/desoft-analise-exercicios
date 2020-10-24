def Piwallis (i):
    x = 2
    c = 1
    while x <= i * 2:
        if c % 2 != 0:
            pi *= (x / (x - 1))
        else:
            pi *= (x / (x + 1)
        x += 2
        c += 1
   return pi
                   