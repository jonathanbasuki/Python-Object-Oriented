class Hero:

	__total = 0

	def __init__(self, name):
		self.__name = name
		Hero.__total += 1

	# method untuk objek
	def getTotal(self):
		return Hero.__total

	# method untuk class
	def getJTotal1():
		return Hero.__total

	# method static
	@staticmethod
	def getTotal2():
		return Hero.__total

	# class method
	@classmethod
	def getTotal3(cls):
			return cls.__total

sniper = Hero("sniper")
print(Hero.getTotal2())
tank = Hero("tank")
print(tank.getTotal2())
rusher = Hero("rusher")
print(Hero.getTotal3())