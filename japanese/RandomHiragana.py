import random

#Only inlcudes what i have learned so far for practice. More will be added as time goes on
soundList = ['a','i','u','e','o','ka','ki','ku','ke','ko','sa','shi','su','se','so','ta','chi','tsu','te','to','na','ni','nu','ne','no','ha','hi','fu','he','ho','ma','mi','mu','me','mo','ya','yu','yo','ra','ri','ru','re','ro','wa','wi','we','wo','n']

numberList = []

flag = True

while flag:
	num = 0
	numFlag = True;
	while numFlag:
		num = random.randint(1,len(soundList))
		if (num not in numberList):
			numberList.append(num)
			numFlag = False
	print soundList[num-1]
	
	if (len(soundList) == len(numberList)):
		numberList = []
	instuff = raw_input()
	if instuff == "exit":
		flag = False
	
