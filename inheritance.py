class rect:
	def __init__(self,length,breadth):
		self.l = length
		self.b  = breadth

	def info(self):
		print ("Length of the Rectangle is ",self.l)
		print ("Breadth of the Rectangle is ",self.b)

	def area(self):
		a = self.l * self.b
		print ("Area of the rectangle with {},{} is {}".format(self.l,self.b,a))


class cubiod(rect):
	"""docstring for cubiod"""
	def __init__(self, length,breadth,height):
		super().__init__(length,breadth)
		self.h = height

	def volume(self):
		v = self.l*self.b*self.h
		print("volume of the cubiod with length {},breadth {},and height {} is {}".format(self.l,self.b,self.h,v))



rect1 = rect(23,35)
rect1.info()
rect1.area()

cuboid1 = cubiod(15,11,15)
cuboid1.info()
cuboid1.volume()
	
		