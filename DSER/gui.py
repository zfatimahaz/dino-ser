import sys

from PyQt5 import QtWidgets, QtGui, QtCore


class MainWindow:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()

        self.mainPath = "asset/welcome.png"
        self.recPath = "asset/micrec.png"
        self.filePath = "asset/folder.png"
        self.neutralPath = "asset/neutral.png"
        self.sadPath = "asset/sad.png"
        self.angryPath = "asset/angry.png"
        self.happyPath = "asset/happy.png"

        self.initGui()
        self.initComponent()
        self.initOutputGui()

        self.window.setWindowTitle("DSER")
        self.window.setGeometry(500, 50, 400, 600)
        self.window.setStyleSheet("color: #75756e;"
                                  "background-color: #dbdbdb;")

        self.window.show()
        sys.exit(self.app.exec_())

    def initGui(self):
        self.mainImage = QtGui.QImage(self.mainPath)
        self.mainLabel = QtWidgets.QLabel(self.window)
        self.mainLabel.setGeometry(125, 20, 150, 150)
        self.mainLabel.setPixmap(QtGui.QPixmap.fromImage(self.mainImage))
        self.mainLabel.setScaledContents(True)

        self.titleLabel = QtWidgets.QLabel(self.window)
        self.titleLabel.setText("DINO'S SPEECH")
        self.titleLabel.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.titleLabel.adjustSize()
        self.titleLabel.move(125, 175)

        self.titleLabel = QtWidgets.QLabel(self.window)
        self.titleLabel.setText("EMOTION RECOGNITION")
        self.titleLabel.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.titleLabel.adjustSize()
        self.titleLabel.move(85, 200)

    def initOutputGui(self):
        self.neutralImage = QtGui.QImage(self.neutralPath)
        self.neutralLabel = QtWidgets.QLabel(self.window)
        self.neutralLabel.setGeometry(40, 360, 80, 80)
        self.neutralLabel.setPixmap(QtGui.QPixmap.fromImage(self.neutralImage))
        self.neutralLabel.setScaledContents(True)

        self.neutralLabel = QtWidgets.QLabel(self.window)
        self.neutralLabel.setText("Neutral")
        self.neutralLabel.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Black))
        self.neutralLabel.adjustSize()
        self.neutralLabel.move(110, 400)

        self.happyImage = QtGui.QImage(self.happyPath)
        self.happyLabel = QtWidgets.QLabel(self.window)
        self.happyLabel.setGeometry(230, 370, 75, 75)
        self.happyLabel.setPixmap(QtGui.QPixmap.fromImage(self.happyImage))
        self.happyLabel.setScaledContents(True)

        self.happyLabel = QtWidgets.QLabel(self.window)
        self.happyLabel.setText("Happy")
        self.happyLabel.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Black))
        self.happyLabel.adjustSize()
        self.happyLabel.move(310, 400)

        self.angryImage = QtGui.QImage(self.angryPath)
        self.angryLabel = QtWidgets.QLabel(self.window)
        self.angryLabel.setGeometry(45, 480, 75, 75)
        self.angryLabel.setPixmap(QtGui.QPixmap.fromImage(self.angryImage))
        self.angryLabel.setScaledContents(True)

        self.angryLabel = QtWidgets.QLabel(self.window)
        self.angryLabel.setText("Angry")
        self.angryLabel.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Black))
        self.angryLabel.adjustSize()
        self.angryLabel.move(125, 515)

        self.sadImage = QtGui.QImage(self.sadPath)
        self.sadLabel = QtWidgets.QLabel(self.window)
        self.sadLabel.setGeometry(230, 480, 75, 75)
        self.sadLabel.setPixmap(QtGui.QPixmap.fromImage(self.sadImage))
        self.sadLabel.setScaledContents(True)

        self.sadLabel = QtWidgets.QLabel(self.window)
        self.sadLabel.setText("Sad")
        self.sadLabel.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Black))
        self.sadLabel.adjustSize()
        self.sadLabel.move(315, 518)

    def initComponent(self):
        self.recImage = QtGui.QIcon(self.recPath)
        self.recButton = QtWidgets.QPushButton(self.window)
        self.recButton.setGeometry(70, 240, 100, 100)
        self.recButton.setIcon(self.recImage)
        self.recButton.setIconSize(QtCore.QSize(80,80))
        self.recButton.setStyleSheet("QPushButton { border-radius: 50px }"
                                     "QPushButton:pressed { background-color: #75756e }")
        # self.recButton.clicked.connect() # self.on_click_rec

        self.fileImage = QtGui.QIcon(self.filePath)
        self.fileButton = QtWidgets.QPushButton(self.window)
        self.fileButton.setGeometry(230, 240, 100, 100)
        self.fileButton.setIcon(self.fileImage)
        self.fileButton.setIconSize(QtCore.QSize(70, 70))
        self.fileButton.setStyleSheet("QPushButton { border-radius: 50px }"
                                     "QPushButton:pressed { background-color: #75756e }")
        # self.fileButton.clicked.connect() # self.on_click_file

    # @QtCore.pyqtSlot()
    # def on_click_rec(self):
    #     # do rec-1st click
    #     # stop rec-2nd click and then do prediction then  display result
    #
    # @QtCore.pyqtSlot()
    # def on_click_file(self):
    #     # do accept file
    #     # on submit do prediction then display result


main = MainWindow()