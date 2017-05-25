import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title = 'Choice for vote'
        self.left = 30
        self.top = 30
        self.width = 900
        self.height = 100
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.createHorizontalLayout()
 
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
 
        self.show()
 
    def createHorizontalLayout(self):
        theme="test"
        self.horizontalGroupBox = QGroupBox("%s"%theme)
        layout = QHBoxLayout()
        choices="a,b,c,d"
        choiceslist=choices.split(',')
 
        buttonChoice1 = QPushButton('%s'%choiceslist[0], self)
        buttonChoice1.clicked.connect(self.on_click_choice1)
        layout.addWidget(buttonChoice1) 
 
        buttonChoice2 = QPushButton('%s'%choiceslist[1], self)
        buttonChoice2.clicked.connect(self.on_click_choice2)
        layout.addWidget(buttonChoice2) 
 
        buttonChoice3 = QPushButton('%s'%choiceslist[2], self)
        buttonChoice3.clicked.connect(self.on_click_choice3)
        layout.addWidget(buttonChoice3) 

        buttonChoice4 = QPushButton('%s'%choiceslist[3], self)
        buttonChoice4.clicked.connect(self.on_click_choice4)
        layout.addWidget(buttonChoice4) 
 
        self.horizontalGroupBox.setLayout(layout)
 
 
    @pyqtSlot()
    def on_click_choice1(self):
        userchoice=1
    
    def on_click_choice2(self):
        userchoice=2

    def on_click_choice3(self):
        userchoice=3

    def on_click_choice4(self):
        userchoice=4

  
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())