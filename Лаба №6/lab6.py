class UserAccount():
	email = None
	login = None
	password = None
	def __init__(self, password, email, login):
		self.password = password
		self.email = email
		self.login = login
	def set_password(self, new_password):
		self.password = new_password
	def check_password(self, password):
		print(password == self.password)
User = UserAccount("qwerty123", "megamozg@gmail.com", "Crutoy_tipochek228")

User.set_password("abc3234")
User.check_password("qwerty123")

User.check_password("abc3234")


