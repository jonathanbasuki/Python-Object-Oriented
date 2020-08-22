class HP:
	"""docstring for HP"""
	def __init__(self, name, price):
		self.name = name
		self.price = price

	# used for debuggin
	def __repr__(self):
		return "Debug - iPhone : {} Price : {}M".format(self.name, self.price)

	# used after debuggin
	def __str__(self):
		return "iPhone : {} Price : {}M".format(self.name, self.price)

	# magic method = arithmetic
	def __add__(self, object):
		return self.price + object.price

	@property
	def __dict__(self):
		return "This object has Name and Price"
		
iphone = HP("iPhone 11 Pro Max", 19)
samsung = HP("Samsung Galaxy Note 20 Ultra", 19)

print(iphone)
print(samsung)
print(iphone + samsung)
