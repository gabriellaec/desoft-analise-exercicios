100_primeiros = [0]*100
i = 0
s = 0
while i < len(100_primeiros)
	100_primeiros[i + 1] = 100_primeiros[i]*(1/2)
    i += 1
    s += 1
print(100_primeiros)    