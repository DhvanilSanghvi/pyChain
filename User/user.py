class User(object):
	def __init__(self, Name, Aadhar, Age):
		self.name = Name
		self.id = Aadhar
		self.age = Age
		
	def getName(self):
		return self.name
	def getID(self):
		return self.id
	def getAge(self):
		return self.age

class Patient(User):
	def __init__(self, Name, Aadhar, Requirement, areaOfResidence, Age, Insurer=None):
		User.__init__(self, Name, Aadhar, Age)
		self.requirement= Requirement 		# Requirement is the req. of the user -> i.e for what purpose does he need assistance
		self.area = areaOfResidence
		self.insurer = Insurer 				# None, or the name of the company from which insurance is taken

	def getRequirement(self):	
		return self.requirement
	def getAreaOfResidence(self):
		return self.area
	def getInsurer(self):
		return self.insurer


