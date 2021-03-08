def leapyear(x):
	if (x % 4 != 0):
		return False
	elif (x % 100 == 0):
		return False
	else:
		return True