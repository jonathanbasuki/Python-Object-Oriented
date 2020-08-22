class Hero:

	def __init__(self, name, health):
		self.name = name
		self.health = health

	def info(self):
		print("{} \n\tType : Hero \n\tHealth : {}".format(self.name, self.health))

# subclass
class Mage(Hero):
	def __init__(self, name):
		super().__init__(name, 100)

# subclass
class Tank(Hero):
	def __init__(self, name):
		super().__init__(name, 200)

	def info(self):
		print("{} \n\tType : Tank \n\tHealth : {}".format(self.name, self.health))

cyclops = Mage("Cyclops")
franco = Tank("Franco")

cyclops.info()
franco.info()
