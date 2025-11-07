def design_rug(width, length, pattern):
	result = "Your rug is:\n"
	for i in range(length):
		result += pattern * width
		if i < length - 1:
			result += "\n"
	return result

print(design_rug(4, 4, "*"))
