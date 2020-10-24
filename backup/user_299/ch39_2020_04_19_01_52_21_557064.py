m = 2
termomax = 1
numrespon = 1
termos_n_p_m = {}
while m<1001:
    n = m
    while n != 1:
        termos_n_p_m[m] = 1
        if n%2 == 0:
            n = n/2
            termos_n_p_m[m] += 1
        else:
            n = 3*n + 1
            termos_n_p_m[m] += 1
    m += 1
for num,termos in termos_n_p_m.items():
    if termos>termomax:
        termomax = termos
        numrespon = num
        
print(numrespon)
    
        
    