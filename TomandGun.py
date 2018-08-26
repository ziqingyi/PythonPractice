
class Person(object):

	def __init__(self,name):
		super(Person,self).__init__()
		self.name = name

	def load_bullet(self,clip_temp,bullet_temp):
		clip_temp.add_bullet(bullet_temp)

	def load_clip(self,gun_temp,clip_temp):
		gun_temp.accept_clip(clip_temp)


class Gun(object):

	def __init__(self,name):
		super(Gun,self).__init__()
		self.name = name  # the type of the gun
		self.clip = None # the reference to clip obj

	def accept_clip(self,clip_temp):
		self.clip = clip_temp

	def __str__(self):
		return "the info of gun: %s" %(self.name)


class Clip(object):

	def __init__(self,max_num):
		super (Clip,self).__init__()
		self.max_num= max_num # max capacity
		self.bullet_list = [] # store reference to B
	def add_bullet(self,bullet_temp):
		""""add bullet to clip"""
		self.bullet_list.append(bullet_temp)

	def __str__(self):
		return "the info of clip: %d/%d"%(len(self.bullet_list),self.max_num)  # ava/total



class Bullet(object):
	def __init__(self, power):
		super(Bullet, self).__init__()
		self.power = power # power of the bullet


def main():

    #1 create Tom object
    Tom = Person('Tom')

    #2 create a Gun object
    ak47 = Gun("AK47")

    #3 create a Clip object
    clip_1 = Clip(20)

    #4 create bullets
    for i in range(15):
    	bullet_1 = Bullet(10)

    #5 Tom load the bullet to clip
    	Tom.load_bullet(clip_1,bullet_1)

    #6 load the clip to the gun
    Tom.load_clip(ak47,clip_1)

    # test: clip_1
    print(clip_1)

    #test ak47
    print(ak47)


if __name__ == '__main__':
	main()












