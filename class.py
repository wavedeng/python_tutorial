class Person:
	def __init__(self,name,height,weight):
		self.name = name
		self.height = height
		self.weight = weight

	def say_name(self):
		print("我的名字叫"+self.name)

	def say_hello(self,target_name):
		print("我叫"+self.name+",很高兴见到你"+target_name)


person1 = Person("老张",170,100)
person2 = Person("老王",160,80)


person1.say_hello("老邓")
# person1.say_name()
# person2.say_name()

