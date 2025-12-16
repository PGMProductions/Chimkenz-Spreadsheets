import csv
import sys


from libs.printSpreadsheet import printScreen
from libs.calculations import Grid
from libs.cursor import Cursor


from cursor import Cursor


csv.field_size_limit(sys.maxsize)

class ChimkenzSpreadsheet:
	def __init__(self,filepath):

		self.originX = 0
		self.originY = 0

		self.cursor = Cursor()
		self.grid   = Grid()

		self.keepRunning = True

		with open(filepath , newline = "") as csvfile:
			spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
			for row in spamreader:
				for collumn in row:
					grid.setSquare((row,collumn))

		self.options = {}
		#available options are
			#autoUpdate : Bool
			

		with open("OPTIONS.txt" , newline = "") as csvfile:
			spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
			for row in spamreader:
				options[row[0]] = row[1]



		self._launchMainLoop()


	def updateScreen(self):
		"""updates what is shown on screen but not the values"""
		printScreen(self.grid.getValueGrid(),self.originX,self.originY,8,cursor.X(),cursor.Y())            #add collumn size choosing when options are done


	def _updateValues(self):
		"""updates the values of the grid but not what is shown on screen"""
		self.grid.update()





	def _input(self):         #to do
		"""does all the input work
		waits for the user to press a key
		moves the cursor when an arrow is pressed
		types/delete text when letters or del is pressed
		"""
		#waitin for sandbuster to work for me








	def _newLoop_(self):
		"""executed as the first ever method in the main loop
		unused in the original code"""
		pass

	def _preInput_(self):
		"""is executed right before _input() in main loop
		unused in the original code"""
		pass

	def _postInput_(self):
		"""is executed right after _input() in main loop
		unused in the original code"""
		pass

	def _preUpdateValues_(self):
		"""is executed right before _updateValues() in main loop
		unused in the original code"""
		pass

	def _postUpdateValues_(self):
		"""is executed right after _updateValues() in main loop
		unused in the original code"""
		pass

	def _preUpdateScreen_(self):
		"""is executed right before updateScreen() in main loop
		unused in the original code"""
		pass

	def _postUpdateScreen_(self):
		"""is executed right after updateScreen() in main loop
		unused in the original code"""
		pass

	def _endLoop_(self):
		"""executed as the last ever method in the main loop
		unused in the original code"""
		pass





	def _launchMainLoop(self):
		while self.keepRunning:
			_newLoop_()           #unused

			_preInput_()          #unused
			_input()
			_postInput_()         #unused

			_preUpdateValues_()   #unused
			_updateValues()
			_postUpdateValues_()  #unused

			_preUpdateScreen_()   #unused
 			updateScreen()
			_postUpdateScreen_()  #unused

			_endLoop_()           #unused











if __name__ == "__main__":
	ChimkenzSpreadsheet("DIS_COM_UDI_2020.csv")