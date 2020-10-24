def equaliza_imagem(ip, k):
    ip_k=[0]*len(ip)
    i=0
    while i<len(ip) and ip[i] <= 255 and ip[i] >= 0:
        ip_k[i] = ip[i]*k
        i+=1
    return ip_k
        