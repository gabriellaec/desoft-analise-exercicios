def equaliza_imagem(ip, k):
    ip_k=[0]*len(ip)
    i=0
    while i<len(ip):
        ip_k[i] = ip[i]*k
        i+=1
        if ip_k[i] > 255:
            ip_K[i] == 255
    return ip_k
        