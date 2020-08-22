class Hero:

	def __init__(self, name, health):
		self.name = name
		self.health = health

	def info(self):
		print("{} with health {}".format(self.name, self.health))

class HeroMage(Hero):
	def __init__(self, name):
		super().__init__(name, 100)
		super().info()

class HeroTank(Hero):
	def __init__(self, name):
		super().__init__(name, 200)
		super().info()

cyclops = HeroMage("cyclops")
khurfa = HeroTank("khurfa")
