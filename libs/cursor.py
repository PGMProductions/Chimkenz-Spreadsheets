#this probably isn't too complicated
#I don't think I need to add comments, you can probably figure stuff out on your own


class Cursor:
	def __init__(self):
		self.X = 0
		self.Y = 0

	def __str__(self):
		return f"cursor at {self.X} {self.Y}"



	#setters
	def up(self):
		self.Y -= 1

	def down(self):
		self.Y += 1

	def left(self):
		self.X -= 1

	def right(self):
		self.X += 1

	def goto(self,goX,goY):
		self.X = goX
		self.Y = goY


	#getters
	def X(self):
		return self.X

	def Y(self):
		return self.Y

