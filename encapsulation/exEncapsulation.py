class Hero:

	__jumlah = 0

	def __init__(self, name, health, power, armor):
		self.__name = name
		self.__healthBase = health
		self.__powerBase = power
		self.__armorBase = armor
		self.__level = 1
		self.__exp = 0

		self.__healthMax = self.__healthBase * self.__level
		self.__power = self.__powerBase * self.__level
		self.__armor = self.__armorBase * self.__level

		self.__health = self.__healthMax

		Hero.__jumlah += 1

	@property
	def info(self):
		return "{} level {}: \n\thealth {} \n\tpower {} \n\tarmor {}".format(self.__name, self.__level, self.__health, self.__healthMax, self.__power, self.__armor)
	
	@property
	def gainExp(self):
		pass

	@gainExp.setter
	def gainExp(self, addExp):
		self.__exp += addExp
		if (self.__exp >= 100):
			print(self.__name + " level up!")
			self.__level += 1
			self.__exp -= 100

			self.__healthMax = self.__healthBase * self.__level
			self.__power = self.__powerBase * self.__level
			self.__armor = self.__armorBase * self.__level

	def attack(self, enemy):
		self.gainExp = 40

sniper = Hero("sniper", 100, 10, 10)
axe = Hero("axe", 100, 10, 10)
print(sniper.info)

sniper.attack(axe)
sniper.attack(axe)
sniper.attack(axe)
print(sniper.info)