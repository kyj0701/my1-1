def isleapyear(year):
	if y % 400 == 0:
		return True
	elif y % 100 == 0:
		return False
	elif y % 4 == 0:
		return True
	elif y < 0 :
		return 0
	else :
		return False


y = int(input())
print(y, isleapyear(y))