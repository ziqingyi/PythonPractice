import sys
class Home:
	def __init__(self, new_area, new_info,new_addr):
		self.area = new_area
		self.info = new_info
		self.addr = new_addr
		self.left_area = new_area
		self.contain_items = []
	def __str__(self):
		msg = "total area: %d, available area is: %d"%(self.area,self.left_area)
		msg += "\nadditional info is %s, address is %s"%(self.info,self.addr)
		msg += "\nshow items: %s"%(str(self.contain_items))
		return msg
	def __del__(self):
		print("delete the object")
	def add_item(self,item):
		self.left_area -= item.get_area()
		self.contain_items.append(item.get_name())

class objectClass:
	def __init__(self):
		print("from object")
	def __price(self,lprice):
		self.price = lprice
	def printprice(self, num):
		self.__price(num)
		print("the price is %d"%(self.price))




class Bed(objectClass):
	def __init__(self,new_name,new_area):
		self.name = new_name
		self.area = new_area
	def __str__(self):
		return "%s occupy space: %d"%(self.name,self.area)

	def get_area(self):
		return self.area
	def get_name(self):
		return self.name

newHome = Home(100,"house", "easewood")
print(newHome)

bed1 = Bed("prince",20)

newHome.add_item(bed1)
print(newHome)

print(sys.getrefcount(bed1))
print(bed1.printprice(50))


