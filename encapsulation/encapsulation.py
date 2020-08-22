class Hero:

	def __init__(self, name, health, power):
		self.__name = name
		self.__health = health
		self.__power = power

	# getter
	def getName(self):
		return self.__name

	def getHealth(self):
		return self.__health

	# setter
	def attack(self, damage):
		self.__health -= damage

sniper = Hero("sniper", 100, 10)

print(sniper.getName())
print(sniper.getHealth())
sniper.attack(5)
print(sniper.getHealth())