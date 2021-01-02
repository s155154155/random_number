import random

r = random.randint(1 , 100)

while True:
	num = input('1~100猜一個數字')
	num = int(num)
	
	if num == r:
		print('終於猜對了！')
		break
	elif num > r:
		print('比答案大')
	else:
		print('比答案小')