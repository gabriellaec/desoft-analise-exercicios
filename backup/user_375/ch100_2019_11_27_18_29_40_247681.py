def login_disponivel(login_new, logins):
	login_test = 0

	for i in range (0, len(logins)):
		for login in logins:
			if i == 0 and login_new == login:
				login_test += 1
			elif login_new + str(i) == login:
				login_test += 1

	if login_test > 0:
		return login_new + str(login_test)
	else:
		return login_new

login_new = ""

while login_new != "fim":
	login_new = input("Qual o seu login? ")
	if login_new != "fim":
		logins.append(login_disponivel(login_new, logins))

for login in logins:
	print(login)