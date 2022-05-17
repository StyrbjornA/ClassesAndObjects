class Vehicle:
	name = ""
	kind = ""
	color = ""
	value = 100.00
	def __init__(self, _name, _kind, _color, _value):
		self.name = _name
		self.kind = _kind
		self.color = _color
		self.value = _value
		
	def description(self):
		desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
		return desc_str

car2 = Vehicle("Jump", "van","blue", 10000)
car1 = Vehicle("Fer", "red convertible", "red", 60000)

print(car1.description())
print(car2.description())
		