class HP:
	"""docstring for HP"""
	def __init__(self, nama, price):
		self.nama = nama
		self.price = price

	# biasanya untuk debuggin
	def __repr__(self):
		return "Debug - iPhone : {} Price : {}M".format(self.nama, self.price)

	# biasanya dipake setelah debuggin
	def __str__(self):
		return "iPhone : {} Price : {}M".format(self.nama, self.price)

	# magic method aritmatik (+)
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
print(iphone.__dict__)