from libs.misc import isNumber
from libs.printSpreadsheet import nameCollumn


DEBUGGRID = False

if DEBUGGRID:
	from libs.printSpreadsheet import printScreen


class Grid:
	def __init__(self,maxDepth,width = 1,height = 1):
		"""basically, this is a big, 2 dimensions list of the squares defined bellow"""
		self.width = width
		self.height = height
		self.content = [[Square() for _  in range(width)]for _ in range(height)] #content grid

		self.maxDepth = maxDepth

		self.valuesDict = {}                                                     #value dictionary
		self.toCalculate = {}

		self.valuesGrid = []                                                     #value grid

	def __str__(self):                         #ig now ik it works, because getCSV
		finalList = []
		for liste in self.content:
			tempList = []
			for square in liste:
				tempList.append(square.getContent())
			finalList.append(" | ".join(tempList))
		return "\n".join(finalList)


	#useful funcs

	def _nameToPos(self,name):          #fairily simple, shouldn't cause problems
		"""ya give name like A7 (string obviously) and it returns position in list like (7,0)"""
		collumn = ""
		row = ""

		for i in range(len(name)):
			if name[:i].isalpha():
				collumn = name[:i]
				row = name[i:]

		collumn = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25,"AA":26,"AB":27,"AC":28,"AD":29,"AE":30,"AF":31,"AG":32,"AH":33,"AI":34,"AJ":35,"AK":36,"AL":37,"AM":38,"AN":39,"AO":40,"AP":41,"AQ":42,"AR":43,"AS":44,"AT":45,"AU":46,"AV":47,"AW":48,"AX":49,"AY":50,"AZ":51,"BA":52,"BB":53,"BC":54,"BD":55,"BE":56,"BF":57,"BG":58,"BH":59,"BI":60,"BJ":61,"BK":62,"BL":63,"BM":64,"BN":65,"BO":66,"BP":67,"BQ":68,"BR":69,"BS":70,"BT":71,"BU":72,"BV":73,"BW":74,"BX":75,"BY":76,"BZ":77,"CA":78,"CB":79,"CC":80,"CD":81,"CE":82,"CF":83,"CG":84,"CH":85,"CI":86,"CJ":87,"CK":88,"CL":89,"CM":90,"CN":91,"CO":92,"CP":93,"CQ":94,"CR":95,"CS":96,"CT":97,"CU":98,"CV":99,"CW":100,"CX":101,"CY":102,"CZ":103,"DA":104,"DB":105,"DC":106,"DD":107,"DE":108,"DF":109,"DG":110,"DH":111,"DI":112,"DJ":113,"DK":114,"DL":115,"DM":116,"DN":117,"DO":118,"DP":119,"DQ":120,"DR":121,"DS":122,"DT":123,"DU":124,"DV":125,"DW":126,"DX":127,"DY":128,"DZ":129,"EA":130,"EB":131,"EC":132,"ED":133,"EE":134,"EF":135,"EG":136,"EH":137,"EI":138,"EJ":139,"EK":140,"EL":141,"EM":142,"EN":143,"EO":144,"EP":145,"EQ":146,"ER":147,"ES":148,"ET":149,"EU":150,"EV":151,"EW":152,"EX":153,"EY":154,"EZ":155,"FA":156,"FB":157,"FC":158,"FD":159,"FE":160,"FF":161,"FG":162,"FH":163,"FI":164,"FJ":165,"FK":166,"FL":167,"FM":168,"FN":169,"FO":170,"FP":171,"FQ":172,"FR":173,"FS":174,"FT":175,"FU":176,"FV":177,"FW":178,"FX":179,"FY":180,"FZ":181,"GA":182,"GB":183,"GC":184,"GD":185,"GE":186,"GF":187,"GG":188,"GH":189,"GI":190,"GJ":191,"GK":192,"GL":193,"GM":194,"GN":195,"GO":196,"GP":197,"GQ":198,"GR":199,"GS":200,"GT":201,"GU":202,"GV":203,"GW":204,"GX":205,"GY":206,"GZ":207,"HA":208,"HB":209,"HC":210,"HD":211,"HE":212,"HF":213,"HG":214,"HH":215,"HI":216,"HJ":217,"HK":218,"HL":219,"HM":220,"HN":221,"HO":222,"HP":223,"HQ":224,"HR":225,"HS":226,"HT":227,"HU":228,"HV":229,"HW":230,"HX":231,"HY":232,"HZ":233,"IA":234,"IB":235,"IC":236,"ID":237,"IE":238,"IF":239,"IG":240,"IH":241,"II":242,"IJ":243,"IK":244,"IL":245,"IM":246,"IN":247,"IO":248,"IP":249,"IQ":250,"IR":251,"IS":252,"IT":253,"IU":254,"IV":255,"IW":256,"IX":257,"IY":258,"IZ":259,"JA":260,"JB":261,"JC":262,"JD":263,"JE":264,"JF":265,"JG":266,"JH":267,"JI":268,"JJ":269,"JK":270,"JL":271,"JM":272,"JN":273,"JO":274,"JP":275,"JQ":276,"JR":277,"JS":278,"JT":279,"JU":280,"JV":281,"JW":282,"JX":283,"JY":284,"JZ":285,"KA":286,"KB":287,"KC":288,"KD":289,"KE":290,"KF":291,"KG":292,"KH":293,"KI":294,"KJ":295,"KK":296,"KL":297,"KM":298,"KN":299,"KO":300,"KP":301,"KQ":302,"KR":303,"KS":304,"KT":305,"KU":306,"KV":307,"KW":308,"KX":309,"KY":310,"KZ":311,"LA":312,"LB":313,"LC":314,"LD":315,"LE":316,"LF":317,"LG":318,"LH":319,"LI":320,"LJ":321,"LK":322,"LL":323,"LM":324,"LN":325,"LO":326,"LP":327,"LQ":328,"LR":329,"LS":330,"LT":331,"LU":332,"LV":333,"LW":334,"LX":335,"LY":336,"LZ":337,"MA":338,"MB":339,"MC":340,"MD":341,"ME":342,"MF":343,"MG":344,"MH":345,"MI":346,"MJ":347,"MK":348,"ML":349,"MM":350,"MN":351,"MO":352,"MP":353,"MQ":354,"MR":355,"MS":356,"MT":357,"MU":358,"MV":359,"MW":360,"MX":361,"MY":362,"MZ":363,"NA":364,"NB":365,"NC":366,"ND":367,"NE":368,"NF":369,"NG":370,"NH":371,"NI":372,"NJ":373,"NK":374,"NL":375,"NM":376,"NN":377,"NO":378,"NP":379,"NQ":380,"NR":381,"NS":382,"NT":383,"NU":384,"NV":385,"NW":386,"NX":387,"NY":388,"NZ":389,"OA":390,"OB":391,"OC":392,"OD":393,"OE":394,"OF":395,"OG":396,"OH":397,"OI":398,"OJ":399,"OK":400,"OL":401,"OM":402,"ON":403,"OO":404,"OP":405,"OQ":406,"OR":407,"OS":408,"OT":409,"OU":410,"OV":411,"OW":412,"OX":413,"OY":414,"OZ":415,"PA":416,"PB":417,"PC":418,"PD":419,"PE":420,"PF":421,"PG":422,"PH":423,"PI":424,"PJ":425,"PK":426,"PL":427,"PM":428,"PN":429,"PO":430,"PP":431,"PQ":432,"PR":433,"PS":434,"PT":435,"PU":436,"PV":437,"PW":438,"PX":439,"PY":440,"PZ":441,"QA":442,"QB":443,"QC":444,"QD":445,"QE":446,"QF":447,"QG":448,"QH":449,"QI":450,"QJ":451,"QK":452,"QL":453,"QM":454,"QN":455,"QO":456,"QP":457,"QQ":458,"QR":459,"QS":460,"QT":461,"QU":462,"QV":463,"QW":464,"QX":465,"QY":466,"QZ":467,"RA":468,"RB":469,"RC":470,"RD":471,"RE":472,"RF":473,"RG":474,"RH":475,"RI":476,"RJ":477,"RK":478,"RL":479,"RM":480,"RN":481,"RO":482,"RP":483,"RQ":484,"RR":485,"RS":486,"RT":487,"RU":488,"RV":489,"RW":490,"RX":491,"RY":492,"RZ":493,"SA":494,"SB":495,"SC":496,"SD":497,"SE":498,"SF":499,"SG":500,"SH":501,"SI":502,"SJ":503,"SK":504,"SL":505,"SM":506,"SN":507,"SO":508,"SP":509,"SQ":510,"SR":511,"SS":512,"ST":513,"SU":514,"SV":515,"SW":516,"SX":517,"SY":518,"SZ":519,"TA":520,"TB":521,"TC":522,"TD":523,"TE":524,"TF":525,"TG":526,"TH":527,"TI":528,"TJ":529,"TK":530,"TL":531,"TM":532,"TN":533,"TO":534,"TP":535,"TQ":536,"TR":537,"TS":538,"TT":539,"TU":540,"TV":541,"TW":542,"TX":543,"TY":544,"TZ":545,"UA":546,"UB":547,"UC":548,"UD":549,"UE":550,"UF":551,"UG":552,"UH":553,"UI":554,"UJ":555,"UK":556,"UL":557,"UM":558,"UN":559,"UO":560,"UP":561,"UQ":562,"UR":563,"US":564,"UT":565,"UU":566,"UV":567,"UW":568,"UX":569,"UY":570,"UZ":571,"VA":572,"VB":573,"VC":574,"VD":575,"VE":576,"VF":577,"VG":578,"VH":579,"VI":580,"VJ":581,"VK":582,"VL":583,"VM":584,"VN":585,"VO":586,"VP":587,"VQ":588,"VR":589,"VS":590,"VT":591,"VU":592,"VV":593,"VW":594,"VX":595,"VY":596,"VZ":597,"WA":598,"WB":599,"WC":600,"WD":601,"WE":602,"WF":603,"WG":604,"WH":605,"WI":606,"WJ":607,"WK":608,"WL":609,"WM":610,"WN":611,"WO":612,"WP":613,"WQ":614,"WR":615,"WS":616,"WT":617,"WU":618,"WV":619,"WW":620,"WX":621,"WY":622,"WZ":623,"XA":624,"XB":625,"XC":626,"XD":627,"XE":628,"XF":629,"XG":630,"XH":631,"XI":632,"XJ":633,"XK":634,"XL":635,"XM":636,"XN":637,"XO":638,"XP":639,"XQ":640,"XR":641,"XS":642,"XT":643,"XU":644,"XV":645,"XW":646,"XX":647,"XY":648,"XZ":649,"YA":650,"YB":651,"YC":652,"YD":653,"YE":654,"YF":655,"YG":656,"YH":657,"YI":658,"YJ":659,"YK":660,"YL":661,"YM":662,"YN":663,"YO":664,"YP":665,"YQ":666,"YR":667,"YS":668,"YT":669,"YU":670,"YV":671,"YW":672,"YX":673,"YY":674,"YZ":675,"ZA":676,"ZB":677,"ZC":678,"ZD":679,"ZE":680,"ZF":681,"ZG":682,"ZH":683,"ZI":684,"ZJ":685,"ZK":686,"ZL":687,"ZM":688,"ZN":689,"ZO":690,"ZP":691,"ZQ":692,"ZR":693,"ZS":694,"ZT":695,"ZU":696,"ZV":697,"ZW":698,"ZX":699,"ZY":700,"ZZ":701}[collumn]
        #hardcoded by program, go to libs/printSpreadsheet.py for more info
        #yes it is stupid, yes its impossible to read, but collumns names are annoying

		return int(row),collumn

	def _posToName(self,row,collumn):   #simple af
		return nameCollumn(collumn) + str(row)	

	def _addLine(self):
		"""adds a line at the bottom of the content grid"""
		self.content.append([Square() for _ in self.content[0]])      #adds a line as long as the first

	def _addCollumn(self):
		"""adds a collumn at the end of every line"""
		for line in self.content:
			line.append(Square())

	def isLongEnough(self,collumn):
		"""returns if the grid is long enough to include the given collumn"""
		return collumn < len(self.content[0])

	def isTallEnough(self,line):
		"""returns if the grid is tall enough to incude the given line"""
		return line < len(self.content)

	#setters and getters


	def setSquare(self,square,value):
		"""sets a square
		you can pass the name of the square or a tuple with its coordinates (row,collumn)
		makes the grid bigger if needed"""

		if type(square) == str:
			squarePos = self._nameToPos(square)
		else:
			squarePos = square

		while not self.isLongEnough(squarePos[1]):   #adds collumns until the square is in the grid
			self._addCollumn()

		while not self.isTallEnough(squarePos[0]):   #adds lines until the square is in the grid
			self._addLine()


		self.content[squarePos[0]][squarePos[1]].setContent(value)


	def getValueGrid(self):
		"""returns the grid of content WITHOUT UPDATING
		you likely wana run update() before using this"""
		return self.valuesGrid

	def getValueDict(self):
		"""can be much samller but also harder to work with
		I put that here in case but I dont use it"""
		return self.valuesDict

	def getCSV(self):
		"""returns the string of the grid's content in csv form"""
		finalList = []
		for liste in self.content:
			tempList = []
			for square in liste:
				tempList.append(square.getContent())
			finalList.append(";".join(tempList))
		return "\n".join(finalList)







    #all the methods of the update cyle

	def update(self, updateGrid = True):                   #done, pretty simple
		"""updates the values dictionary and potentially the grid"""
		self.valuesDict = {}

		self._firstCycle()

		depth = 0
		while (not self._isFinished()) and depth < self.maxDepth:
			self._otherCycles()
			depth += 1

		if depth >= self.maxDepth:           #executes only if the calculations stopped because the max depth was reached and not when calculations are done
			raise Exception("max depth reached")
		if updateGrid:
			self._updateValuesGrid()




	def _updateValuesGrid(self):
		"""updates the variable valuesGrid"""
		self.valuesGrid = []

		for row in range(len(self.content)):
			rowList = []
			for collumn in range(len(self.content[row])):
				rowList.append(self.valuesDict[self._posToName(row,collumn)])               #self.content[row][collumn]    will be every square of the spreadsheet
			self.valuesGrid.append(rowList)


	def _firstCycle(self):             #pretty ugly
		"""this is to do all of the quick , independent Squares"""
		for row in range(len(self.content)):
			for collumn in range(len(self.content[row])):
				if self.content[row][collumn].isIndependant():                                     #self.content[row][collumn]    will be every square of the spreadsheet
					self.valuesDict[self._posToName(row,collumn)] = self.content[row][collumn].getValue(self.valuesDict)

				else:

					self.toCalculate[self._posToName(row,collumn)] = self.content[row][collumn]



		if DEBUGGRID:                                                                              print("First Cycle finished : " + str(self.valuesDict))

	def _otherCycles(self):            #works in a pretty weird order BUT that shouldn't cause any problems
		"""does all the squares it can do
		regardless of order
		it will do them in the order of the list of squares to do and if one later in the list requires only one previously in the list, it will be able to calculate"""
		for name,square in self.toCalculate.items():
			if DEBUGGRID:                                                                              print(f"toCalculate : {str(self.toCalculate[name])}")
			if square.isCalculatable(self.valuesDict):
				self.valuesDict[name] =	square.getValue(self.valuesDict)
		if DEBUGGRID:                                                                              print("Cycle finished : " + str(self.valuesDict))


	def _isFinished(self):
		for row in range(len(self.content)):
			for collumn in range(len(self.content[row])):
				if not self._posToName(row,collumn) in self.valuesDict:
					return False
		return True






DEBUGSQARE = False

#values is a dictionary

class Square:                                           #finished
	def __init__(self):
		self.content = ""
		self.value = 0

	def __str__(self):
		return f"{self.content} -> {self.quickGetValue()}"




	def quickGetValue(self):                              #single line
		"""to get the value without updating it, use carefully"""
		return self.value

	def getValue(self,values):                            #single line
		"""to update the value then get it, slow but safe"""
		self.updateValue(values)
		return self.value

	def updateValue(self,values):                         #not that simple but "thourougly" tested

		if DEBUGSQARE:                                              print(f"updateValue {values}")

		if self.content == "":
			self.value = None

		elif self.content[0] == "=":  #only tries to do calculations if the first character is = and the square isnt empty

			localContent = self.content                        #a local copy of self.content for the method to not modify it outside 

			if not self.isIndependant():                       #saves some performance (probably)
				for square,value in values.items():

					if DEBUGSQARE:                                  print(str(square) + " UwU " + str(value))
					localContent = localContent.replace(square,str(value))

			if DEBUGSQARE:                                          print(localContent)
			exec(f"self.value = {localContent[1:]}")           #gets rid of the beggining =
		else:
			self.value = self.content

	def setContent(self,content):                         #single line
		self.content = content

	def getContent(self):
		"""self explanatory"""
		return self.content




	def getOtherSquare(self,values,square):               #single line, unused
		return values[square]


	def isIndependant(self):
		"""returns true if the square can run without any other squares being calculated
		dont run this on a text square (a square with text and that doesn't beggin with a =)"""
		if self.content == "" or not self.content[0] == "=":
			return True                        #if the square is just a str, it can always run on its own
		else:
			for letter in ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"):
				if letter in self.content:     #if any of those letters are in the content, it means that a collumn name is inputed
					return False
			return True                             #fairily simple, shouldn't cause problems

	def listRequiredSquares(self):                          #untested and complicated, if there's a problem, look here                Fixed, maybe
		"""returns a list of all the squares that need to be calculated in order to calculate that one
		dont run this on a text square (a square with text and that doesn't beggin with a =)"""
		pointer = 0
		requiredSquares = []
		while pointer < len(self.content):

			if self.content[pointer].isalpha():            #if the pointer is on a letter

				#getting 1 collumn name
				lenght = 1
				if self.content[pointer+1].isalpha():      #if the thing after the pointer is a letter (the collumn names can be up to 2 letters)
					lenght = 2
				tempPointer = pointer+lenght
				while tempPointer < lenght and isNumber(self.content[tempPointer]):      #adds as many chars as there are numbers
					lenght += 1
					tempPointer += 1

				requiredSquares.append(self.content[pointer:pointer+lenght+1])             #+1 cuz the second number is excluded
				pointer += lenght                          #puts the pointer after the collumn name to not add both AA1 and A1 when there is AA1

			else:
				pointer += 1

		return requiredSquares



	def isCalculatable(self,values):                       #fairily simple but relies on listRequiredSquares()
		"""returns True if all the collumn names of the square are indexes in the values dictionary
		dont run this on a text square (a square with text and that doesn't beggin with a =)"""

		requiredSquares = self.listRequiredSquares()
		if DEBUGGRID:                                       print(requiredSquares)
		for name in requiredSquares:
			if not name in values:
				return False

		return True








if __name__ == "__main__":
	assert Grid(0,0,0)._nameToPos("A8") == (8,0)
	assert Grid(0,0,0)._posToName(8,0) == "A8"

	a = Square()
	a.setContent("=5*5")
	assert a.isIndependant() == True
	assert a.getValue({"A1" : 7}) == 25


	a.setContent("=A1*5")
	assert a.isIndependant() == False
	assert a.getValue({"A1" : 7}) == 35


	a.setContent("=((A1*B3)+32)**2")
	assert a.isIndependant() == False
	assert a.getValue({"A1" : 2 , "B3" : 4}) == 1600


	a.setContent("=min(A1,B3,Y7)")
	assert a.isIndependant() == False
	assert a.getValue({"A1" : 2 , "B3" : 4 , "Y7" : -12}) == -12

	b = Grid(15,15,100)
	b.setSquare("A1","=7")
	b.setSquare("A2","=8")
	b.setSquare("B1","=A1*A2")       #turn on DEBUGGRID for those

	b.update()

	b.setSquare("A9","=9")
	b.setSquare("H10","=B1*H2")
	b.setSquare("H2","=19")

