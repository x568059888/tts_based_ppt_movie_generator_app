# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AudioConfirmWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AudioConfirmWindow(object):
    def setupUi(self, AudioConfirmWindow):
        AudioConfirmWindow.setObjectName("AudioConfirmWindow")
        AudioConfirmWindow.setEnabled(True)
        AudioConfirmWindow.resize(500, 140)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AudioConfirmWindow.sizePolicy().hasHeightForWidth())
        AudioConfirmWindow.setSizePolicy(sizePolicy)
        AudioConfirmWindow.setMinimumSize(QtCore.QSize(500, 140))
        AudioConfirmWindow.setMaximumSize(QtCore.QSize(500, 140))
        self.gridLayout_2 = QtWidgets.QGridLayout(AudioConfirmWindow)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.ChooseButton = QtWidgets.QDialogButtonBox(AudioConfirmWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.ChooseButton.setFont(font)
        self.ChooseButton.setOrientation(QtCore.Qt.Horizontal)
        self.ChooseButton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ChooseButton.setObjectName("ChooseButton")
        self.gridLayout.addWidget(self.ChooseButton, 2, 0, 1, 1)
        self.ChangeTimeLabel = QtWidgets.QLabel(AudioConfirmWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.ChangeTimeLabel.setFont(font)
        self.ChangeTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ChangeTimeLabel.setObjectName("ChangeTimeLabel")
        self.gridLayout.addWidget(self.ChangeTimeLabel, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(AudioConfirmWindow)
        self.ChooseButton.accepted.connect(AudioConfirmWindow.accept)
        self.ChooseButton.rejected.connect(AudioConfirmWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(AudioConfirmWindow)

    def retranslateUi(self, AudioConfirmWindow):
        _translate = QtCore.QCoreApplication.translate
        AudioConfirmWindow.setWindowTitle(_translate("AudioConfirmWindow", "AudioConfirm"))
        self.ChangeTimeLabel.setText(_translate("AudioConfirmWindow", "音频合成完毕！是否需要试听并对音频时长做进一步修改？"))