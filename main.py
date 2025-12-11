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








	def _launchMainLoop(self):
		while self.keepRunning:










if __name__ == "__main__":
	ChimkenzSpreadsheet("DIS_COM_UDI_2020.csv")