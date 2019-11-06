# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

name = "Blank.jpg"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(863, 716)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.query_frame = QtWidgets.QFrame(self.centralwidget)
        self.query_frame.setGeometry(QtCore.QRect(40, 40, 361, 361))
        self.query_frame.setAcceptDrops(True)
        self.query_frame.setAutoFillBackground(False)
        self.query_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.query_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.query_frame.setObjectName("query_frame")

        self.label_2 = QtWidgets.QLabel(self.query_frame)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 361, 361))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(name))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 620, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 620, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 620, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")

        self.thumbnail_result_frame = QtWidgets.QFrame(self.centralwidget)
        self.thumbnail_result_frame.setGeometry(QtCore.QRect(40, 460, 141, 141))
        self.thumbnail_result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_result_frame.setObjectName("thumbnail_result_frame")

        self.thumbnail_result_frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.thumbnail_result_frame_2.setGeometry(QtCore.QRect(200, 460, 141, 141))
        self.thumbnail_result_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_result_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_result_frame_2.setObjectName("thumbnail_result_frame_2")

        self.thumbnail_result_frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.thumbnail_result_frame_3.setGeometry(QtCore.QRect(360, 460, 141, 141))
        self.thumbnail_result_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_result_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_result_frame_3.setObjectName("thumbnail_result_frame_3")

        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(520, 460, 141, 141))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")

        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(680, 460, 141, 141))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")

        self.main_result_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_result_frame.setGeometry(QtCore.QRect(460, 40, 361, 361))
        self.main_result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_result_frame.setObjectName("main_result_frame")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 420, 101, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen_Image = QtWidgets.QAction(MainWindow)
        self.actionOpen_Image.setObjectName("actionOpen_Image")
        self.actionOpen_Image.triggered.connect(self.file_open)


        self.actionOpen_Train_Folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_Train_Folder.setObjectName("actionOpen_Train_Folder")

        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")

        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.actionFace_Recognition_Help = QtWidgets.QAction(MainWindow)
        self.actionFace_Recognition_Help.setObjectName("actionFace_Recognition_Help")

        self.menuFile.addAction(self.actionOpen_Image)
        self.menuFile.addAction(self.actionOpen_Train_Folder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)

        self.menuHelp.addAction(self.actionFace_Recognition_Help)
        self.menuHelp.addAction(self.actionAbout)

        self.menuSetting.addAction(self.actionPreferences)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_2.setText(_translate("MainWindow", "Detail"))
        self.pushButton_3.setText(_translate("MainWindow", "Previous"))
        self.label.setText(_translate("MainWindow", "Match: N%"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSetting.setTitle(_translate("MainWindow", "Settings"))
        self.actionOpen_Image.setText(_translate("MainWindow", "Open Image..."))
        self.actionOpen_Image.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpen_Train_Folder.setText(_translate("MainWindow", "Open Train Folder..."))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences.."))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionFace_Recognition_Help.setText(_translate("MainWindow", "Face Recognition Help"))

    def file_open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        name, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if (name):
            print(name)
        self.label_2.setPixmap(QtGui.QPixmap(name))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
