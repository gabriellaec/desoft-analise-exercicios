def snell_descartes(n1,n2,teta1):
    teta1 = teta1*(m.pi/180)

    teta2 = m.asin((n1 * teta1)/n2)

    teta2 = teta2*(180/m.pi)

    return teta2