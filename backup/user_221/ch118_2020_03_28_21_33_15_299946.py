def reflexao_interna_total(n1, n2, teta2):
    y = (n2*math.sin(math.radians(teta2)))/n1
    return y
if reflexao_interna_total(n1, n2, teta2) > 1:
    return True
print ('reflexão interna')
else:
    return False
print ('refração')