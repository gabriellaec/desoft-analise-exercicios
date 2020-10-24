100_primeiros = [0]*100
while len(100_primeiros) < 99:
	100_primeiros[i + 1] = 100_primeiros[i]*(1/2)
    s += i
print(s)    