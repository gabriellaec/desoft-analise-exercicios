def equaliza_imagem (r, g, b, k):
    r = r * k
    g = g * k
    b = b * k
    if (r > 255):
        r = 255
    elif (g>255):
        g = 255
    elif(b>255):
        b = 255
    vF = [r, g, b]
    return vF