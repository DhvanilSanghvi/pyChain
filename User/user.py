class User(object):
	def __init__(self, Name, Aadhar):
		self.name = Name
		self.id = Aadhar

	def getName(self):
		return self.name

	def getID(self):
		return self.id

