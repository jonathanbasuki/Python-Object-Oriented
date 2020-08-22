class Hero:

	def __init__(self, name, health, armor):
		self.name = name
		self.__health = health
		self.__armor = armor

	# decorator property = change method to variable
	@property
	def info(self):
		return "name : {} \n\thealth : {}".format(self.name, self.__health)

	@property
	def armor(self):
		pass

	# getter = take the armor value
	@armor.getter
	def armor(self):
		return self.__armor

	# setter = set the armor value
	@armor.setter
	def armor(self, input):
		self.__armor = input

	# deleter = delete the armor value
	@armor.deleter
	def armor(self):
		print("armor deleted")
		self.__armor = None

sniper = Hero("sniper", 100, 10)

print("changing info :")
print(sniper.info)

# property
sniper.name = "rusher"
print(sniper.info)

# getter
print("getter armor :")
print(sniper.armor) 

# setter
print("setter armor :")
sniper.armor = 50
print(sniper.armor)

# deleter
print("delete armor :")
del sniper.armor

print(sniper.__dict__)
