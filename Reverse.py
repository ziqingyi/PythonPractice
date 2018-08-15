import re
def reverseAndCapitalise(sentenceIn):
	ret = ''
	for c in re.findall(r"[\w']+|\s*[.,!? ]\s*",sentenceIn):
		if re.compile(r"[\w']+").match(c):
			ret += c[::-1].capitalize()
		else:
			ret += c
	print(ret)


reverseAndCapitalise("Hey there, Alan")





