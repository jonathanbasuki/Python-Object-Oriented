class Hero:

	def __init__(self, name, health):
		self.name = name
		self.health = health

class Hero_mage(Hero):
	pass

class Hero_tank(Hero):
	pass

granger = Hero("granger", 100)
cyclops = Hero_mage("cyclops", 80)
khufra = Hero_tank("khufra", 200)

print(granger.name)
print(cyclops.health)
print(khufra.name)