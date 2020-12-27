# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):
    _file_dir = ''  # pptx文件路径
    _save_dir = ''  # 视频保存路径
    update = True  # 检查pptx是否需要转换为图片
    _translate = QtCore.QCoreApplication.translate
    dict_male = {"磁性男声": "107289", "时尚男声": "100453",
                 "浑厚男声": "106528", "成熟男声": "107813"}
    dict_female = {"亲切女声": "101238", "时尚女声": "100438", "甜美女声": "108259-shaoyv",
                   "温柔女声": "100216", "活泼女声": "biaobei", "可爱女童": "108259-luoli"}
    dict = {
        'male': {"磁性男声", "时尚男声", "浑厚男声", "成熟男声"},
        'female': {"亲切女声", "时尚女声", "甜美女声", "温柔女声", "活泼女声", "可爱女童"}
    }

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(607, 205)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(607, 205))
        MainWindow.setMaximumSize(QtCore.QSize(607, 205))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.StatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.StatusLabel.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.StatusLabel.setFont(font)
        self.StatusLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.StatusLabel.setObjectName("StatusLabel")
        self.gridLayout.addWidget(self.StatusLabel, 3, 0, 1, 4)
        self.ChooseFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChooseFileButton.setMinimumSize(QtCore.QSize(108, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.ChooseFileButton.setFont(font)
        self.ChooseFileButton.setObjectName("ChooseFileButton")
        self.gridLayout.addWidget(self.ChooseFileButton, 0, 5, 1, 1)
        self.PreviewButton = QtWidgets.QPushButton(self.centralwidget)
        self.PreviewButton.setMinimumSize(QtCore.QSize(108, 0))
        self.PreviewButton.setMaximumSize(QtCore.QSize(108, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.PreviewButton.setFont(font)
        self.PreviewButton.setObjectName("PreviewButton")
        self.gridLayout.addWidget(self.PreviewButton, 1, 5, 1, 1)
        self.VoiceCheck = QtWidgets.QLabel(self.centralwidget)
        self.VoiceCheck.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.VoiceCheck.setFont(font)
        self.VoiceCheck.setObjectName("VoiceCheck")
        self.gridLayout.addWidget(self.VoiceCheck, 1, 0, 1, 1)
        self.ChooseGender = QtWidgets.QComboBox(self.centralwidget)
        self.ChooseGender.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.ChooseGender.setFont(font)
        self.ChooseGender.setObjectName("ChooseGender")
        self.ChooseGender.addItem("")
        self.ChooseGender.addItem("")
        self.gridLayout.addWidget(self.ChooseGender, 1, 2, 1, 1)
        self.GenderLabel = QtWidgets.QLabel(self.centralwidget)
        self.GenderLabel.setEnabled(True)
        self.GenderLabel.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.GenderLabel.setFont(font)
        self.GenderLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GenderLabel.setObjectName("GenderLabel")
        self.gridLayout.addWidget(self.GenderLabel, 1, 1, 1, 1)
        self.SynthLabel = QtWidgets.QLabel(self.centralwidget)
        self.SynthLabel.setMinimumSize(QtCore.QSize(55, 0))
        self.SynthLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.SynthLabel.setFont(font)
        self.SynthLabel.setObjectName("SynthLabel")
        self.gridLayout.addWidget(self.SynthLabel, 1, 3, 1, 1)
        self.ConvertButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.ConvertButton.setFont(font)
        self.ConvertButton.setObjectName("ConvertButton")
        self.gridLayout.addWidget(self.ConvertButton, 3, 5, 1, 1)
        self.ChooseSavedDirButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChooseSavedDirButton.sizePolicy().hasHeightForWidth())
        self.ChooseSavedDirButton.setSizePolicy(sizePolicy)
        self.ChooseSavedDirButton.setMinimumSize(QtCore.QSize(108, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.ChooseSavedDirButton.setFont(font)
        self.ChooseSavedDirButton.setMouseTracking(False)
        self.ChooseSavedDirButton.setObjectName("ChooseSavedDirButton")
        self.gridLayout.addWidget(self.ChooseSavedDirButton, 2, 5, 1, 1)
        self.ChooseSpeakerId = QtWidgets.QComboBox(self.centralwidget)
        self.ChooseSpeakerId.setMinimumSize(QtCore.QSize(110, 0))
        self.ChooseSpeakerId.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.ChooseSpeakerId.setFont(font)
        self.ChooseSpeakerId.setObjectName("ChooseSpeakerId")
        self.ChooseSpeakerId.addItem("")
        self.ChooseSpeakerId.addItem("")
        self.ChooseSpeakerId.addItem("")
        self.ChooseSpeakerId.addItem("")
        self.gridLayout.addWidget(self.ChooseSpeakerId, 1, 4, 1, 1)
        self.SaveDirBlank = QtWidgets.QLineEdit(self.centralwidget)
        self.SaveDirBlank.setReadOnly(True)
        self.SaveDirBlank.setObjectName("SaveDirBlank")
        self.gridLayout.addWidget(self.SaveDirBlank, 2, 1, 1, 4)
        self.SavedDirLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.SavedDirLabel.setFont(font)
        self.SavedDirLabel.setObjectName("SavedDirLabel")
        self.gridLayout.addWidget(self.SavedDirLabel, 2, 0, 1, 1)
        self.FileDirBlank = QtWidgets.QLineEdit(self.centralwidget)
        self.FileDirBlank.setReadOnly(True)
        self.FileDirBlank.setObjectName("FileDirBlank")
        self.gridLayout.addWidget(self.FileDirBlank, 0, 1, 1, 4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.PinyinCheck = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.PinyinCheck.setFont(font)
        self.PinyinCheck.setCheckable(True)
        self.PinyinCheck.setChecked(False)
        self.PinyinCheck.setObjectName("PinyinCheck")
        self.verticalLayout.addWidget(self.PinyinCheck)
        self.NoNotesCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.NoNotesCheck.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.NoNotesCheck.setFont(font)
        self.NoNotesCheck.setCheckable(True)
        self.NoNotesCheck.setChecked(False)
        self.NoNotesCheck.setTristate(False)
        self.NoNotesCheck.setObjectName("NoNotesCheck")
        self.verticalLayout.addWidget(self.NoNotesCheck)
        self.gridLayout.addLayout(self.verticalLayout, 3, 4, 1, 1)
        self.FileDirLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.FileDirLabel.setFont(font)
        self.FileDirLabel.setTextFormat(QtCore.Qt.AutoText)
        self.FileDirLabel.setObjectName("FileDirLabel")
        self.gridLayout.addWidget(self.FileDirLabel, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOption = QtWidgets.QAction(MainWindow)
        self.actionOption.setObjectName("actionOption")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPreference = QtWidgets.QAction(MainWindow)
        self.actionPreference.setObjectName("actionPreference")

        self.retranslateUi(MainWindow)
        self.PinyinCheck.clicked['bool'].connect(self.NoNotesCheck.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ChooseFileButton, self.ChooseGender)
        MainWindow.setTabOrder(self.ChooseGender, self.ChooseSpeakerId)
        MainWindow.setTabOrder(self.ChooseSpeakerId, self.PreviewButton)

        self.ChooseFileButton.clicked.connect(self.openFile)
        self.ChooseSavedDirButton.clicked.connect(self.saveFile)
        self.PinyinCheck.clicked.connect(self.visible)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StatusLabel.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:11pt; color:#21ff06;\">一切就绪！</span></p></body></html>"))
        self.ChooseFileButton.setText(_translate("MainWindow", "选择文件"))
        self.PreviewButton.setText(_translate("MainWindow", "试听"))
        self.VoiceCheck.setText(_translate("MainWindow", "语音设定："))
        self.ChooseGender.setItemText(0, _translate("MainWindow", "男声"))
        self.ChooseGender.setItemText(1, _translate("MainWindow", "女声"))
        self.GenderLabel.setText(_translate("MainWindow", "性别"))
        self.SynthLabel.setText(_translate("MainWindow", "语调设定"))
        self.ConvertButton.setText(_translate("MainWindow", "开始转换"))
        self.ChooseSavedDirButton.setText(_translate("MainWindow", "选择文件夹"))
        self.ChooseSpeakerId.setItemText(0, _translate("MainWindow", "时尚男声"))
        self.ChooseSpeakerId.setItemText(1, _translate("MainWindow", "磁性男声"))
        self.ChooseSpeakerId.setItemText(2, _translate("MainWindow", "浑厚男声"))
        self.ChooseSpeakerId.setItemText(3, _translate("MainWindow", "成熟男声"))
        self.SavedDirLabel.setText(_translate("MainWindow", "保存路径："))
        self.PinyinCheck.setText(_translate("MainWindow", "启用拼音检查"))
        self.NoNotesCheck.setText(_translate("MainWindow", "只查看无备注页"))
        self.FileDirLabel.setText(_translate("MainWindow", "文件路径："))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOption.setText(_translate("MainWindow", "Option"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionPreference.setText(_translate("MainWindow", "Preference"))

    def getFileDir(self):
        return self._file_dir

    def getSaveDir(self):
        return self._save_dir

    def openFile(self):
        openfile_name = QFileDialog.getOpenFileName(None, '选择文件', '', 'Pptx files(*.pptx)')
        self.FileDirBlank.setText(openfile_name[0])

    def saveFile(self):
        self._save_dir = QtWidgets.QFileDialog.getExistingDirectory(None, "getExistingDirectory", "./")
        self.SaveDirBlank.setText(self._save_dir)

    def visible(self):
        if self.PinyinCheck.isChecked():
            self.NoNotesCheck.setChecked(False)
            self.NoNotesCheck.setEnabled(False)
        else:
            self.NoNotesCheck.setEnabled(True)

    # 音频转换函数
    def convert(self):
        if self._file_dir != '' and self._file_dir == self.FileDirBlank.text():
            self.update = False
        self._file_dir = self.FileDirBlank.text()
        self._save_dir = self.SaveDirBlank.text()
        if self._file_dir == '':
            self.StatusLabel.setText(self._translate("MainWindow",
                                                     "<html><head/><body><p><span style=\" "
                                                     "font-size:14pt; color:#ff0000;\""
                                                     ">文件目录为空!请检查后重试!"
                                                     "</span></p></body></html>"))
            return False
        elif self._save_dir == '':
            self.StatusLabel.setText(self._translate("MainWindow",
                                                     "<html><head/><body><p><span style=\" "
                                                     "font-size:14pt; color:#ff0000;\""
                                                     ">保存路径为空!请检查后重试!"
                                                     "</span></p></body></html>"))
            return False
        return True

    def set_PreviewButton(self):
        self.PreviewButton.setEnabled(True)
