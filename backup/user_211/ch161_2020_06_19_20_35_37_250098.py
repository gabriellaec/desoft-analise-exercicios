

def PiWallis(n):
    pi = 2.
    for i in range(1, n):
        left = (2. * i)/(2. * i - 1.)
        right = (2. * i)/(2. * i + 1.)
        pi = pi * left * right
    return pi
  
