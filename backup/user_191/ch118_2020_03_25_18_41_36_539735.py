def reflexao_total_interna(n1,n2,t2):
    x=(n1*math.sin(math.radians(t2)))/n2
    y=math.asin(x)
    if math.degrees(y)>=90:
        print(1>2)
    else:
        print(1<2)