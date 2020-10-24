def conta_a(plv):
    t = 0
    w = 0
    while t < len(plv):
        if plv[t] == 'a':
            w += 1
        t += 1    
    return w 