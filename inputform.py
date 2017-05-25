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
	theme.detail=QLineEdit()
	choice1.detail=QLineEdit()
	choice2.detail=QLineEdit()
	choice3.detail=QLineEdit()
	choice4.detail=QLineEdit()
	votemember1.member=QComboBox()
	votemember2.member=QComboBox()
	votemember3.member=QComboBox()
	votemember4.member=QComboBox()
	monthofdeadline.number=QSpinBox()
	dayofdeadline.number=QSpinBox()
	
	choice1.detail.addItems(user)
	choice2.detail.addItems(user)
	choice3.detail.addItems(user)
	choice4.detail.addItems(user)
	
	monthofdeadline.number.setRange(1,12)
	dayofdeadline.number.setRange(1,31)

	monthofdeadline.number.setSingleStep(1)
	dayofdeadline.number.setSingleStep(1)

        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        layout.addRow(QLabel("Theme:"), theme.detail)
        layout.addRow(QLabel("First vote member:"), votemember1.member)
	layout.addRow(QLabel("Second vote member:"), votemember2.member)
	layout.addRow(QLabel("Third vote member:"), votemember3.member)
	layout.addRow(QLabel("Fourth vote member:"), votemember4.member)
	layout.addRow(QLabel("First choice:"), choice1.detail)
	layout.addRow(QLabel("Second choice:"), choice2.detail)
	layout.addRow(QLabel("Third choice:"), choice3.detail)
	layout.addRow(QLabel("Fourth choice:"), choice4.detail)
        layout.addRow(QLabel("Month deadline:"), monthofdeadline.number)
        layout.addRow(QLabel("Day deadline:"), dayofdeadline.number)
        self.formGroupBox.setLayout(layout)

    def accept(self):
	usersname ="%s,%s,%s,%s"%(votemember1.member.text,votemember2.member.text,votemember3.member.text,votemember4.member.text)
	choices ="%s,%s,%s,%s"%(choice1.detail.currentText,choice2.detail.currentText,choice3.detail.currentText,choice4.detail.currentText)
	today =datetime.date.today()
	deadline = "%s/%s/%s"%(today.strtime('%Y'),monthofdeadline.number.value,dayofdeadline.number.value)
	con = lite.connect('mes.db')
	with con:
    		cur = con.cursor()    
    		cur.execute("INSERT INTO vote VALUES(%s,%s,%s,%s,%s,%s)"%(theme.detail.text,usersname,choices,deadline,votedmember,owner))
	con.close()
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
sys.exit(dialog.exec_())
