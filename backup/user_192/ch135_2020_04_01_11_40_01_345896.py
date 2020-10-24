def equaliza_imagem(ip, k):
    ip_k=[0]*len(ip)
    i=0
    while i<len(ip):
        ip_k[i] = ip[i]*k
        if ip_k[i] > 255:
            ip_k[i] == 255
        i+=1
    return ip_k
        