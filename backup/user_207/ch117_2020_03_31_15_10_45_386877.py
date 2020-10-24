def snell_descartes (n1,n2,theta01):
    seno_theta02 = n1/n2 * sin(theta01/360 *2*pi)
    return asin(seno_theta02)*180/pi