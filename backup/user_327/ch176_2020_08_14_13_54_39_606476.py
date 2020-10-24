def imprime_grade(n):
    imp = "+"
    ang = "|"
    
    for i in range(0,n):
        imp += "-+"
        ang += " |"
        
    for e in range(0,n):
        print(imp)
        print(ang)
    
    print(imp)