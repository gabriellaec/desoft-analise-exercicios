def PiWallis(n):
    y = 0
    if n >= 2:
        y += n/(n+1)
        return 2*y
        
       
        