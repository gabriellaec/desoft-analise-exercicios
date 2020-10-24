import math as m

bhaskara_list = list()
sin_list = list()
diff = list()

for a in range(0, 90, 1):
    sin_alpha = (720*a - 4*(a**2))/(40500 - 180*a + a**2)
    bhaskara_list.append(sin_alpha)

for b in range(0, 90, 1):
    sin_beta = m.sin(b)
    sin_list.append(sin_beta)

for i in bhaskara_list:
    for j in sin_list:
        diff.append(i-j)

print(abs(max(diff)))