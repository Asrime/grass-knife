import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import os
import shutil
import random 

#打印当前调用模块的名字
print(__name__)

#Caodao类继承了窗体:
class Caodao(QMainWindow):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		#设置字体
		QToolTip.setFont(QFont('SansSerif', 10))
		
		#显示语
		self.setToolTip('这是草刀')

		#路径框
		pathLabel = QLabel('路径')
		self.pathEdit = QLineEdit()

		pathbtn = QPushButton('浏览', self)
		pathbtn.clicked.connect(self.setBrowerPath)
		pathbtn.resize(pathbtn.sizeHint())

		openbtn = QPushButton('打开', self)
		openbtn.clicked.connect(self.openDir)
		openbtn.resize(pathbtn.sizeHint())

		pathLayoutBox = QHBoxLayout()
		#pathLayoutBox.addStretch(1)
		pathLayoutBox.addWidget(pathLabel)
		pathLayoutBox.addWidget(self.pathEdit)
		# pathLayoutBox.addStretch(1)
		pathLayoutBox.addWidget(pathbtn)
		pathLayoutBox.addWidget(openbtn)


		#退出按钮
		qbtn = QPushButton('Quit', self)
		qbtn.clicked.connect(QCoreApplication.instance().quit)
		qbtn.setToolTip('这是退出按钮')
		qbtn.resize(qbtn.sizeHint())
		#qbtn.move(50,50)

		#提取整合图片按钮
		okbtn = QPushButton('提取整合图片', self)
		okbtn.clicked.connect(self.getAllPic)
		okbtn.setToolTip('将对应目录下3层的单独文件收集到一层')
		okbtn.resize(okbtn.sizeHint())

		#框布局按钮
		hbox = QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(okbtn)
		hbox.addStretch(1)
		hbox.addWidget(qbtn)
		hbox.addStretch(1)

		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(pathLayoutBox)
		vbox.addStretch(1)
		vbox.addLayout(hbox)
		vbox.addStretch(1)
		#vbox.addStretch(1)

		#状态栏
		self.statusBar()

		#QMain的框布局方式
		widget = QWidget()
		widget.setLayout(vbox)
		self.setCentralWidget(widget)

		#居中显示窗体
		#self.setGeometry(300,300,300,220)
		self.resize(500,400)
		self.center()
		self.setWindowTitle('草刀 v1.0')
		self.setWindowIcon(QIcon('icon.png'))
		self.show()

	#控制窗口居中显示
	def center(self):
		#获取窗口
		qr = self.frameGeometry()
		#获得中心点
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	#键盘事件
	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Escape:
			self.close()

	#ok按钮事件
	def okButtonClicked(self):
		sender = self.sender()
		#sender()方法来判断信号源
		self.statusBar().showMessage(sender.text() + '被按下了')

	#浏览文件窗口
	def setBrowerPath(self):
		download_path = QFileDialog.getExistingDirectory(self, "浏览", "D:")   
		self.pathEdit.setText(download_path)

	def openDir(self):
		path = self.pathEdit.text()
		if path == '':
			QMessageBox.question(self, "提示", "路径不能为空", QMessageBox.Yes | QMessageBox.No)
		else:
			os.startfile(path)

	def getAllPic(self):
		path = self.pathEdit.text()
		if path == '':
			QMessageBox.question(self, "提示", "路径不能为空", QMessageBox.Yes | QMessageBox.No)
		else:
			all_dir = os.listdir(path)
			# print(all_dir)
			counts = []
			num = 0
			randomRange = 100000
			#cut pics for each dir
			for dir_i in all_dir:
				father_path = path + '\\' + dir_i
				#print(finalpath)
				if os.path.isdir(father_path):
					#print(finalpath)
					all_files = os.listdir(father_path)
					#print(all_files)
					for file_i in all_files:
						son_path = father_path + '\\' + file_i
						if os.path.isdir(son_path):
							#print(finalpath)
							all_files2 = os.listdir(son_path)
							#print(all_files)
							for file_j in all_files2:
								son_path2 = son_path + '\\' + file_j
								if os.path.isdir(son_path2):
									print('存在3层目录，放弃提取：'+son_path2)
								else:
									count = random.randint(0,randomRange)
									while count in counts:
										count = random.randint(0,randomRange)
									counts.append(count)
									#print( str(count) + '.png')
									appedix = os.path.splitext(son_path2)[-1]
									shutil.copy(son_path2, path + '/' + str(count) + appedix )
									num = num + 1

						else:
							#os.path.splitext(son_path)[0]
							count = random.randint(0,randomRange)
							while count in counts:
								count = random.randint(0,randomRange)
							counts.append(count)
							#print( str(count) + '.png')
							appedix = os.path.splitext(son_path)[-1]
							shutil.copy(son_path, path + '/' + str(count) + appedix )
							num = num + 1
						#print(str(count))
			print('提取了' + str(num) + '个文件')

#如果是本体调用，运行主程序
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Caodao()
	sys.exit(app.exec_())
