
class testObject:
	def __init__(self):
		self.status = "+"
		self.level = 0
	def __str__(self):
		return "status is %s (%d)" %(self.status, self.level)

	def cook(self,timeframe):
		if timeframe >=0 and timeframe<3:
			self.status = "++"
		elif timeframe >=3 and timeframe<5:
			self.status = "+++"
		elif timeframe > 5:
			self.status = "++++"

newObj = testObject()
print(newObj)







