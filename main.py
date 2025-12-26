import csv
import sys


from libs.printSpreadsheet import printScreen
from libs.calculations import Grid
from libs.cursor import Cursor
from libs.terminal import ninput,Key
from libs.misc import strToBool
from datetime import datetime



csv.field_size_limit(sys.maxsize)

class ChimkenzSpreadsheet:
	def __init__(self,filepath):
		print("__init__")
		print("Launching Chimkenz Spreadsheet")

		self.originX = 0
		self.originY = 0

		self.text = ""
		self.message = ""

		self.shouldUpdate = False

		self.skipLineAmmount = 3   #check printSpreadsheet to see what that is

		self.keepRunning = True

		self.filepath = filepath
		self.fileName = filepath.split("/")[-1]

		print("Variables initialized")

		self.options = {"autoUpdate" : True , "maxDepth" : 100 , "collumnSize" : 16}


		with open("OPTIONS.txt" , newline = "") as csvfile:
			spamreader = csv.reader(csvfile, delimiter='=', quotechar='|')
			for row in spamreader:

				if type(self.options[row[0]]) == bool:
					self.options[row[0]] = strToBool(row[1])

				elif type(self.options[row[0]]) == int:
					self.options[row[0]] = int(row[1])

		print("Options loaded")

		self.cursor = Cursor()
		self.grid   = Grid(self.options["maxDepth"])

		with open(filepath , newline = "") as csvfile:
			spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
			rowNum = 0
			for row in spamreader:
				for collumn in range(len(row)):
					self.grid.setSquare((rowNum,collumn),row[collumn])
				rowNum += 1

		print("File loaded")


		self.makeBackup()

		print("Backup made (just in case)")



		self._launchMainLoop()


	def updateScreen(self):
		"""updates what is shown on screen but not the values"""
		if self.message == "":               #to skip a line in the printing when the message takes one
			self.skipLineAmmount = 3
		else:
			self.skipLineAmmount = 4       

		printScreen(self.grid.getValueGrid(),self.originX,self.originY,self.options["collumnSize"],self.cursor.X(),self.cursor.Y(),self.skipLineAmmount)            #add collumn size choosing when options are done


	def _updateValues(self):
		"""updates the values of the grid but not what is shown on screen"""
		self.grid.update()

	def makeBackup(self):   #FIX THIS
		"""makes a backup
		remember to execute this at least 17 times per second"""
		try:
			with open(f"backups/{self.fileName.split(".")[0]}/{self.fileName} - {datetime.now()}.backup","x") as file:
				file.write(self.grid.getCSV())

		except:
			raise Exception("Well, looks like you already made a backup this one-millionth of a second... Either that or I screwed up")



	def _input(self):         #to do
		"""does all the input work
		waits for the user to press a key
		moves the cursor if an arrow is pressed
		types/delete text if letters or del is pressed
		"""
		command = ninput(quick = 1, simple = True, text = self.message, before = self.text, error = None)

		#cursor movement
		if command == Key.UP:
			self.cursor.up()

		elif command == Key.DOWN:
			self.cursor.down()

		elif command == Key.LEFT:
			self.cursor.left()

		elif command == Key.RIGHT:
			self.cursor.right()

		#commands
		elif command == Key.CTRL_U:
			self.shouldUpdate = True
			self.message = "Values Updated"

		elif command == Key.CTRL_A:
			with open(f"{self.filepath}","w") as file:
				file.write(self.grid.getCSV())





		#text
		elif command == Key.ENTER:
			self.grid.setSquare((self.cursor.Y(),self.cursor.X()),self.text)
			self.message = ""

		elif command == Key.BACKSPACE:
			self.text = self.text[:-1]
			self.message = ""

		elif command == ";":
			pass             #because semicolons are stupid and break everything
			                 #take that C#

		else:
			self.text = self.text + command
			self.message = ""




	def _start(self):
		"""executed before the main loop
		unused in the original code"""
		pass

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
		print("_launchMainLoop")

		self._updateValues()           #initializes the values grid
		print("Values calculated")

		self._start()                  #unused
		print("Main loop initialised")
		while self.keepRunning:
			self._newLoop_()           #unused



			if self.shouldUpdate:

				self._preUpdateValues_()   #unused
				self._updateValues()
				self._postUpdateValues_()  #unused
				if self.options["autoUpdate"] == False:
					self.shouldUpdate = False


			self._preUpdateScreen_()   #unused
			self.updateScreen()
			self._postUpdateScreen_()  #unused


			self._preInput_()          #unused
			self._input()
			self._postInput_()         #unused



			self._endLoop_()           #unused











if __name__ == "__main__":
	ChimkenzSpreadsheet("DIS_COM_UDI_2020.csv")