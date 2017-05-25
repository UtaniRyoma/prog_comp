from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
	QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
	QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
	QVBoxLayout)

import sys

class Dialog(QDialog):
	NumGridRows = 11
	NumButtons = 4

	def __init__(self):
		super(Dialog, self).__init__()
		self.createFormGroupBox()
	
		buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
		buttonBox.accepted.connect(self.accept)
		buttonBox.rejected.connect(self.reject)

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(self.formGroupBox)
		mainLayout.addWidget(buttonBox)
		self.setLayout(mainLayout)

		self.setWindowTitle("Vote detail")
 
	def createFormGroupBox(self):
		self.formGroupBox = QGroupBox("Input form")
		theme=QLineEdit()
		choice1=QLineEdit()
		choice2=QLineEdit()
		choice3=QLineEdit()
		choice4=QLineEdit()
		votemember1=QComboBox()
		votemember2=QComboBox()
		votemember3=QComboBox()
		votemember4=QComboBox()
		monthofdeadline=QSpinBox()
		dayofdeadline=QSpinBox()
	
		votemember1.addItems(["a","b","c","d"])
		votemember2.addItems(["a","b","c","d"])
		votemember3.addItems(["a","b","c","d"])
		votemember4.addItems(["a","b","c","d"])
	
		monthofdeadline.setRange(1,12)
		dayofdeadline.setRange(1,31)

		monthofdeadline.setSingleStep(1)
		dayofdeadline.setSingleStep(1)


		layout = QFormLayout()
		layout.addRow(QLabel("Theme:"), theme)
		layout.addRow(QLabel("First vote member:"), votemember1)
		layout.addRow(QLabel("Second vote member:"), votemember2)
		layout.addRow(QLabel("Third vote member:"), votemember3)
		layout.addRow(QLabel("Fourth vote member:"), votemember4)
		layout.addRow(QLabel("First choice:"), choice1)
		layout.addRow(QLabel("Second choice:"), choice2)
		layout.addRow(QLabel("Third choice:"), choice3)
		layout.addRow(QLabel("Fourth choice:"), choice4)
		layout.addRow(QLabel("Month deadline:"), monthofdeadline)
		layout.addRow(QLabel("Day deadline:"), dayofdeadline)
		self.formGroupBox.setLayout(layout)

	def accept(self):
		usersname ="%s,%s,%s,%s"%(votemember1.text,votemember2.text,votemember3.text,votemember4.text)
		choices ="%s,%s,%s,%s"%(choice1.currentText,choice2.currentText,choice3.currentText,choice4.currentText)
		today =datetime.date.today()
		deadline = "%s/%s/%s"%(today.strtime('%Y'),monthofdeadline.value,dayofdeadline.value)
		con = lite.connect('mes.db')
		with con:
			cur = con.cursor()    
			cur.execute("INSERT INTO vote VALUES(%s,%s,%s,%s,%s,%s)"%(theme.text,usersname,choices,deadline,votedmember,owner))
		con.close()




if __name__ == '__main__':
	app = QApplication(sys.argv)
	dialog = Dialog()
sys.exit(dialog.exec_())
