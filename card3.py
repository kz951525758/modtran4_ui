# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'card3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(855, 383)
        self.H1_lineEdit = QtWidgets.QLineEdit(Form)
        self.H1_lineEdit.setEnabled(False)
        self.H1_lineEdit.setGeometry(QtCore.QRect(190, 240, 171, 21))
        self.H1_lineEdit.setObjectName("H1_lineEdit")
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(40, 240, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.LENN_comboBox = QtWidgets.QComboBox(Form)
        self.LENN_comboBox.setEnabled(False)
        self.LENN_comboBox.setGeometry(QtCore.QRect(630, 330, 141, 27))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.LENN_comboBox.setFont(font)
        self.LENN_comboBox.setEditable(False)
        self.LENN_comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.LENN_comboBox.setObjectName("LENN_comboBox")
        self.LENN_comboBox.addItem("")
        self.LENN_comboBox.addItem("")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(40, 50, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.H2_lineEdit = QtWidgets.QLineEdit(Form)
        self.H2_lineEdit.setGeometry(QtCore.QRect(190, 60, 171, 21))
        self.H2_lineEdit.setText("")
        self.H2_lineEdit.setObjectName("H2_lineEdit")
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(430, 240, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.ANGLE_lineEdit = QtWidgets.QLineEdit(Form)
        self.ANGLE_lineEdit.setEnabled(False)
        self.ANGLE_lineEdit.setGeometry(QtCore.QRect(630, 240, 141, 21))
        self.ANGLE_lineEdit.setText("")
        self.ANGLE_lineEdit.setObjectName("ANGLE_lineEdit")
        self.label_30 = QtWidgets.QLabel(Form)
        self.label_30.setGeometry(QtCore.QRect(430, 290, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.BETA_lineEdit = QtWidgets.QLineEdit(Form)
        self.BETA_lineEdit.setEnabled(False)
        self.BETA_lineEdit.setGeometry(QtCore.QRect(650, 290, 121, 21))
        self.BETA_lineEdit.setText("")
        self.BETA_lineEdit.setObjectName("BETA_lineEdit")
        self.label_31 = QtWidgets.QLabel(Form)
        self.label_31.setGeometry(QtCore.QRect(40, 340, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.RO_lineEdit = QtWidgets.QLineEdit(Form)
        self.RO_lineEdit.setEnabled(False)
        self.RO_lineEdit.setGeometry(QtCore.QRect(190, 340, 171, 21))
        self.RO_lineEdit.setText("")
        self.RO_lineEdit.setObjectName("RO_lineEdit")
        self.label_32 = QtWidgets.QLabel(Form)
        self.label_32.setGeometry(QtCore.QRect(40, 290, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.RANGE_lineEdit = QtWidgets.QLineEdit(Form)
        self.RANGE_lineEdit.setEnabled(False)
        self.RANGE_lineEdit.setGeometry(QtCore.QRect(210, 290, 151, 21))
        self.RANGE_lineEdit.setText("")
        self.RANGE_lineEdit.setObjectName("RANGE_lineEdit")
        self.label_33 = QtWidgets.QLabel(Form)
        self.label_33.setGeometry(QtCore.QRect(430, 340, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.PHI_lineEdit = QtWidgets.QLineEdit(Form)
        self.PHI_lineEdit.setGeometry(QtCore.QRect(610, 60, 161, 21))
        self.PHI_lineEdit.setText("")
        self.PHI_lineEdit.setObjectName("PHI_lineEdit")
        self.label_34 = QtWidgets.QLabel(Form)
        self.label_34.setGeometry(QtCore.QRect(440, 50, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(-10, 150, 1001, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.COR_pushButton = QtWidgets.QPushButton(Form)
        self.COR_pushButton.setGeometry(QtCore.QRect(440, 180, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.COR_pushButton.setFont(font)
        self.COR_pushButton.setObjectName("COR_pushButton")
        self.BEFORE_pushButton = QtWidgets.QPushButton(Form)
        self.BEFORE_pushButton.setGeometry(QtCore.QRect(30, 110, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.BEFORE_pushButton.setFont(font)
        self.BEFORE_pushButton.setObjectName("BEFORE_pushButton")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(20, 180, 391, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.NEXT_pushButton = QtWidgets.QPushButton(Form)
        self.NEXT_pushButton.setGeometry(QtCore.QRect(150, 110, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.NEXT_pushButton.setFont(font)
        self.NEXT_pushButton.setObjectName("NEXT_pushButton")
        self.INSURE_pushButton = QtWidgets.QPushButton(Form)
        self.INSURE_pushButton.setGeometry(QtCore.QRect(560, 180, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.INSURE_pushButton.setFont(font)
        self.INSURE_pushButton.setObjectName("INSURE_pushButton")
        self.CERTAIN_pushButton = QtWidgets.QPushButton(Form)
        self.CERTAIN_pushButton.setGeometry(QtCore.QRect(270, 110, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.CERTAIN_pushButton.setFont(font)
        self.CERTAIN_pushButton.setObjectName("CERTAIN_pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "card3"))
        self.H1_lineEdit.setText(_translate("Form", "100"))
        self.label_26.setText(_translate("Form", "卫星高度(H1)"))
        self.LENN_comboBox.setItemText(0, _translate("Form", "短路径"))
        self.LENN_comboBox.setItemText(1, _translate("Form", "长路径"))
        self.label_27.setText(_translate("Form", "目标高度(H2)"))
        self.label_28.setText(_translate("Form", "目标天顶角(ANGLE)"))
        self.label_30.setText(_translate("Form", "相对地球中心角(BETA)"))
        self.label_31.setText(_translate("Form", "地球半径(RO)"))
        self.label_32.setText(_translate("Form", "路径长度(RANGE)"))
        self.label_33.setText(_translate("Form", "路径类型(LENN)"))
        self.label_34.setText(_translate("Form", "卫星天顶角(PHI)"))
        self.label_8.setText(_translate("Form", "主要修改参数"))
        self.COR_pushButton.setText(_translate("Form", "修改"))
        self.BEFORE_pushButton.setText(_translate("Form", "上一页"))
        self.label_9.setText(_translate("Form", "其它默认参数（一般不需修改）"))
        self.NEXT_pushButton.setText(_translate("Form", "下一页"))
        self.INSURE_pushButton.setText(_translate("Form", "确定"))
        self.CERTAIN_pushButton.setText(_translate("Form", "确定"))