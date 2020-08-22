class Team:

	def setTeam(self, team):
		self.team = team

	def showTeam(self):
		print(self.team)

class Type:

	def setType(self, type):
		self.type = type

	def showType(self):
		print(self.type)

class Hero(Team, Type):

	def __init__(self, name, health):
		self.name = name
		self.health = health

nana = Hero("Nana", 100)
nana.setTeam("Red Team")
nana.setType("Support")

nana.showTeam()
nana.showType()