
def snell_descartes(n1,n2,o):
    x = (n1 * math.sin(math.degrees(o)))/ n2 
    o2=math.sin(x)
    return o2