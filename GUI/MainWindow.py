# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        input_image = "Blank.jpg"

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.query_frame = QtWidgets.QFrame(self.centralwidget)
        self.query_frame.setGeometry(QtCore.QRect(40, 40, 360, 360))
        self.query_frame.setAcceptDrops(True)
        self.query_frame.setAutoFillBackground(False)
        self.query_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.query_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.query_frame.setObjectName("query_frame")

        self.query_image = QtWidgets.QLabel(self.query_frame)
        self.query_image.setGeometry(QtCore.QRect(0, 0, 360, 360))
        self.query_image.setText("")
        self.query_image.setPixmap(QtGui.QPixmap(input_image))
        self.query_image.setScaledContents(True)
        self.query_image.setObjectName("query_image")

        self.next_btn = QtWidgets.QPushButton(self.centralwidget)
        self.next_btn.setGeometry(QtCore.QRect(710, 620, 90, 25))
        self.next_btn.setObjectName("next_btn")

        self.detail_btn = QtWidgets.QPushButton(self.centralwidget)
        self.detail_btn.setGeometry(QtCore.QRect(390, 620, 90, 25))
        self.detail_btn.setObjectName("detail_btn")

        self.prev_btn = QtWidgets.QPushButton(self.centralwidget)
        self.prev_btn.setGeometry(QtCore.QRect(60, 620, 90, 25))
        self.prev_btn.setObjectName("prev_btn")

        self.thumbnail_result_frame = QtWidgets.QFrame(self.centralwidget)
        self.thumbnail_result_frame.setGeometry(QtCore.QRect(40, 460, 140, 140))
        self.thumbnail_result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_result_frame.setObjectName("thumbnail_result_frame")

        self.thumb_image = QtWidgets.QLabel(self.thumbnail_result_frame)
        self.thumb_image.setGeometry(QtCore.QRect(0, 0, 140, 140))
        self.thumb_image.setText("")
        self.thumb_image.setScaledContents(True)
        self.thumb_image.setObjectName("thumb_image")

        self.thumbnail_result_frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.thumbnail_result_frame_2.setGeometry(QtCore.QRect(200, 460, 140, 140))
        self.thumbnail_result_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_result_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_result_frame_2.setObjectName("thumbnail_result_frame_2")

        self.thumb_image_2 = QtWidgets.QLabel(self.thumbnail_result_frame_2)
        self.thumb_image_2.setGeometry(QtCore.QRect(0, 0, 140, 140))
        self.thumb_image_2.setText("")
        self.thumb_image_2.setScaledContents(True)
        self.thumb_image_2.setObjectName("thumb_image_2")
        
        self.thumbnail_result_frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.thumbnail_result_frame_3.setGeometry(QtCore.QRect(360, 460, 140, 140))
        self.thumbnail_result_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_result_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_result_frame_3.setObjectName("thumbnail_result_frame_3")

        self.thumb_image_3 = QtWidgets.QLabel(self.thumbnail_result_frame_3)
        self.thumb_image_3.setGeometry(QtCore.QRect(0, 0, 140, 140))
        self.thumb_image_3.setText("")
        self.thumb_image_3.setScaledContents(True)
        self.thumb_image_3.setObjectName("thumb_image_3")

        self.thumbnail_result_frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.thumbnail_result_frame_4.setGeometry(QtCore.QRect(520, 460, 140, 140))
        self.thumbnail_result_frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_result_frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_result_frame_4.setObjectName("thumbnail_result_frame_4")

        self.thumb_image_4 = QtWidgets.QLabel(self.thumbnail_result_frame_4)
        self.thumb_image_4.setGeometry(QtCore.QRect(0, 0, 140, 140))
        self.thumb_image_4.setText("")
        self.thumb_image_4.setScaledContents(True)
        self.thumb_image_4.setObjectName("thumb_image_4")

        self.thumbnail_result_frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.thumbnail_result_frame_5.setGeometry(QtCore.QRect(680, 460, 140, 140))
        self.thumbnail_result_frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_result_frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_result_frame_5.setObjectName("thumbnail_result_frame_5")

        self.thumb_image_5 = QtWidgets.QLabel(self.thumbnail_result_frame_5)
        self.thumb_image_5.setGeometry(QtCore.QRect(0, 0, 140, 140))
        self.thumb_image_5.setText("")
        self.thumb_image_5.setScaledContents(True)
        self.thumb_image_5.setObjectName("thumb_image_5")

        self.main_result_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_result_frame.setGeometry(QtCore.QRect(460, 40, 360, 360))
        self.main_result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_result_frame.setObjectName("main_result_frame")

        self.main_result_image = QtWidgets.QLabel(self.main_result_frame)
        self.main_result_image.setGeometry(QtCore.QRect(0, 0, 360, 360))
        self.main_result_image.setText("")
        self.main_result_image.setScaledContents(True)
        self.main_result_image.setObjectName("main_result_image")

        self.match_rating = QtWidgets.QLabel(self.centralwidget)
        self.match_rating.setGeometry(QtCore.QRect(350, 420, 160, 20))
        self.match_rating.setScaledContents(True)
        self.match_rating.setAlignment(QtCore.Qt.AlignCenter)
        self.match_rating.setObjectName("match_rating")

        self.query_name = QtWidgets.QLabel(self.centralwidget)
        self.query_name.setGeometry(QtCore.QRect(40, 20, 360, 17))
        self.query_name.setAlignment(QtCore.Qt.AlignCenter)
        self.query_name.setObjectName("query_name")

        self.main_result_name = QtWidgets.QLabel(self.centralwidget)
        self.main_result_name.setGeometry(QtCore.QRect(460, 20, 360, 17))
        self.main_result_name.setAlignment(QtCore.Qt.AlignCenter)
        self.main_result_name.setObjectName("main_result_name")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 22))
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
        self.actionOpen_Train_Folder.triggered.connect(self.train_folder_open)
        
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.actionPreferences.setObjectName("actionPreferences")

        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(MainWindow.close)

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setMenuRole(QtWidgets.QAction.AboutRole)
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

    def file_open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        input_image, _ = QFileDialog.getOpenFileName(None, "Select Image", "","All Files (*);;JPG Files (*.jpg)", options=options)
        if input_image:
            self.query_image.setPixmap(QtGui.QPixmap(input_image))
    
    def train_folder_open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog
        train_folder = QFileDialog.getExistingDirectory(None, "Select Directory", "", options=options)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next_btn.setText(_translate("MainWindow", "Next"))
        self.detail_btn.setText(_translate("MainWindow", "Detail"))
        self.prev_btn.setText(_translate("MainWindow", "Previous"))
        self.match_rating.setText(_translate("MainWindow", "Match: N%"))
        self.query_name.setText(_translate("MainWindow", "Aaron_Paul"))
        self.main_result_name.setText(_translate("MainWindow", "Aaron_Paul"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
