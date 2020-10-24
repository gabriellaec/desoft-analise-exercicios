def conta_ocorrencias(a,b,c):
    s= [a, b, c]
    if a==b and a==c and b==c:
        l={a:3} or l={b:3} or l={c:3}
    if a==b and a!=c and b!=c:
        l={a:2,c:1}
    if a!=b and a!=c and b!=c:
        l={a:1,b:1,c:1}
    if a==c and a!=b and b!=c:
        l={a:2,b:1}    
    
    
    