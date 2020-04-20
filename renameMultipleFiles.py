import sys
import os
from functools import partial
from PySide2 import QtCore, QtGui, QtWidgets

font = QtGui.QFont()
font.setFamily("Tekton Pro Ext")
font.setPointSize(12)
font.setWeight(10)

class MainWidget(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(MainWidget, self).__init__()
		self.initUI()

	def initUI(self):
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		self.setWindowTitle("Rename Multi Files")
		self.setSizePolicy(sizePolicy)
		self.layout = QtWidgets.QGridLayout()

		self.centralwidget = QtWidgets.QWidget(self)
		self.centralwidget.setObjectName("centralwidget")
		self.centralwidget.setSizePolicy(sizePolicy)
		self.setCentralWidget(self.centralwidget)
		self.centralwidget.setLayout(self.layout)

		self.lineEdit_input = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_input.setPlaceholderText("Folder input's Location...")
		self.lineEdit_input.setClearButtonEnabled(True)
		self.lineEdit_input.editingFinished.connect(partial(self.getListFiles))

		self.items = QtWidgets.QListWidgetItem()
		self.items.setFlags(QtCore.Qt.ItemIsEditable)

		self.listFiles_input = QtWidgets.QListWidget(self.centralwidget)
		

		self.button_Rename = QtWidgets.QPushButton(self.centralwidget)
		self.button_Rename.setText("Rename")
		self.button_Rename.clicked.connect(partial(self.rename))

		self.layout.addWidget(self.lineEdit_input, 1, 1, 0)
		self.layout.addWidget(self.listFiles_input, 2, 1, 0)
		self.layout.addWidget(self.button_Rename, 3, 1, 0)

	def getListFiles(self):
		try:
			dirr = self.lineEdit_input.text()
			listofFiles = os.listdir(dirr)
			self.listFiles_input.addItems(listofFiles)
			for index in range(self.listFiles_input.count()):
				item = self.listFiles_input.item(index)
				item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
		except:
			msg = QtWidgets.QMessageBox()
			msg.setIcon(msg.Critical)
			msg.setText("Folder's Location doesn't exist")
			msg.setWindowTitle("Error!")
			msg.exec_()

	def rename(self):
		dirr = self.lineEdit_input.text()
		listofFiles = os.listdir(dirr)
		for i in range(len(listofFiles)):
			os.rename(os.path.join(dirr,listofFiles[i]), os.path.join(dirr, self.listFiles_input.item(i).text()))

		msg = QtWidgets.QMessageBox()
		msg.setIcon(msg.Information)
		msg.setText("Rename Successfully!")
		msg.setWindowTitle("Notification!")
		msg.exec_()


if(__name__ == '__main__'):
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle("Fusion")
	palette = QtGui.QPalette()
	palette.setColor(QtGui.QPalette.Window, QtGui.QColor(50,50,50))
	palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(60,224,238))
	palette.setColor(QtGui.QPalette.Base, QtGui.QColor(0,0,0))
	palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
	palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
	palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
	palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53,53,53))
	palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(60,224,238))

	app.setPalette(palette)
	window = MainWidget()
	window.show()
	sys.exit(app.exec_())