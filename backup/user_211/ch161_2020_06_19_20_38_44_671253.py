

def PiWallis(n):
    return  2 * reduce(lambda x, y: x*y, [(4.0*(i**2))/(4.0*(i**2)-1) for i in range (1, n)])