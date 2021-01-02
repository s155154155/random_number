import random

start = input('請決定隨機數字範圍開始值：')
end = input('請決定隨機數字範圍結束值：')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

while True:
	count += 1
	num = input('1~100猜一個數字')
	num = int(num)

	if num == r:
		print('終於猜對了！')
		print('第', count, '次')
		break
	elif num > r:
		print('比答案大')
	else:
		print('比答案小')
	print('第', count, '次')