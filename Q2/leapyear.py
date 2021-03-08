def leapyear(x):
	if (x % 4 != 0):
		return False
	elif (x % 100 != 0):
		return True
	elif (x % 400 != 0):
		return False
	else:
		return True