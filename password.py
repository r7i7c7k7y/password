password = 'qazws015'
i = 3
while i > 0:
	i = i -1
	a = input('輸入密碼 :')
	if a == password:
		print('登入成功!')
		break
	elif i != 0:
		print('密碼錯誤! 還有',i,'次機會!')
	

