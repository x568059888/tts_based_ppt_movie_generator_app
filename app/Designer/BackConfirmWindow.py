# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BackConfirmWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BackConfirmWindow(object):
    def setupUi(self, BackConfirmWindow):
        BackConfirmWindow.setObjectName("BackConfirmWindow")
        BackConfirmWindow.resize(500, 120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BackConfirmWindow.sizePolicy().hasHeightForWidth())
        BackConfirmWindow.setSizePolicy(sizePolicy)
        BackConfirmWindow.setMinimumSize(QtCore.QSize(500, 120))
        BackConfirmWindow.setMaximumSize(QtCore.QSize(500, 120))
        self.gridLayout = QtWidgets.QGridLayout(BackConfirmWindow)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(BackConfirmWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(BackConfirmWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(BackConfirmWindow)
        self.buttonBox.accepted.connect(BackConfirmWindow.accept)
        self.buttonBox.rejected.connect(BackConfirmWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(BackConfirmWindow)

    def retranslateUi(self, BackConfirmWindow):
        _translate = QtCore.QCoreApplication.translate
        BackConfirmWindow.setWindowTitle(_translate("BackConfirmWindow", "Confirm"))
        self.label.setText(_translate("BackConfirmWindow", "   是否对当前页面所作编辑进行保存？"))
