# abc = abtract base class
from abc import ABC, abstractmethod
class Button(ABC):
	"""docstring for Button"""
	@abstractmethod
	def Click(self):
		pass

class RadioButton(Button):
		"""docstring for RadioButton"""
		def Click(self):
			print("Radio Button worked")
				
class Checkbox(Button):
		"""docstring for CheckBox"""
		def Click(self):
			print("Checkbox worked")

button1 = RadioButton()
button2 = Checkbox()
button1.Click()
button2.Click()						