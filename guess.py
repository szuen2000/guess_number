import random
r = random.randint(  1 , 100 )

while True:
	user = int(input('猜數字: '))
	if user == r :
		print('恭喜你猜對了! ')
		break
	elif user > r :
		print('比答案大')
	else :
		print ('比答案小')