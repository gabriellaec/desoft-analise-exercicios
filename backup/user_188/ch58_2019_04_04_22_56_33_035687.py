def calcula_fibonacci(n):
	if n <= 0:
		return []
	if n == 1:
		return [0]
	result = [0, 1]
	if n == 2:
		return result
    for i in xrange(2, n):
		result.append(result[i-1] + result[i-2])
    return result