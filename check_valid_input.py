def check_valid(inputString):
	if type(inputString) == str:
		readings = list(map(int, inputString.split(',')))
		return readings
	else:
		return False