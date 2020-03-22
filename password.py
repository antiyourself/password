chance = 3
my_password = 'a123456'
while chance > 0:
	chance = chance - 1
	password = input('輸入密碼: ')
	if password == my_password:
		print('登入成功')
		break

	else:
		print('密碼錯誤!')
		if chance > 0:
			print('還有', chance, '次機會')
		else:
			print('已無機會')
		
