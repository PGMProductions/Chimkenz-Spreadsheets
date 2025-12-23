import csv
import sys


from libs.printSpreadsheet import printScreen
from libs.calculations import Grid
from libs.cursor import Cursor
from libs.terminal import ninput,Key
from libs.misc import strToBool



csv.field_size_limit(sys.maxsize)

class ChimkenzSpreadsheet:
	def __init__(self,filepath):

		self.originX = 0
		self.originY = 0


		self.options = {"autoUpdate" : True , "maxDepth" : 100 , "collumnSize" : 16}


		with open("OPTIONS.txt" , newline = "") as csvfile:
			spamreader = csv.reader(csvfile, delimiter='=', quotechar='|')
			for row in spamreader:

				if type(self.options[row[0]]) == bool:
					self.options[row[0]] = strToBool(row[1])

				elif type(self.options[row[0]]) == int:
					self.options[row[0]] = int(row[1])

		self.cursor = Cursor()
		self.grid   = Grid(self.options["maxDepth"])

		self.keepRunning = True

		with open(filepath , newline = "") as csvfile:
			spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
			rowNum = 0
			for row in spamreader:
				for collumn in range(len(row)):
					self.grid.setSquare((rowNum,collumn),row[collumn])
				rowNum += 1




		self._launchMainLoop()


	def updateScreen(self):
		"""updates what is shown on screen but not the values"""
		printScreen(self.grid.getValueGrid(),self.originX,self.originY,self.options["collumnSize"],self.cursor.X(),self.cursor.Y())            #add collumn size choosing when options are done


	def _updateValues(self):
		"""updates the values of the grid but not what is shown on screen"""
		self.grid.update()





	def _input(self):         #to do
		"""does all the input work
		waits for the user to press a key
		moves the cursor if an arrow is pressed
		types/delete text if letters or del is pressed
		"""
		command = ninput(quick = 1, simple = True) #idk, sandbuster isnt of much help

		if command == Key.UP:
			self.cursor.up()
		
		elif command == Key.DOWN:
			self.cursor.down()
		
		elif command == Key.LEFT:
			self.cursor.left()

		elif command == Key.RIGHT:
			self.cursor.right()

		elif command == Key.ENTER:
			






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
			self._newLoop_()           #unused

			if self.options["autoUpdate"] == True:
				self._preUpdateScreen_()   #unused
				self.updateScreen()
				self._postUpdateScreen_()  #unused

				self._preUpdateValues_()   #unused
				self._updateValues()
				self._postUpdateValues_()  #unused

			self._preInput_()          #unused
			self._input()
			self._postInput_()         #unused



			self._endLoop_()           #unused











if __name__ == "__main__":
	ChimkenzSpreadsheet("DIS_COM_UDI_2020.csv")