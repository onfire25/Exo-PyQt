import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.counterTask = 1
		self.setWindowTitle("To Do List")
		self.setLayout(qtw.QHBoxLayout())
		self.setUI()
		self.show()
	
	def setUI(self):
		container = qtw.QWidget()
		container.setLayout(qtw.QGridLayout())

		self.input1 = qtw.QLineEdit()
		self.btn_add = qtw.QPushButton('Ajouter', clicked = self.addTask)

		container.layout().addWidget(self.input1,0,0,1,3)
		container.layout().addWidget(self.btn_add,0,3)

		self.layout().addWidget(container)


	def addTask(self):
		container = qtw.QWidget()
		container.setLayout(qtw.QGridLayout())

		self.taskLabel = qtw.QLabel(self.input1.text())
		self.btn_check = qtw.QPushButton('Pas fait', clicked = self.check)
		self.btn_supprimer = qtw.QPushButton('X', clicked = self.supprimer)

		container.layout().addWidget(self.taskLabel,self.counterTask,0,1,3)
		container.layout().addWidget(self.btn_check,self.counterTask,1)
		container.layout().addWidget(self.btn_supprimer,self.counterTask,2)

		self.layout().addWidget(container)
		self.counterTask += 1

	def supprimer(self):
		a = 0

	def check(self):
		if self.btn_check.text() == 'Pas fait':
			self.btn_check.setText('Fait')
		elif self.btn_check.text() == 'Fait':
			self.btn_check.setText('Pas fait')


app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
