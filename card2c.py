# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'card2c.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(919, 705)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.ML_lineEdit = QtWidgets.QLineEdit(Form)
        self.ML_lineEdit.setEnabled(False)
        self.ML_lineEdit.setGeometry(QtCore.QRect(270, 60, 111, 21))
        self.ML_lineEdit.setText("")
        self.ML_lineEdit.setObjectName("ML_lineEdit")
        self.label_34 = QtWidgets.QLabel(Form)
        self.label_34.setGeometry(QtCore.QRect(20, 60, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.label_38 = QtWidgets.QLabel(Form)
        self.label_38.setGeometry(QtCore.QRect(540, 60, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.IRD1_comboBox = QtWidgets.QComboBox(Form)
        self.IRD1_comboBox.setEnabled(False)
        self.IRD1_comboBox.setGeometry(QtCore.QRect(790, 60, 101, 27))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.IRD1_comboBox.setFont(font)
        self.IRD1_comboBox.setEditable(False)
        self.IRD1_comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.IRD1_comboBox.setObjectName("IRD1_comboBox")
        self.IRD1_comboBox.addItem("")
        self.IRD1_comboBox.addItem("")
        self.label_39 = QtWidgets.QLabel(Form)
        self.label_39.setGeometry(QtCore.QRect(10, 100, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_39.setFont(font)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.IRD2_comboBox = QtWidgets.QComboBox(Form)
        self.IRD2_comboBox.setEnabled(False)
        self.IRD2_comboBox.setGeometry(QtCore.QRect(270, 100, 111, 27))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.IRD2_comboBox.setFont(font)
        self.IRD2_comboBox.setEditable(False)
        self.IRD2_comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.IRD2_comboBox.setObjectName("IRD2_comboBox")
        self.IRD2_comboBox.addItem("")
        self.IRD2_comboBox.addItem("")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(-10, 140, 1201, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(20, 160, 291, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_35 = QtWidgets.QLabel(Form)
        self.label_35.setGeometry(QtCore.QRect(20, 210, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.label_37 = QtWidgets.QLabel(Form)
        self.label_37.setGeometry(QtCore.QRect(150, 160, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.label_36 = QtWidgets.QLabel(Form)
        self.label_36.setGeometry(QtCore.QRect(330, 210, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.P_lineEdit = QtWidgets.QLineEdit(Form)
        self.P_lineEdit.setEnabled(False)
        self.P_lineEdit.setGeometry(QtCore.QRect(480, 210, 121, 21))
        self.P_lineEdit.setText("")
        self.P_lineEdit.setObjectName("P_lineEdit")
        self.T_lineEdit = QtWidgets.QLineEdit(Form)
        self.T_lineEdit.setEnabled(False)
        self.T_lineEdit.setGeometry(QtCore.QRect(770, 210, 121, 21))
        self.T_lineEdit.setText("")
        self.T_lineEdit.setObjectName("T_lineEdit")
        self.label_40 = QtWidgets.QLabel(Form)
        self.label_40.setGeometry(QtCore.QRect(630, 210, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.WMOL1_lineEdit = QtWidgets.QLineEdit(Form)
        self.WMOL1_lineEdit.setEnabled(False)
        self.WMOL1_lineEdit.setGeometry(QtCore.QRect(330, 250, 111, 21))
        self.WMOL1_lineEdit.setText("")
        self.WMOL1_lineEdit.setObjectName("WMOL1_lineEdit")
        self.label_41 = QtWidgets.QLabel(Form)
        self.label_41.setGeometry(QtCore.QRect(10, 250, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.WMOLX_lineEdit = QtWidgets.QLineEdit(Form)
        self.WMOLX_lineEdit.setEnabled(False)
        self.WMOLX_lineEdit.setGeometry(QtCore.QRect(770, 390, 121, 21))
        self.WMOLX_lineEdit.setText("")
        self.WMOLX_lineEdit.setObjectName("WMOLX_lineEdit")
        self.label_42 = QtWidgets.QLabel(Form)
        self.label_42.setGeometry(QtCore.QRect(470, 390, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.JCHAR_lineEdit = QtWidgets.QLineEdit(Form)
        self.JCHAR_lineEdit.setEnabled(False)
        self.JCHAR_lineEdit.setGeometry(QtCore.QRect(770, 250, 121, 21))
        self.JCHAR_lineEdit.setText("")
        self.JCHAR_lineEdit.setObjectName("JCHAR_lineEdit")
        self.label_44 = QtWidgets.QLabel(Form)
        self.label_44.setGeometry(QtCore.QRect(470, 250, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_44.setFont(font)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(Form)
        self.label_45.setGeometry(QtCore.QRect(20, 290, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_45.setFont(font)
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.JCHARX_lineEdit = QtWidgets.QLineEdit(Form)
        self.JCHARX_lineEdit.setEnabled(False)
        self.JCHARX_lineEdit.setGeometry(QtCore.QRect(330, 290, 111, 21))
        self.JCHARX_lineEdit.setText("")
        self.JCHARX_lineEdit.setObjectName("JCHARX_lineEdit")
        self.INSURE_pushButton = QtWidgets.QPushButton(Form)
        self.INSURE_pushButton.setGeometry(QtCore.QRect(260, 660, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.INSURE_pushButton.setFont(font)
        self.INSURE_pushButton.setObjectName("INSURE_pushButton")
        self.NEXT_pushButton = QtWidgets.QPushButton(Form)
        self.NEXT_pushButton.setGeometry(QtCore.QRect(140, 660, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.NEXT_pushButton.setFont(font)
        self.NEXT_pushButton.setObjectName("NEXT_pushButton")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(-10, 320, 1101, 16))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setLineWidth(5)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.BEFORE_pushButton = QtWidgets.QPushButton(Form)
        self.BEFORE_pushButton.setGeometry(QtCore.QRect(20, 660, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.BEFORE_pushButton.setFont(font)
        self.BEFORE_pushButton.setObjectName("BEFORE_pushButton")
        self.HMODEL_lineEdit = QtWidgets.QLineEdit(Form)
        self.HMODEL_lineEdit.setEnabled(False)
        self.HMODEL_lineEdit.setGeometry(QtCore.QRect(790, 100, 101, 21))
        self.HMODEL_lineEdit.setText("")
        self.HMODEL_lineEdit.setObjectName("HMODEL_lineEdit")
        self.label_43 = QtWidgets.QLabel(Form)
        self.label_43.setGeometry(QtCore.QRect(540, 100, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_43.setFont(font)
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(20, 340, 131, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_47 = QtWidgets.QLabel(Form)
        self.label_47.setGeometry(QtCore.QRect(160, 340, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_47.setFont(font)
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.WMOL2_lineEdit = QtWidgets.QLineEdit(Form)
        self.WMOL2_lineEdit.setEnabled(False)
        self.WMOL2_lineEdit.setGeometry(QtCore.QRect(330, 390, 111, 21))
        self.WMOL2_lineEdit.setText("")
        self.WMOL2_lineEdit.setObjectName("WMOL2_lineEdit")
        self.label_46 = QtWidgets.QLabel(Form)
        self.label_46.setGeometry(QtCore.QRect(10, 390, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_46.setFont(font)
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(-10, 420, 1101, 16))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setLineWidth(5)
        self.line_4.setMidLineWidth(0)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.label_48 = QtWidgets.QLabel(Form)
        self.label_48.setGeometry(QtCore.QRect(620, 340, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_48.setFont(font)
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(480, 340, 131, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.ZM_lineEdit = QtWidgets.QLineEdit(Form)
        self.ZM_lineEdit.setEnabled(False)
        self.ZM_lineEdit.setGeometry(QtCore.QRect(180, 210, 121, 21))
        self.ZM_lineEdit.setText("")
        self.ZM_lineEdit.setObjectName("ZM_lineEdit")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(20, 440, 131, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_49 = QtWidgets.QLabel(Form)
        self.label_49.setGeometry(QtCore.QRect(160, 440, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_49.setFont(font)
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(-10, 630, 1101, 16))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setLineWidth(5)
        self.line_5.setMidLineWidth(0)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.AHAZE_lineEdit = QtWidgets.QLineEdit(Form)
        self.AHAZE_lineEdit.setEnabled(False)
        self.AHAZE_lineEdit.setGeometry(QtCore.QRect(330, 480, 111, 21))
        self.AHAZE_lineEdit.setText("")
        self.AHAZE_lineEdit.setObjectName("AHAZE_lineEdit")
        self.label_50 = QtWidgets.QLabel(Form)
        self.label_50.setGeometry(QtCore.QRect(20, 480, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_50.setFont(font)
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.EQLWCZ_lineEdit = QtWidgets.QLineEdit(Form)
        self.EQLWCZ_lineEdit.setEnabled(False)
        self.EQLWCZ_lineEdit.setGeometry(QtCore.QRect(770, 480, 121, 21))
        self.EQLWCZ_lineEdit.setText("")
        self.EQLWCZ_lineEdit.setObjectName("EQLWCZ_lineEdit")
        self.label_51 = QtWidgets.QLabel(Form)
        self.label_51.setGeometry(QtCore.QRect(480, 480, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_51.setFont(font)
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.RRATZ_lineEdit = QtWidgets.QLineEdit(Form)
        self.RRATZ_lineEdit.setEnabled(False)
        self.RRATZ_lineEdit.setGeometry(QtCore.QRect(330, 520, 111, 21))
        self.RRATZ_lineEdit.setText("")
        self.RRATZ_lineEdit.setObjectName("RRATZ_lineEdit")
        self.IHA1_lineEdit = QtWidgets.QLineEdit(Form)
        self.IHA1_lineEdit.setEnabled(False)
        self.IHA1_lineEdit.setGeometry(QtCore.QRect(770, 520, 121, 21))
        self.IHA1_lineEdit.setText("")
        self.IHA1_lineEdit.setObjectName("IHA1_lineEdit")
        self.label_52 = QtWidgets.QLabel(Form)
        self.label_52.setGeometry(QtCore.QRect(480, 520, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_52.setFont(font)
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(Form)
        self.label_53.setGeometry(QtCore.QRect(20, 520, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_53.setFont(font)
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.ICLD1_lineEdit = QtWidgets.QLineEdit(Form)
        self.ICLD1_lineEdit.setEnabled(False)
        self.ICLD1_lineEdit.setGeometry(QtCore.QRect(330, 560, 111, 21))
        self.ICLD1_lineEdit.setText("")
        self.ICLD1_lineEdit.setObjectName("ICLD1_lineEdit")
        self.IVUL1_lineEdit = QtWidgets.QLineEdit(Form)
        self.IVUL1_lineEdit.setEnabled(False)
        self.IVUL1_lineEdit.setGeometry(QtCore.QRect(770, 560, 121, 21))
        self.IVUL1_lineEdit.setText("")
        self.IVUL1_lineEdit.setObjectName("IVUL1_lineEdit")
        self.label_54 = QtWidgets.QLabel(Form)
        self.label_54.setGeometry(QtCore.QRect(480, 560, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_54.setFont(font)
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(Form)
        self.label_55.setGeometry(QtCore.QRect(20, 560, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_55.setFont(font)
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.ISEA1_lineEdit = QtWidgets.QLineEdit(Form)
        self.ISEA1_lineEdit.setEnabled(False)
        self.ISEA1_lineEdit.setGeometry(QtCore.QRect(330, 600, 111, 21))
        self.ISEA1_lineEdit.setText("")
        self.ISEA1_lineEdit.setObjectName("ISEA1_lineEdit")
        self.label_56 = QtWidgets.QLabel(Form)
        self.label_56.setGeometry(QtCore.QRect(480, 600, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_56.setFont(font)
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(Form)
        self.label_57.setGeometry(QtCore.QRect(20, 600, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_57.setFont(font)
        self.label_57.setAlignment(QtCore.Qt.AlignCenter)
        self.label_57.setObjectName("label_57")
        self.ICHR_comboBox = QtWidgets.QComboBox(Form)
        self.ICHR_comboBox.setEnabled(False)
        self.ICHR_comboBox.setGeometry(QtCore.QRect(770, 600, 121, 27))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.ICHR_comboBox.setFont(font)
        self.ICHR_comboBox.setEditable(False)
        self.ICHR_comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.ICHR_comboBox.setObjectName("ICHR_comboBox")
        self.ICHR_comboBox.addItem("")
        self.ICHR_comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CARD 2C"))
        self.label_8.setText(_translate("Form", "CARD 2C"))
        self.label_34.setText(_translate("Form", "要插入的大气层数(ML)"))
        self.label_38.setText(_translate("Form", "是否读取CARD 2C2(IRD1)"))
        self.IRD1_comboBox.setItemText(0, _translate("Form", "不读取"))
        self.IRD1_comboBox.setItemText(1, _translate("Form", "读取"))
        self.label_39.setText(_translate("Form", "是否读取CARD 2C3(IRD2)"))
        self.IRD2_comboBox.setItemText(0, _translate("Form", "不读取"))
        self.IRD2_comboBox.setItemText(1, _translate("Form", "读取"))
        self.label_9.setText(_translate("Form", "CARD 2C1"))
        self.label_35.setText(_translate("Form", "边界层高度(ZM)"))
        self.label_37.setText(_translate("Form", "（每层输入以\",\"分隔）"))
        self.label_36.setText(_translate("Form", "层边界压强(P)"))
        self.label_40.setText(_translate("Form", "层边界温度(T)"))
        self.label_41.setText(_translate("Form", "单个分子种类密度(WMOL1(1-12))"))
        self.label_42.setText(_translate("Form", "重分子种类密度(WMOLX(1-13))"))
        self.label_44.setText(_translate("Form", "主要参数单位(JCHAR(1-14))"))
        self.label_45.setText(_translate("Form", "其它参数单位(JCHARX)"))
        self.INSURE_pushButton.setText(_translate("Form", "确定"))
        self.NEXT_pushButton.setText(_translate("Form", "下一页"))
        self.BEFORE_pushButton.setText(_translate("Form", "上一页"))
        self.label_43.setText(_translate("Form", "识别新大气模式(HMODEL)"))
        self.label_10.setText(_translate("Form", "CARDs 2C2"))
        self.label_47.setText(_translate("Form", "（每层输入以\",\"分隔）"))
        self.label_46.setText(_translate("Form", "单个分子种类密度(WMOL2(1-12))"))
        self.label_48.setText(_translate("Form", "（每层输入以\",\"分隔）"))
        self.label_11.setText(_translate("Form", "CARDs 2C3"))
        self.label_12.setText(_translate("Form", "CARDs 2C3"))
        self.label_49.setText(_translate("Form", "（每层输入以\",\"分隔）"))
        self.label_50.setText(_translate("Form", "气溶胶或云比例因子(AHAZE)"))
        self.label_51.setText(_translate("Form", "模型等效液态水含量(EQLWCZ)"))
        self.label_52.setText(_translate("Form", "ZM海拔气溶胶消光控制(IHA1)"))
        self.label_53.setText(_translate("Form", "海拔ZM处降雨率(RRATZ)"))
        self.label_54.setText(_translate("Form", "平流层气溶胶消光控制(IVUL1)"))
        self.label_55.setText(_translate("Form", "ZM海拔云消光控制(ICLD1)"))
        self.label_56.setText(_translate("Form", "用户定义气溶胶边界显示(ICHR)"))
        self.label_57.setText(_translate("Form", "ZM海拔气溶胶季节控制(ISEA1)"))
        self.ICHR_comboBox.setItemText(0, _translate("Form", "无边界变化"))
        self.ICHR_comboBox.setItemText(1, _translate("Form", "用户定义变化"))