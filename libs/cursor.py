#this probably isn't too complicated
#I don't think I need to add comments, you can probably figure stuff out on your own


class Cursor:
	def __init__(self):
		self.x = 0
		self.y = 0

	def __str__(self):
		return f"cursor at {self.x} {self.y}"



	#setters
	def up(self):
		self.y -= 1

	def down(self):
		self.y += 1

	def left(self):
		self.x -= 1

	def right(self):
		self.x += 1

	def goto(self,gox,goy):
		self.x = gox
		self.y = goy


	#getters
	def X(self):
		return self.x

	def Y(self):
		return self.y

