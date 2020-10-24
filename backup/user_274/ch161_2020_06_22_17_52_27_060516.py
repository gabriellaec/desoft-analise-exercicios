def PiWallis(x):
    rep1 = "n"
    rep2 = "y"
    up = 2
    down = 1
    i = 0
    pi = 1
    while i < x:
        pi = pi*(up/down)

        if rep1 == "n":
            rep1 = "y"
        else:
            up = up + 2
            rep1 = "n"
        
        if rep2 == "n":
            rep2 = "y"
        else:
            down = down + 2
            rep2 = "n"
        i=i+1
    return pi*2