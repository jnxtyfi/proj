def sum(x,y):
	return int(x) + int(y)

def rev(st):
	return str(st[::-1])

def sdv(x, c, d):
	if d == "l":
		return int(x) << int(c)
	elif d == "r":
		return int(x) >> int(c)
