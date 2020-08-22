class Hero:

	def __init__(self, name, health, armor):
		self.name = name
		self.__health = health
		self.__armor = armor
		#self.info = "name : {} \n\thealth : {}".format(self.name, self.__health)

	# decorator properti = mengubah method menjadi variable
	@property
	def info(self):
		return "name : {} \n\thealth : {}".format(self.name, self.__health)

	@property
	def armor(self):
		pass

	# getter
	# mengambil nilai armor
	@armor.getter
	def armor(self):
		return self.__armor

	# setter
	# men-setting nilai armor
	@armor.setter
	def armor(self, input):
		self.__armor = input

	# deleter
	# menghapus nilai armor
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