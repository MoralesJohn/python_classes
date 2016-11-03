
class MathDojo(object):
	def __init__(self):
		self.value = 0

	def subadd(self, elem):
		try:
			self.value += elem
		except TypeError:
			self.value += sum(elem)
		return self

	def subsub(self, elem):
		try:
			self.value -= elem
		except TypeError:
			self.value -= sum(elem)
		return self

	def add(self, *more):
		if type(more) == "Int":
			self.value += more
		else:
			for i in range (0, len(more)):
				self.subadd(more[i])
		return self

	def subtract(self, *more):
		if type(more) == "Int":
			self.value -= more
		else:
			for i in range (0, len(more)):
				self.subsub(more[i])
		return self

md = MathDojo()

md.add(5).add(10, [10,10],10)
print md.value
md.add(30, [15,25], [25,25])
print md.value
md.subtract([1,1],1)
print md.value

