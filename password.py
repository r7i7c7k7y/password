password = 'qazws015'
n = 0
while n < 3:
	a = input('輸入密碼 :')
	if a == password:
		print('登入成功!')
		break
	else:
		print('密碼錯誤! 還有',(2-n),'次機會!')
	n = n + 1

