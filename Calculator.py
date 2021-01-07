
import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Calculator")
		self.setLayout(qtw.QVBoxLayout())
		self.setUI()

		self.show()

	def setUI(self):
		container = qtw.QWidget()
		container.setLayout(qtw.QGridLayout())

		# create input
		self.input1 = qtw.QLineEdit()
		self.input2 = qtw.QLineEdit()

		# create label
		self.operatorLabel = qtw.QLabel()
		self.resLabel = qtw.QLabel("=")

		# create the buttons
		self.btn_1 = qtw.QPushButton('1', clicked = self.ajout1)
		self.btn_2 = qtw.QPushButton('2', clicked = self.ajout2)
		self.btn_3 = qtw.QPushButton('3', clicked = self.ajout3)
		self.btn_4 = qtw.QPushButton('4', clicked = self.ajout4)
		self.btn_5 = qtw.QPushButton('5', clicked = self.ajout5)
		self.btn_6 = qtw.QPushButton('6', clicked = self.ajout6)
		self.btn_7 = qtw.QPushButton('7', clicked = self.ajout7)
		self.btn_8 = qtw.QPushButton('8', clicked = self.ajout8)
		self.btn_9 = qtw.QPushButton('9', clicked = self.ajout9)
		self.btn_0 = qtw.QPushButton('0', clicked = self.ajout0)
		self.btn_supprimer = qtw.QPushButton('C', clicked = self.supprimer)
		self.btn_addition = qtw.QPushButton('+', clicked = self.addition)
		self.btn_soustraction = qtw.QPushButton('-', clicked = self.soustraction)
		self.btn_multiplication = qtw.QPushButton('*', clicked = self.multiplication)
		self.btn_division = qtw.QPushButton('/', clicked = self.division)
		self.btn_equal = qtw.QPushButton("=", clicked = self.calcul)

		# add buttons to layout
		container.layout().addWidget(self.btn_7,2, 0 )
		container.layout().addWidget(self.btn_8,2, 1 )
		container.layout().addWidget(self.btn_9,2, 2 )

		container.layout().addWidget(self.btn_4,3, 0 )
		container.layout().addWidget(self.btn_5,3, 1 )
		container.layout().addWidget(self.btn_6,3, 2 )

		container.layout().addWidget(self.btn_1,4, 0 )
		container.layout().addWidget(self.btn_2,4, 1 )
		container.layout().addWidget(self.btn_3,4, 2 )

		container.layout().addWidget(self.btn_0,5,0, 1, 3 )
		container.layout().addWidget(self.btn_supprimer,2,3)
		container.layout().addWidget(self.btn_addition,3,3)
		container.layout().addWidget(self.btn_soustraction,3,4)
		container.layout().addWidget(self.btn_multiplication,4,3)
		container.layout().addWidget(self.btn_division,4,4)
		container.layout().addWidget(self.btn_equal,5,3)

		# add input
		container.layout().addWidget(self.input1,0,0)
		container.layout().addWidget(self.input2,0,2)

		#add label
		container.layout().addWidget(self.operatorLabel,0,1)
		container.layout().addWidget(self.resLabel,0,3)

		self.layout().addWidget(container)
	
	def onClick(self):
		qtw.QMessageBox.about(self, "HELLO", "test")

	def supprimer(self):
		self.input1.setText('')
		self.input2.setText('')
		self.operatorLabel.setText('')
		self.resLabel.setText('')
	
	def calcul(self):
		num1 = int(self.input1.text())
		num2 = int(self.input2.text())
		if self.operatorLabel.text() == '+':
			self.resLabel.setText(str(num1 + num2))
		elif self.operatorLabel.text() == '-':
			self.resLabel.setText(str(num1 - num2))
		elif self.operatorLabel.text() == '*':
			self.resLabel.setText(str(num1 * num2))
		elif self.operatorLabel.text() == '/':
			self.resLabel.setText(str(num1 / num2))

	def addition(self):
		self.operatorLabel.setText('+')

	def soustraction(self):
		self.operatorLabel.setText('-')

	def multiplication(self):
		self.operatorLabel.setText('*')

	def division(self):
		self.operatorLabel.setText('/')

	def ajout1(self):
		if self.input1.text() == '':
			self.input1.setText('1')
		elif self.input2.text() == '':
			self.input2.setText('1')
	
	def ajout2(self):
		if self.input1.text() == '':
			self.input1.setText('2')
		elif self.input2.text() == '':
			self.input2.setText('2')

	def ajout3(self):
		if self.input1.text() == '':
			self.input1.setText('3')
		elif self.input2.text() == '':
			self.input2.setText('3')

	def ajout4(self):
		if self.input1.text() == '':
			self.input1.setText('4')
		elif self.input2.text() == '':
			self.input2.setText('4')

	def ajout5(self):
		if self.input1.text() == '':
			self.input1.setText('5')
		elif self.input2.text() == '':
			self.input2.setText('5')

	def ajout6(self):
		if self.input1.text() == '':
			self.input1.setText('6')
		elif self.input2.text() == '':
			self.input2.setText('6')

	def ajout7(self):
		if self.input1.text() == '':
			self.input1.setText('7')
		elif self.input2.text() == '':
			self.input2.setText('7')

	def ajout8(self):
		if self.input1.text() == '':
			self.input1.setText('8')
		elif self.input2.text() == '':
			self.input2.setText('8')

	def ajout9(self):
		if self.input1.text() == '':
			self.input1.setText('9')
		elif self.input2.text() == '':
			self.input2.setText('9')

	def ajout0(self):
		if self.input1.text() == '':
			self.input1.setText('0')
		elif self.input2.text() == '':
			self.input2.setText('0')

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
