# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'card2b.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(838, 190)
        self.ZCVSA_lineEdit = QtWidgets.QLineEdit(Form)
        self.ZCVSA_lineEdit.setEnabled(False)
        self.ZCVSA_lineEdit.setGeometry(QtCore.QRect(200, 20, 171, 21))
        self.ZCVSA_lineEdit.setText("")
        self.ZCVSA_lineEdit.setObjectName("ZCVSA_lineEdit")
        self.label_34 = QtWidgets.QLabel(Form)
        self.label_34.setGeometry(QtCore.QRect(20, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(Form)
        self.label_35.setGeometry(QtCore.QRect(430, 20, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.ZTVSA_lineEdit = QtWidgets.QLineEdit(Form)
        self.ZTVSA_lineEdit.setEnabled(False)
        self.ZTVSA_lineEdit.setGeometry(QtCore.QRect(630, 20, 171, 21))
        self.ZTVSA_lineEdit.setText("")
        self.ZTVSA_lineEdit.setObjectName("ZTVSA_lineEdit")
        self.label_36 = QtWidgets.QLabel(Form)
        self.label_36.setGeometry(QtCore.QRect(20, 70, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.ZINVSA_lineEdit = QtWidgets.QLineEdit(Form)
        self.ZINVSA_lineEdit.setEnabled(False)
        self.ZINVSA_lineEdit.setGeometry(QtCore.QRect(330, 70, 171, 21))
        self.ZINVSA_lineEdit.setText("")
        self.ZINVSA_lineEdit.setObjectName("ZINVSA_lineEdit")
        self.INSURE_pushButton = QtWidgets.QPushButton(Form)
        self.INSURE_pushButton.setGeometry(QtCore.QRect(270, 140, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.INSURE_pushButton.setFont(font)
        self.INSURE_pushButton.setObjectName("INSURE_pushButton")
        self.NEXT_pushButton = QtWidgets.QPushButton(Form)
        self.NEXT_pushButton.setGeometry(QtCore.QRect(150, 140, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.NEXT_pushButton.setFont(font)
        self.NEXT_pushButton.setObjectName("NEXT_pushButton")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(-20, 110, 1101, 16))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setLineWidth(5)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.BEFORE_pushButton = QtWidgets.QPushButton(Form)
        self.BEFORE_pushButton.setGeometry(QtCore.QRect(30, 140, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.BEFORE_pushButton.setFont(font)
        self.BEFORE_pushButton.setObjectName("BEFORE_pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CARD 2B"))
        self.label_34.setText(_translate("Form", "云顶高度(ZCVSA)"))
        self.label_35.setText(_translate("Form", "云或雾厚度(ZTVSA)"))
        self.label_36.setText(_translate("Form", "逆温层或边界层的高度(ZINVSA)"))
        self.INSURE_pushButton.setText(_translate("Form", "确定"))
        self.NEXT_pushButton.setText(_translate("Form", "下一页"))
        self.BEFORE_pushButton.setText(_translate("Form", "上一页"))