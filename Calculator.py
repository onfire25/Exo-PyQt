
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
		valueInput1 = qtw.QLineEdit()
		valueInput2 = qtw.QLineEdit()

		# create label
		operatorLabel = qtw.QLabel()
		resLabel = qtw.QLabel("=")

		# create the buttons
		btn_1 = qtw.QPushButton('1')
		btn_2 = qtw.QPushButton('2')
		btn_3 = qtw.QPushButton('3')
		btn_4 = qtw.QPushButton('4')
		btn_5 = qtw.QPushButton('5')
		btn_6 = qtw.QPushButton('6')
		btn_7 = qtw.QPushButton('7')
		btn_8 = qtw.QPushButton('8')
		btn_9 = qtw.QPushButton('9')
		btn_0 = qtw.QPushButton('0', clicked = self.onClick)
		btn_equal = qtw.QPushButton("=", clicked = self.calcul)

		# add buttons to layout
		container.layout().addWidget(btn_7,2, 0 )
		container.layout().addWidget(btn_8,2, 1 )
		container.layout().addWidget(btn_9,2, 2 )

		container.layout().addWidget(btn_4,3, 0 )
		container.layout().addWidget(btn_5,3, 1 )
		container.layout().addWidget(btn_6,3, 2 )

		container.layout().addWidget(btn_1,4, 0 )
		container.layout().addWidget(btn_2,4, 1 )
		container.layout().addWidget(btn_3,4, 2 )

		container.layout().addWidget(btn_0,5,0, 1, 3 )
		container.layout().addWidget(btn_equal,5,4)

		# add input
		container.layout().addWidget(valueInput1,0,0)
		container.layout().addWidget(valueInput2,0,2)

		#add label
		container.layout().addWidget(operatorLabel,0,1)
		container.layout().addWidget(resLabel,0,3)

		self.layout().addWidget(container)
	
	def onClick(self):
		qtw.QMessageBox.about(self, "HELLO", "test")
	
	def calcul(self):
		num1 = int(self.input1.text())
		num2 = int(self.input2.text())
		self.resLabel.setText(str(num1 + num2))

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
