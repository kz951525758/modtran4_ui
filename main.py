# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tape5(object):
    def setupUi(self, Tape5):
        Tape5.setObjectName("Tape5")
        Tape5.resize(800, 518)
        self.centralwidget = QtWidgets.QWidget(Tape5)
        self.centralwidget.setObjectName("centralwidget")
        Tape5.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tape5)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menuCARD_2 = QtWidgets.QMenu(self.menu_2)
        self.menuCARD_2.setObjectName("menuCARD_2")
        self.menuCARD_3 = QtWidgets.QMenu(self.menu_2)
        self.menuCARD_3.setObjectName("menuCARD_3")
        self.menu_MODTRAN = QtWidgets.QMenu(self.menubar)
        self.menu_MODTRAN.setObjectName("menu_MODTRAN")
        Tape5.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tape5)
        self.statusbar.setObjectName("statusbar")
        Tape5.setStatusBar(self.statusbar)
        self.actionCARD1 = QtWidgets.QAction(Tape5)
        self.actionCARD1.setObjectName("actionCARD1")
        self.actionCARD1A = QtWidgets.QAction(Tape5)
        self.actionCARD1A.setObjectName("actionCARD1A")
        self.actionCARD2 = QtWidgets.QAction(Tape5)
        self.actionCARD2.setObjectName("actionCARD2")
        self.actionCARD3 = QtWidgets.QAction(Tape5)
        self.actionCARD3.setObjectName("actionCARD3")
        self.actionCARD4 = QtWidgets.QAction(Tape5)
        self.actionCARD4.setObjectName("actionCARD4")
        self.actionCARD5 = QtWidgets.QAction(Tape5)
        self.actionCARD5.setObjectName("actionCARD5")
        self.actionCARD4plus = QtWidgets.QAction(Tape5)
        self.actionCARD4plus.setObjectName("actionCARD4plus")
        self.actionyunx = QtWidgets.QAction(Tape5)
        self.actionyunx.setObjectName("actionyunx")
        self.actionyunx_2 = QtWidgets.QAction(Tape5)
        self.actionyunx_2.setObjectName("actionyunx_2")
        self.actionCARD2A = QtWidgets.QAction(Tape5)
        self.actionCARD2A.setObjectName("actionCARD2A")
        self.actionCARD2B = QtWidgets.QAction(Tape5)
        self.actionCARD2B.setObjectName("actionCARD2B")
        self.actionCARD2C = QtWidgets.QAction(Tape5)
        self.actionCARD2C.setObjectName("actionCARD2C")
        self.actionCARD2D = QtWidgets.QAction(Tape5)
        self.actionCARD2D.setObjectName("actionCARD2D")
        self.actionCARD2E = QtWidgets.QAction(Tape5)
        self.actionCARD2E.setObjectName("actionCARD2E")
        self.actionCARD_3a = QtWidgets.QAction(Tape5)
        self.actionCARD_3a.setObjectName("actionCARD_3a")
        self.actionCARD3A = QtWidgets.QAction(Tape5)
        self.actionCARD3A.setObjectName("actionCARD3A")
        self.actionCARD3B = QtWidgets.QAction(Tape5)
        self.actionCARD3B.setObjectName("actionCARD3B")
        self.actioncard1a = QtWidgets.QAction(Tape5)
        self.actioncard1a.setObjectName("actioncard1a")
        self.actioncard1plus = QtWidgets.QAction(Tape5)
        self.actioncard1plus.setObjectName("actioncard1plus")
        self.actionRUN = QtWidgets.QAction(Tape5)
        self.actionRUN.setObjectName("actionRUN")
        self.actionCARD1Aplus = QtWidgets.QAction(Tape5)
        self.actionCARD1Aplus.setObjectName("actionCARD1Aplus")
        self.menu.addAction(self.actionCARD1)
        self.menu.addAction(self.actionCARD1A)
        self.menu.addAction(self.actionCARD2)
        self.menu.addAction(self.actionCARD3)
        self.menu.addAction(self.actionCARD4)
        self.menu.addAction(self.actionCARD5)
        self.menuCARD_2.addAction(self.actionCARD2A)
        self.menuCARD_2.addAction(self.actionCARD2B)
        self.menuCARD_2.addAction(self.actionCARD2C)
        self.menuCARD_2.addAction(self.actionCARD2D)
        self.menuCARD_2.addAction(self.actionCARD2E)
        self.menuCARD_3.addAction(self.actionCARD3A)
        self.menuCARD_3.addAction(self.actionCARD3B)
        self.menu_2.addAction(self.actionCARD1Aplus)
        self.menu_2.addAction(self.menuCARD_2.menuAction())
        self.menu_2.addAction(self.menuCARD_3.menuAction())
        self.menu_2.addAction(self.actionCARD4plus)
        self.menu_MODTRAN.addAction(self.actionRUN)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_MODTRAN.menuAction())

        self.retranslateUi(Tape5)
        QtCore.QMetaObject.connectSlotsByName(Tape5)

    def retranslateUi(self, Tape5):
        _translate = QtCore.QCoreApplication.translate
        Tape5.setWindowTitle(_translate("Tape5", "主页面"))
        self.menu.setTitle(_translate("Tape5", "必选参数"))
        self.menu_2.setTitle(_translate("Tape5", "可选参数"))
        self.menuCARD_2.setTitle(_translate("Tape5", "CARD 2+"))
        self.menuCARD_3.setTitle(_translate("Tape5", "CARD 3+"))
        self.menu_MODTRAN.setTitle(_translate("Tape5", "运行程序"))
        self.actionCARD1.setText(_translate("Tape5", "CARD1（运行模式）"))
        self.actionCARD1A.setText(_translate("Tape5", "CARD 1A（基本参数）"))
        self.actionCARD2.setText(_translate("Tape5", "CARD 2（气溶胶参数）"))
        self.actionCARD3.setText(_translate("Tape5", "CARD 3（几何参数）"))
        self.actionCARD4.setText(_translate("Tape5", "CARD 4（光谱参数）"))
        self.actionCARD5.setText(_translate("Tape5", "CARD 5（重复运行参数）"))
        self.actionCARD4plus.setText(_translate("Tape5", "CARD 4+"))
        self.actionyunx.setText(_translate("Tape5", "保存tape5文件"))
        self.actionyunx_2.setText(_translate("Tape5", "运行MODTRAN"))
        self.actionCARD2A.setText(_translate("Tape5", "CARD 2A"))
        self.actionCARD2B.setText(_translate("Tape5", "CARD 2B"))
        self.actionCARD2C.setText(_translate("Tape5", "CARD 2C"))
        self.actionCARD2D.setText(_translate("Tape5", "CARD 2D"))
        self.actionCARD2E.setText(_translate("Tape5", "CARD 2E"))
        self.actionCARD_3a.setText(_translate("Tape5", "CARD 3a"))
        self.actionCARD3A.setText(_translate("Tape5", "CARD 3A"))
        self.actionCARD3B.setText(_translate("Tape5", "CARD 3B"))
        self.actioncard1a.setText(_translate("Tape5", "card1a"))
        self.actioncard1plus.setText(_translate("Tape5", "card1+"))
        self.actionRUN.setText(_translate("Tape5", "运行程序"))
        self.actionCARD1Aplus.setText(_translate("Tape5", "CARD 1A+"))
