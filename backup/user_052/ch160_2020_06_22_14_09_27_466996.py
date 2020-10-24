import math

dic = {}

for x in range(0, 91):
    sin_python = math.sin(math.radians(x))
    sin_bhaskara = 4 * x * (180-x)/(40500 - x * (180 - x))
    dic[x] = abs(sin_python - sin_bhaskara)

for k,v in dic.items():
    resultado = max(dic, key = dic.get)
print (resultado)