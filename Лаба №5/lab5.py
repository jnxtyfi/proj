class Book():
	title = None
	author = None
	year = None
	def set_info(self, title, author, year):
		self.title = title
		self.author = author
		self.year = year
	def get_info(self):
		print(str('Название книги: \"' + self.title + '\", Автор: \"' + self.author + '\", Год издания: \"' + self.year + '\"'))

tom = Book()
tom.set_info("Война и мир", "Л. Н. Толстой", "1865")
tom.get_info()




class Circle():

	def __init__(self, radius):
		self.radius = radius
	def __dict__(self, rad, z):
		self.rad = rad
		self.z = z
	def get_radius(self):
		print(self.radius)
	def set_radius(self, new_radius):
		self.radius = new_radius

circ = Circle(16)
circ.get_radius()

circ.set_radius(40)
circ.get_radius()

print(Book.title)

