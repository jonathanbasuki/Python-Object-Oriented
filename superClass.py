class Hero:

	def __init__(self, name, health):
		self.name = name
		self.health = health

	def info(self):
		print("{} with health {}".format(self.name, self.health))

class Hero_mage(Hero):
	def __init__(self, name):
		super().__init__(name, 100)
		super().info()

class Hero_tank(Hero):
	def __init__(self, name):
		super().__init__(name, 200)
		super().info()

cyclops = Hero_mage("cyclops")
khurfa = Hero_tank("khurfa")