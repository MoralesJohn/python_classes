# define parent class "Amimal"
class Animal(object):
	def __init__(self, nombre):
		self.name = nombre
		self.health = 100

	def walk(self):
		self.health -= 1
		return self  # allows method chaining

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print self.name, "has {} health points.".format(self.health)
		print ""

class Dog(Animal):
	def __init__(self, nombre): # still needs to capture nombre
		super(Dog, self).__init__(nombre)  # passing nombre back to __init__ in parent class
		self.health = 150

	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self, nombre):
		super(Dragon, self).__init__(nombre)
		self.health = 170

	def fly(self):
		self.health -= 10
		return self

	def displayHealth(self):
		print "This is a dragon!"
		super(Dragon, self).displayHealth()

anim1 = Animal("Anima_1")

anim1.walk().walk().walk().run().run().displayHealth()

# anim1.pet() - fails with AttributeError: 'Animal' object has no attribute 'pet'
# anim1.fly() - fails with AttributeError: 'Animal' object has no attribute 'fly'

anim2 = Dog("Fido")

anim2.walk().walk().walk().run().run().pet().displayHealth()

anim3 = Dragon("Tiamat")

anim3.walk().walk().walk().run().run().fly().fly().displayHealth()