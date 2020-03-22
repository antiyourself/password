chance = 3
my_password = 'a123456'
while chance > 0:
	password = input('輸入密碼: ')
	if password == my_password:
		print('登入成功')
		break

	else:
		chance = chance - 1
		print('密碼錯誤! 還有 ', chance, '次機會')
		
