# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'card5.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(583, 157)
        self.IRPT_comboBox = QtWidgets.QComboBox(Form)
        self.IRPT_comboBox.setEnabled(True)
        self.IRPT_comboBox.setGeometry(QtCore.QRect(280, 20, 201, 27))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.IRPT_comboBox.setFont(font)
        self.IRPT_comboBox.setEditable(False)
        self.IRPT_comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.IRPT_comboBox.setObjectName("IRPT_comboBox")
        self.IRPT_comboBox.addItem("")
        self.IRPT_comboBox.addItem("")
        self.IRPT_comboBox.addItem("")
        self.IRPT_comboBox.addItem("")
        self.label_33 = QtWidgets.QLabel(Form)
        self.label_33.setGeometry(QtCore.QRect(70, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.BEFORE_pushButton = QtWidgets.QPushButton(Form)
        self.BEFORE_pushButton.setEnabled(True)
        self.BEFORE_pushButton.setGeometry(QtCore.QRect(110, 60, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.BEFORE_pushButton.setFont(font)
        self.BEFORE_pushButton.setObjectName("BEFORE_pushButton")
        self.NEXT_pushButton = QtWidgets.QPushButton(Form)
        self.NEXT_pushButton.setEnabled(False)
        self.NEXT_pushButton.setGeometry(QtCore.QRect(230, 60, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.NEXT_pushButton.setFont(font)
        self.NEXT_pushButton.setObjectName("NEXT_pushButton")
        self.INSURE_pushButton = QtWidgets.QPushButton(Form)
        self.INSURE_pushButton.setEnabled(False)
        self.INSURE_pushButton.setGeometry(QtCore.QRect(350, 60, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.INSURE_pushButton.setFont(font)
        self.INSURE_pushButton.setObjectName("INSURE_pushButton")
        self.TAPE5_pushButton = QtWidgets.QPushButton(Form)
        self.TAPE5_pushButton.setGeometry(QtCore.QRect(160, 100, 101, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.TAPE5_pushButton.setFont(font)
        self.TAPE5_pushButton.setObjectName("TAPE5_pushButton")
        self.FUYUAN_pushButton = QtWidgets.QPushButton(Form)
        self.FUYUAN_pushButton.setGeometry(QtCore.QRect(290, 100, 101, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.FUYUAN_pushButton.setFont(font)
        self.FUYUAN_pushButton.setObjectName("FUYUAN_pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CARD5"))
        self.IRPT_comboBox.setItemText(0, _translate("Form", "执行一次后停止"))
        self.IRPT_comboBox.setItemText(1, _translate("Form", "读取全新数据卡"))
        self.IRPT_comboBox.setItemText(2, _translate("Form", "读取新的CARD 3- CARD5"))
        self.IRPT_comboBox.setItemText(3, _translate("Form", "读取新的CARD 4- CARD5"))
        self.label_33.setText(_translate("Form", "重复运行选项(IRPT)"))
        self.BEFORE_pushButton.setText(_translate("Form", "上一页"))
        self.NEXT_pushButton.setText(_translate("Form", "下一页"))
        self.INSURE_pushButton.setText(_translate("Form", "确定"))
        self.TAPE5_pushButton.setText(_translate("Form", "Tape5合成"))
        self.FUYUAN_pushButton.setText(_translate("Form", "按键复原"))