# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PreferencesWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PreferencesWindow(object):
    count = 6
    alg = "Distance Euclidean"
    
    def setupUi(self, PreferencesWindow):
    
        PreferencesWindow.setObjectName("PreferencesWindow")
        PreferencesWindow.resize(470, 500)
        PreferencesWindow.setMinimumSize(QtCore.QSize(470, 500))
        PreferencesWindow.setMaximumSize(QtCore.QSize(470, 500))

        self.centralwidget = QtWidgets.QWidget(PreferencesWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.count_result = QtWidgets.QSpinBox(self.centralwidget)
        self.count_result.setGeometry(QtCore.QRect(290, 120, 140, 26))
        self.count_result.setObjectName("count_result")

        self.count_result_label = QtWidgets.QLabel(self.centralwidget)
        self.count_result_label.setGeometry(QtCore.QRect(30, 120, 140, 26))
        self.count_result_label.setObjectName("count_result_label")

        self.algorithm_label = QtWidgets.QLabel(self.centralwidget)
        self.algorithm_label.setGeometry(QtCore.QRect(30, 60, 80, 26))
        self.algorithm_label.setObjectName("algorithm_label")

        self.algorithm = QtWidgets.QComboBox(self.centralwidget)
        self.algorithm.setGeometry(QtCore.QRect(190, 60, 240, 26))
        self.algorithm.setEditable(False)
        self.algorithm.setMaxVisibleItems(10)
        self.algorithm.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.algorithm.setDuplicatesEnabled(False)
        self.algorithm.setObjectName("algorithm")
        self.algorithm.addItem("")
        self.algorithm.addItem("")

        self.apply_btn = QtWidgets.QPushButton(self.centralwidget)
        self.apply_btn.setGeometry(QtCore.QRect(340, 430, 89, 25))
        self.apply_btn.setObjectName("apply_btn")
        self.apply_btn.pressed.connect(self.apply)

        PreferencesWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(PreferencesWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 470, 22))
        self.menubar.setObjectName("menubar")

        PreferencesWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(PreferencesWindow)
        self.statusbar.setObjectName("statusbar")

        PreferencesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PreferencesWindow)
        self.algorithm.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PreferencesWindow)

    def apply(self):
        self.count_result.setValue(self.count_result.value())
        self.count = self.count_result.value()
        self.alg = str(self.algorithm.currentText())
        self.algorithm.setCurrentIndex(self.algorithm.currentIndex())
        PreferencesWindow.close

    def retranslateUi(self, PreferencesWindow):
        _translate = QtCore.QCoreApplication.translate
        PreferencesWindow.setWindowTitle(_translate("PreferencesWindow", "Preferences"))
        self.count_result_label.setText(_translate("PreferencesWindow", "Image Result"))
        self.algorithm_label.setText(_translate("PreferencesWindow", "Algorithm"))
        self.algorithm.setCurrentText(_translate("PreferencesWindow", "Distance Euclidean"))
        self.algorithm.setItemText(0, _translate("PreferencesWindow", "Distance Euclidean"))
        self.algorithm.setItemText(1, _translate("PreferencesWindow", "Cosine Similarity"))
        self.apply_btn.setText(_translate("PreferencesWindow", "Apply"))


