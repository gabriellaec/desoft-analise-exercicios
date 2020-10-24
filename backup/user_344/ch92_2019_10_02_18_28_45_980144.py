def simplifica_dict(dic):
    a = [{'a': 123456}, {'b': 123456}, {'a': 123456}]
	b = []
	for i in range(0, len(a)):
    	if a[i] not in a[i+1:]:
      		b.append(a[i])
	return b
