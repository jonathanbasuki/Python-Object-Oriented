from abc import ABC, abstractmethod

class Button(ABC):
	"""docstring for Button"""
	def __init__(self, link):
		self.link = link

	@abstractmethod
	def Click(self):
		pass

	@property
	@abstractmethod
	def link(self):
		pass

class RadioButton(Button):
	"""docstring for RadioButton"""
	def Click(self):
		print("Link to : {}".format(self.link))

	@Button.link.setter
	def link(self, input):
		self.__link = input

	@link.getter
	def link(self):
		return self.__link

button1 = RadioButton("www.instagram.com/jonathanbasuki")
button1.Click()	
