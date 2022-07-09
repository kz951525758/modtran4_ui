#导入所需库
import sys
import os
import re
import numpy as np
import shutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtWidgets
from main import Ui_Tape5 as Main_Form
from card1 import Ui_Form as Card1_Form
from card1_plus import Ui_Form as Card1_plus_Form
from card1a import Ui_Form as Card1a_Form
from card2 import Ui_Form as Card2_Form
from card2a import Ui_Form as Card2a_Form
from card2b import Ui_Form as Card2b_Form
from card2c import Ui_Form as Card2c_Form
from card2d import Ui_Form as Card2d_Form
from card2e import Ui_Form as Card2e_Form
from card3 import Ui_Form as Card3_Form
from card3a import Ui_Form as Card3a_Form
from card3b import Ui_Form as Card3b_Form
from card4 import Ui_Form as Card4_Form
from card4_plus import Ui_Form as Card4_plus_Form
from card5 import Ui_Form as Card5_Form
from out import Ui_Form as Out_Form
class Start(QMainWindow, Main_Form):
    def __init__(self):
        super(Start, self).__init__()
        self.setupUi(self)
        self.actionCARD1Aplus.setEnabled(False)
        self.menuCARD_2.setEnabled(False)
        self.actionCARD2A.setEnabled(False)
        self.actionCARD2B.setEnabled(False)
        self.actionCARD2C.setEnabled(False)
        self.actionCARD2D.setEnabled(False)
        self.actionCARD2E.setEnabled(False)
        self.menuCARD_3.setEnabled(False)
        self.actionCARD3A.setEnabled(False)
        self.actionCARD3B.setEnabled(False)
        self.actionCARD4plus.setEnabled(False)

class CARD1(QMainWindow, Card1_Form):
    def __init__(self):
        super(CARD1, self).__init__()
        self.setupUi(self)
        self.NEXT_pushButton.clicked.connect(self.card1_next)
        self.COR_pushButton.clicked.connect(self.card1_cor)
        self.INSURE_pushButton.clicked.connect(self.card1_insure1)      #取消可修改
        self.INSURE_pushButton_2.clicked.connect(self.card1_insure2)    #关闭界面
    def card1_tiaozhuan(self):
        #   CARD2C使用条件
        model = self.MODEL_comboBox.currentIndex()
        im = self.IM_comboBox.currentIndex()
        if (im == 1) and ((model == 0) or (model == 7)):
            start_show.menuCARD_2.setEnabled(True)
            start_show.actionCARD2C.setEnabled(True)
            card2c_show.ML_lineEdit.setEnabled(True)
            card2c_show.IRD1_comboBox.setEnabled(True)
            card2c_show.IRD2_comboBox.setEnabled(True)
            card2c_show.HMODEL_lineEdit.setEnabled(True)
            card2c_show.ZM_lineEdit.setEnabled(True)
            card2c_show.P_lineEdit.setEnabled(True)
            card2c_show.T_lineEdit.setEnabled(True)
            card2c_show.WMOL1_lineEdit.setEnabled(True)
            card2c_show.JCHAR_lineEdit.setEnabled(True)
            card2c_show.JCHARX_lineEdit.setEnabled(True)
        else:
            start_show.actionCARD2C.setEnabled(False)
        a = start_show.actionCARD2A.isEnabled()
        b = start_show.actionCARD2B.isEnabled()
        c = start_show.actionCARD2C.isEnabled()
        d = start_show.actionCARD2D.isEnabled()
        e = start_show.actionCARD2E.isEnabled()
        if a or b or c or d or e:
            start_show.menuCARD_2.setEnabled(True)
        else:
            start_show.menuCARD_2.setEnabled(False)
        #CARD3A执行条件
        iemsct= self.IEMSCT_comboBox.currentIndex()
        if iemsct == 2:
            start_show.menuCARD_3.setEnabled(True)
            start_show.actionCARD3A.setEnabled(True)
            card3a_show.IPARM_comboBox.setEnabled(True)
            card3a_show.IPH_comboBox.setEnabled(True)
            card3a_show.IDAY_lineEdit.setEnabled(True)
            card3a_show.ISOURC_comboBox.setEnabled(True)
            card3a_show.PARM1_lineEdit.setEnabled(True)
            card3a_show.PARM2_lineEdit.setEnabled(True)
            card3a_show.G_comboBox.setEnabled(True)
        else:
            start_show.actionCARD3A.setEnabled(False)
        a1 = start_show.actionCARD3A.isEnabled()
        b1 = start_show.actionCARD3B.isEnabled()
        if a1 or b1 :
            start_show.menuCARD_3.setEnabled(True)
        else:
            start_show.menuCARD_3.setEnabled(False)
        #CARD 4+ 使用条件
        surrff = self.SURREF_lineEdit.text()
        if len(surrff) > 0:
            if surrff[0] == 'B' or surrff[0] == 'L' or \
                    surrff[0] == 'b' or surrff[0] == 'l':
                start_show.actionCARD4plus.setEnabled(True)
                card4_plus_show.NSURF_comboBox.setEnabled(True)
                card4_plus_show.AATEMP_lineEdit.setEnabled(True)
            else:
                start_show.actionCARD4plus.setEnabled(False)
            if surrff[0] == 'B' or surrff[0] == 'b':
                card4_plus_show.CBRDF_lineEdit.setEnabled(True)
                card4_plus_show.NWVSRF_lineEdit.setEnabled(True)
                card4_plus_show.SURFZN_lineEdit.setEnabled(True)
                card4_plus_show.SURFAZ_lineEdit.setEnabled(True)
                card4_plus_show.WVSURF_lineEdit.setEnabled(True)
                card4_plus_show.PARAMS_lineEdit.setEnabled(True)
            else:
                card4_plus_show.CBRDF_lineEdit.setEnabled(False)
                card4_plus_show.NWVSRF_lineEdit.setEnabled(False)
                card4_plus_show.SURFZN_lineEdit.setEnabled(False)
                card4_plus_show.SURFAZ_lineEdit.setEnabled(False)
                card4_plus_show.WVSURF_lineEdit.setEnabled(False)
                card4_plus_show.PARAMS_lineEdit.setEnabled(False)
            if surrff[0] == 'L' or surrff[0] == 'l':
                card4_plus_show.SALBFL_lineEdit.setEnabled(True)
                card4_plus_show.CSALB_lineEdit.setEnabled(True)
            else:
                card4_plus_show.SALBFL_lineEdit.setEnabled(False)
                card4_plus_show.CSALB_lineEdit.setEnabled(False)
        else:
            start_show.actionCARD4plus.setEnabled(False)
    def card1_gen(self):
        # 获取参数
        modtran_r = self.MODTRAN_comboBox.currentIndex()     #输入编号
        modtran_t = ['C', 'T', 'L']    #对应modtran输入
        modtran= modtran_t[modtran_r]
        speed_r = self.SPEED_comboBox.currentIndex()
        speed_t = ['M', 'S']
        speed = speed_t[speed_r]
        model = self.MODEL_comboBox.currentIndex()
        itype_r = self.ITYPE_comboBox.currentIndex()
        itype_t = [3, 1, 2]
        itype = itype_t[itype_r]
        iemsct = self.IEMSCT_comboBox.currentIndex()
        imult_r = self.IMULT_comboBox.currentIndex()
        imult_t = [1, 0]
        imult = imult_t[imult_r]
        m1 = self.M1_comboBox.currentIndex()
        m2 = self.M2_comboBox.currentIndex()
        m3 = self.M3_comboBox.currentIndex()
        m4 = self.M4_comboBox.currentIndex()
        m5 = self.M5_comboBox.currentIndex()
        m6 = self.M6_comboBox.currentIndex()
        mdef = self.MDEF_comboBox.currentIndex()
        im = self.IM_comboBox.currentIndex()
        noprnt_r = self.NOPRNT_comboBox.currentIndex()
        noprnt_t = [0, 1, -1, -2]
        noprnt = noprnt_t[noprnt_r]
        tptemp = geshi_float(self.TPTEMP_lineEdit.text())
        if tptemp == '':
            tptemp = 0
        surref = self.SURREF_lineEdit.text()
        if len(surref) > 0:
            if surref[0] == 'B' or surref[0] == 'L' or \
                 surref[0] == 'b' or surref[0] == 'l':
                surref = surref
            elif surref[0] == '-':
                surref = geshi_int(surref)
            else:
                surref = geshi_float(surref)
        else:
            surref =0
        card1 = CARD1_tog(modtran, speed, model, itype, iemsct, imult, m1, m2,
                      m3, m4, m5, m6, mdef, im, noprnt, tptemp, surref)
        return card1
    def card1_next(self):
        self.card1_tiaozhuan()
        card1a_show.show(), card1_show.close()
    def card1_cor(self):
        self.MODTRAN_comboBox.setEnabled(True)
        self.SPEED_comboBox.setEnabled(True)
        self.ITYPE_comboBox.setEnabled(True)
        self.IMULT_comboBox.setEnabled(True)
        self.M1_comboBox.setEnabled(True)
        self.M2_comboBox.setEnabled(True)
        self.M3_comboBox.setEnabled(True)
        self.M4_comboBox.setEnabled(True)
        self.M5_comboBox.setEnabled(True)
        self.M6_comboBox.setEnabled(True)
        self.MDEF_comboBox.setEnabled(True)
        self.IM_comboBox.setEnabled(True)
    def card1_insure1(self):
        self.card1_tiaozhuan()
        self.MODTRAN_comboBox.setEnabled(False)
        self.SPEED_comboBox.setEnabled(False)
        self.ITYPE_comboBox.setEnabled(False)
        self.IMULT_comboBox.setEnabled(False)
        self.M1_comboBox.setEnabled(False)
        self.M2_comboBox.setEnabled(False)
        self.M3_comboBox.setEnabled(False)
        self.M4_comboBox.setEnabled(False)
        self.M5_comboBox.setEnabled(False)
        self.M6_comboBox.setEnabled(False)
        self.MDEF_comboBox.setEnabled(False)
        self.IM_comboBox.setEnabled(False)
    def card1_insure2(self):
        self.card1_tiaozhuan()
        card1_show.close()

class CARD1A(QMainWindow, Card1a_Form):
    def __init__(self):
        super(CARD1A, self).__init__()
        self.setupUi(self)
        self.BEFORE_pushButton.clicked.connect(self.card1a_before)
        self.NEXT_pushButton.clicked.connect(self.card1a_next)
        self.COR_pushButton.clicked.connect(self.card1a_cor)
        self.Certain_pushButton.clicked.connect(self.card1a_certain)
        self.INSURE_pushButton.clicked.connect(self.card1a_insure)

    def card1a_tiaozhuan(self):
        #CARD1A+使用条件
        lsunfl = self.LSUNFL_comboBox.currentIndex()
        lbmnam = self.LBMNAM_comboBox.currentIndex()
        lfltnm = self.LFLTNM_MODEL.currentIndex()
        if (lsunfl == 1) or (lbmnam == 1) or (lfltnm == 1):
            start_show.actionCARD1Aplus.setEnabled(True)
            if lsunfl == 1:
                card1_plus_show.SUNFL2_comboBox.setEnabled(True)
            else:
                card1_plus_show.SUNFL2_comboBox.setEnabled(False)
            if lbmnam == 1:
                card1_plus_show.BMNAME_lineEdit.setEnabled(True)
            else:
                card1_plus_show.BMNAME_lineEdit.setEnabled(False)
            if lfltnm == 1:
                card1_plus_show.FILTNM_lineEdit.setEnabled(True)
            else:
                card1_plus_show.FILTNM_lineEdit.setEnabled(False)
        if (lsunfl == 0) and (lbmnam == 0) and (lfltnm == 0):
            start_show.actionCARD1Aplus.setEnabled(False)

    def card1a_gen(self):
        dis_r = self.DIS_comboBox.currentIndex()
        dis_t = ['T', 'F']
        dis = dis_t[dis_r]
        disazm_r = self.DISAZM_comboBox.currentIndex()
        disazm_t = ['T', 'F']
        disazm = disazm_t[disazm_r]
        nstr_r = self.NSTR_comboBox.currentIndex()
        nstr_t = [8, 2, 4, 16]
        nstr = nstr_t[nstr_r]
        lsun_r = self.LSUN_comboBox.currentIndex()
        lsun_t = ['F', 'T']
        lsun = lsun_t[lsun_r]
        isun= geshi_int(self.ISUN_lineEdit.text())
        co2mx = geshi_float(self.CO2_MXlineEdit.text())
        h2ostr= self.H2OSTR_lineEdit.text()
        o3str = self.O3STR_lineEdit.text()
        lsunfl_r = self.LSUNFL_comboBox.currentIndex()
        lsunfl_t = ['F', 'T']
        lsunfl = lsunfl_t[lsunfl_r]
        lbmnam_r = self.LBMNAM_comboBox.currentIndex()
        lbmnam_t = ['F', 'T']
        lbmnam = lbmnam_t[lbmnam_r]
        lfltnm_r = self.LFLTNM_MODEL.currentIndex()
        lfltnm_t = ['F', 'T']
        lfltnm = lfltnm_t[lfltnm_r]
        h2oaer_r = self.H2OAER_comboBox.currentIndex()
        h2oaer_t = ['F', 'T']
        h2oaer = h2oaer_t[h2oaer_r]
        solcon = geshi_float(self.SOLCON_lineEdit.text())
        card1a = CARD1A_tog(dis, disazm, nstr, lsun, isun, co2mx, h2ostr, o3str, lsunfl, lbmnam, lfltnm, h2oaer, solcon)
        return card1a

    def card1a_before(self):
        self.card1a_tiaozhuan()
        card1a_show.close(), card1_show.show()

    def card1a_next(self):
        self.card1a_tiaozhuan()
        if start_show.actionCARD1Aplus.isEnabled():
            card1a_show.close(), card1_plus_show.show()
        else:
            card1a_show.close(), card2_show.show()

    def card1a_cor(self):
        self.DIS_comboBox.setEnabled(True)
        self.NSTR_comboBox.setEnabled(True)
        self.DISAZM_comboBox.setEnabled(True)
        self.CO2_MXlineEdit.setEnabled(True)
        self.O3STR_lineEdit.setEnabled(True)
        self.LSUNFL_comboBox.setEnabled(True)
        self.LBMNAM_comboBox.setEnabled(True)
        self.H2OAER_comboBox.setEnabled(True)
        self.SOLCON_lineEdit.setEnabled(True)

    def card1a_certain(self):
        self.card1a_tiaozhuan()
        card1a_show.close()

    def card1a_insure(self):
        self.card1a_tiaozhuan()
        self.DIS_comboBox.setEnabled(False)
        self.NSTR_comboBox.setEnabled(False)
        self.DISAZM_comboBox.setEnabled(False)
        self.CO2_MXlineEdit.setEnabled(False)
        self.O3STR_lineEdit.setEnabled(False)
        self.LSUNFL_comboBox.setEnabled(False)
        self.LBMNAM_comboBox.setEnabled(False)
        self.H2OAER_comboBox.setEnabled(False)
        self.SOLCON_lineEdit.setEnabled(False)


class CARD1_PLUS(QMainWindow, Card1_plus_Form):
    def __init__(self):
        super(CARD1_PLUS, self).__init__()
        self.setupUi(self)
        self.BEFORE_pushButton.clicked.connect(self.card1_plus_before)
        self.NEXT_pushButton.clicked.connect(self.card1_plus_next)
        self.INSURE_pushButton.clicked.connect(self.card1_plus_insure)

    def card1_plus_gen(self):
        sunfl2= self.BMNAME_lineEdit_2.text()
        bmname= self.BMNAME_lineEdit.text()
        filtnm= self.FILTNM_lineEdit.text()
        card1a1 = CARD1A1_tog(sunfl2)
        card1a2 = CARD1A2_tog(bmname)
        card1a3 = CARD1A3_tog(filtnm)
        return card1a1, card1a2, card1a3

    def card1_plus_before(self):
        card1_plus_show.close(), card1a_show.show()

    def card1_plus_next(self):
        card1_plus_show.close(), card2_show.show()

    def card1_plus_insure(self):
        card1_plus_show.close()


class CARD2(QMainWindow, Card2_Form):
    def __init__(self):
        super(CARD2, self).__init__()
        self.setupUi(self)
        self.BEFORE_pushButton.clicked.connect(self.card2_before)
        self.NEXT_pushButton.clicked.connect(self.card2_next)
        self.Certain_pushButton.clicked.connect(self.card2_certain)
        self.COR_pushButton.clicked.connect(self.card2_cor)
        self.INSURE_pushButton.clicked.connect(self.card_insure)

    def card2_tiaozhuan(self):
        #   CARD2A+使用条件
        aplus = self.APLUS_comboBox.currentIndex()
        if aplus == 1:
            start_show.menuCARD_2.setEnabled(True)
            start_show.actionCARD2A.setEnabled(True)
            card2a_show.ZAERi1_lineEdit.setEnabled(True)
            card2a_show.ZAERi2_lineEdit.setEnabled(True)
            card2a_show.SCALEi_lineEdit.setEnabled(True)
        else:
            start_show.menuCARD_2.setEnabled(False)
            start_show.actionCARD2A.setEnabled(False)
            card2a_show.ZAERi1_lineEdit.setEnabled(False)
            card2a_show.ZAERi2_lineEdit.setEnabled(False)
            card2a_show.SCALEi_lineEdit.setEnabled(False)
        #   CARD2A使用条件
        icld = self.ICLD_comboBox.currentIndex()
        if 1 <= icld <= 10:
            start_show.menuCARD_2.setEnabled(True)
            start_show.actionCARD2A.setEnabled(True)
            card2a_show.CTHIK2_comboBox.setEnabled(True)
            card2a_show.CALT2_comboBox.setEnabled(True)
            card2a_show.CEXT2_comboBox.setEnabled(True)
            card2a_show.NCRALT_lineEdit.setEnabled(True)
            card2a_show.NCRSPC_lineEdit.setEnabled(True)
            card2a_show.CWAVLN_lineEdit.setEnabled(True)
            card2a_show.CHUMID_lineEdit.setEnabled(True)
            card2a_show.CCOLWD_comboBox.setEnabled(True)
            card2a_show.CCOLIP_comboBox.setEnabled(True)
            card2a_show.ASYMWD_comboBox.setEnabled(True)
            card2a_show.ASYMIP_comboBox.setEnabled(True)
            card2a_show.CTHIK_comboBox.setEnabled(False)
            card2a_show.CALT_comboBox.setEnabled(False)
            card2a_show.CEXT_comboBox.setEnabled(False)
        if (icld == 12) or (icld == 13):
            start_show.menuCARD_2.setEnabled(True)
            start_show.actionCARD2A.setEnabled(True)
            card2a_show.CTHIK2_comboBox.setEnabled(False)
            card2a_show.CALT2_comboBox.setEnabled(False)
            card2a_show.CEXT2_comboBox.setEnabled(False)
            card2a_show.NCRALT_lineEdit.setEnabled(False)
            card2a_show.NCRSPC_lineEdit.setEnabled(False)
            card2a_show.CWAVLN_lineEdit.setEnabled(False)
            card2a_show.CHUMID_lineEdit.setEnabled(False)
            card2a_show.CCOLWD_comboBox.setEnabled(False)
            card2a_show.CCOLIP_comboBox.setEnabled(False)
            card2a_show.ASYMWD_comboBox.setEnabled(False)
            card2a_show.ASYMIP_comboBox.setEnabled(False)
            card2a_show.CTHIK_comboBox.setEnabled(True)
            card2a_show.CALT_comboBox.setEnabled(True)
            card2a_show.CEXT_comboBox.setEnabled(True)
        if (aplus == 0) and ((icld == 0) or (icld == 11)):
            start_show.actionCARD2A.setEnabled(False)
        #   CARD2B使用条件
        ivsa = self.IVSA_comboBox.currentIndex()
        if ivsa == 1:
            start_show.menuCARD_2.setEnabled(True)
            start_show.actionCARD2B.setEnabled(True)
            card2b_show.ZCVSA_lineEdit.setEnabled(True)
            card2b_show.ZTVSA_lineEdit.setEnabled(True)
            card2b_show.ZINVSA_lineEdit.setEnabled(True)
        else:
            start_show.actionCARD2B.setEnabled(False)
        #CARDS 2D使用条件
        ihaze = self.IHAZE_comboBox.currentIndex()
        if ihaze == 8 or icld == 11:
            start_show.menuCARD_2.setEnabled(True)
            start_show.actionCARD2D.setEnabled(True)
            card2d_show.IREG1_comboBox.setEnabled(True)
            card2d_show.IREG2_comboBox.setEnabled(True)
            card2d_show.IREG3_comboBox.setEnabled(True)
            card2d_show.IREG4_comboBox.setEnabled(True)
        else:
            start_show.actionCARD2D.setEnabled(False)

        a = start_show.actionCARD2A.isEnabled()
        b = start_show.actionCARD2B.isEnabled()
        c = start_show.actionCARD2C.isEnabled()
        d = start_show.actionCARD2D.isEnabled()
        e = start_show.actionCARD2E.isEnabled()
        if a or b or c or d or e:
            start_show.menuCARD_2.setEnabled(True)
        else:
            start_show.menuCARD_2.setEnabled(False)

    def card2_gen(self):
        aplus_r = self.APLUS_comboBox.currentIndex()
        aplus_t = ['', 'A+']
        aplus = aplus_t[aplus_r]
        ihaze = self.IHAZE_comboBox.currentIndex()-1
        cnovam_r = self.CNOVAM_comboBox.currentIndex()
        cnovam_t = ['', 'N']
        cnovam = cnovam_t[cnovam_r]
        iseasn = self.ISEASN_comboBox.currentIndex()
        aruss = ''
        ivulcn = self.IVULCN_comboBox.currentIndex()+1
        icstl = geshi_int(self.ICSTL_lineEdit.text())
        icld = self.ICLD_comboBox.currentIndex()
        if icld >= 12:
            icld += 1
        ivsa = self.IVSA_comboBox.currentIndex()
        print('a')
        vis = geshi1(geshi_float(self.VIS_lineEdit.text()))
        wss = geshi_float(self.WSS_lineEdit.text())
        whh = geshi_float(self.WHH_lineEdit.text())
        rainrt = geshi_float(self.RAINRT_lineEdit.text())
        gndalt = geshi1(geshi_float(self.GNDALT_lineEdit.text()))
        card2 = CARD2_tog(aplus, ihaze, cnovam, iseasn, aruss, ivulcn,
                          icstl, icld, ivsa, vis, wss, whh, rainrt, gndalt)
        return card2

    def card2_before(self):
        self.card2_tiaozhuan()
        if start_show.actionCARD1Aplus.isEnabled():
            card2_show.close(), card1_plus_show.show()
        else:
            card2_show.close(), card1a_show.show()

    def card2_next(self):
        self.card2_tiaozhuan()
        if start_show.actionCARD2A.isEnabled():
            card2_show.close(), card2a_show.show()
        elif start_show.actionCARD2B.isEnabled():
            card2_show.close(), card2b_show.show()
        elif start_show.actionCARD2C.isEnabled():
            card2_show.close(), card2c_show.show()
        elif start_show.actionCARD2D.isEnabled():
            card2_show.close(), card2d_show.show()
        elif start_show.actionCARD2E.isEnabled():
            card2_show.close(), card2e_show.show()
        else:
            card2_show.close(), card3_show.show()

    def card2_cor(self):
        self.APLUS_comboBox.setEnabled(True)
        self.CNOVAM_comboBox.setEnabled(True)
        self.ISEASN_comboBox.setEnabled(True)
        self.IVULCN_comboBox.setEnabled(True)
        self.ICLD_comboBox.setEnabled(True)
        self.IVSA_comboBox.setEnabled(True)
        self.ICSTL_lineEdit.setEnabled(True)
        self.RAINRT_lineEdit.setEnabled(True)
        self.WSS_lineEdit.setEnabled(True)
        self.WHH_lineEdit.setEnabled(True)

    def card2_certain(self):
        self.card2_tiaozhuan()
        card2_show.close()

    def card_insure(self):
        self.card2_tiaozhuan()
        self.APLUS_comboBox.setEnabled(False)
        self.CNOVAM_comboBox.setEnabled(False)
        self.ISEASN_comboBox.setEnabled(False)
        self.IVULCN_comboBox.setEnabled(False)
        self.ICLD_comboBox.setEnabled(False)
        self.IVSA_comboBox.setEnabled(False)
        self.ICSTL_lineEdit.setEnabled(False)
        self.RAINRT_lineEdit.setEnabled(False)
        self.WSS_lineEdit.setEnabled(False)
        self.WHH_lineEdit.setEnabled(False)


class CARD2A(QMainWindow, Card2a_Form):
    def __init__(self):
        super(CARD2A, self).__init__()
        self.setupUi(self)
        self.BEFORE_pushButton.clicked.connect(self.card2a_before)
        self.NEXT_pushButton.clicked.connect(self.card2a_next)
        self.INSURE_pushButton.clicked.connect(self.card2a_certain)

    def card2a_tiaozhuan(self):
        ncralt= int(self.NCRALT_lineEdit.text())
        ncrspc= int(self.NCRSPC_lineEdit.text())
        if start_show.actionCARD2A.isEnabled():
            if ncralt >= 3 or ncrspc >= 2:
                start_show.actionCARD2E.setEnabled(True)
            else:
                start_show.actionCARD2E.setEnabled(False)
            if ncralt >= 3:
                card2e_show.ZCLD_lineEdit.setEnabled(True)
                card2e_show.CLD_lineEdit.setEnabled(True)
                card2e_show.CLDICE_lineEdit.setEnabled(True)
                card2e_show.RR_lineEdit.setEnabled(True)
            else:
                card2e_show.ZCLD_lineEdit.setEnabled(False)
                card2e_show.CLD_lineEdit.setEnabled(False)
                card2e_show.CLDICE_lineEdit.setEnabled(False)
                card2e_show.RR_lineEdit.setEnabled(False)
            if ncrspc >= 2:
                card2e_show.WAVLEN_lineEdit.setEnabled(True)
                card2e_show.EXTC_lineEdit.setEnabled(True)
                card2e_show.ABSC_lineEdit.setEnabled(True)
                card2e_show.ASYM_lineEdit.setEnabled(True)
                card2e_show.EXTC2_lineEdit.setEnabled(True)
                card2e_show.ABSC2_lineEdit.setEnabled(True)
                card2e_show.ASYM2_lineEdit.setEnabled(True)
            else:
                card2e_show.WAVLEN_lineEdit.setEnabled(False)
                card2e_show.EXTC_lineEdit.setEnabled(False)
                card2e_show.ABSC_lineEdit.setEnabled(False)
                card2e_show.ASYM_lineEdit.setEnabled(False)
                card2e_show.EXTC2_lineEdit.setEnabled(False)
                card2e_show.ABSC2_lineEdit.setEnabled(False)
                card2e_show.ASYM2_lineEdit.setEnabled(False)
        else:
            start_show.actionCARD2E.setEnabled(False)

    def card2a_gen(self):
        zaer1 = self.ZAERi1_lineEdit.text()
        if zaer1 =='':
            zaer1='0,2,10,30'
        zaer1 = douhao_cut(zaer1)

        zaer2 = self.ZAERi2_lineEdit.text()
        if zaer2 =='':
            zaer2 = '3,11,35,100'
        zaer2 = douhao_cut(zaer2)

        scale = self.SCALEi_lineEdit.text()
        if scale =='':
            scale = '0,0,0,0'
        scale = douhao_cut(scale)
        card2a_plus = CARD2A_PLUS_tog(geshi_int(zaer1[0]), geshi_int(zaer2[0]), geshi_int(scale[0]),
                                      geshi_int(zaer1[1]), geshi_int(zaer2[1]), geshi_int(scale[1]),
                                      geshi_int(zaer1[2]), geshi_int(zaer2[2]), geshi_int(scale[2]),
                                      geshi_int(zaer1[3]), geshi_int(zaer2[3]), geshi_int(scale[3]))

        cthik = geshi_float(self.CTHIK_lineEdit.text())
        calt = geshi_float(self.CALT_lineEdit.text())
        cext = geshi_float(self.CEXT_lineEdit.text())
        card2a = CARD2A_tog(cthik, calt, cext)

        cthik2 = geshi_float(self.CTHIK2_lineEdit.text())
        calt2 = geshi_float(self.CALT2_lineEdit.text())
        cext2 = geshi_float(self.CEXT2_lineEdit.text())
        ncralt = geshi_int(self.NCRALT_lineEdit.text())
        ncrspc = geshi_int(self.NCRSPC_lineEdit.text())
        cwavln = geshi_float(self.CWAVLN_lineEdit.text())
        chumid = geshi_float(self.CHUMID_lineEdit.text())
        ccolwd = geshi_float(self.CCOLWD_lineEdit.text())
        ccolip = geshi_float(self.CCOLIP_lineEdit.text())
        asymwd = geshi_float(self.ASYMWD_lineEdit.text())
        asymip = geshi_float(self.ASYMIP_lineEdit.text())
        card2a_alt = CARD2A_ALT_tog(cthik2, calt2, cext2, ncralt, ncrspc, cwavln,
                                    ccolwd, ccolip, chumid, asymwd, asymip)
        return card2a_plus, card2a, card2a_alt

    def card2a_before(self):
        self.card2a_tiaozhuan()
        card2a_show.close(), card2_show.show()

    def card2a_next(self):
        self.card2a_tiaozhuan()
        if start_show.actionCARD2B.isEnabled():
            card2a_show.close(), card2b_show.show()
        elif start_show.actionCARD2C.isEnabled():
            card2a_show.close(), card2c_show.show()
        elif start_show.actionCARD2D.isEnabled():
            card2a_show.close(), card2d_show.show()
        elif start_show.actionCARD2E.isEnabled():
            card2a_show.close(), card2e_show.show()
        else:
            card2a_show.close(), card3_show.show()

    def card2a_certain(self):
        self.card2a_tiaozhuan()
        card2a_show.close()


class CARD2B(QMainWindow, Card2b_Form):
    def __init__(self):
        super(CARD2B, self).__init__()
        self.setupUi(self)
        self.BEFORE_pushButton.clicked.connect(self.card2b_before)
        self.NEXT_pushButton.clicked.connect(self.card2b_next)
        self.INSURE_pushButton.clicked.connect(self.card2b_certain)

    def card2b_gen(self):
        zcvsa = geshi_float(self.ZCVSA_lineEdit.text())
        ztvsa = geshi_float(self.ZTVSA_lineEdit.text())
        zinvsa = geshi_float(self.ZINVSA_lineEdit.text())
        card2b= CARD2B_tog(zcvsa, ztvsa, zinvsa)
        return card2b

    def card2b_before(self):
        if start_show.actionCARD2A.isEnabled():
            card2b_show.close(), card2a_show.show()
        else:
            card2b_show.close(), card2_show.show()

    def card2b_next(self):
        if start_show.actionCARD2C.isEnabled():
            card2b_show.close(), card2c_show.show()
        elif start_show.actionCARD2D.isEnabled():
            card2b_show.close(), card2d_show.show()
        elif start_show.actionCARD2E.isEnabled():
            card2b_show.close(), card2e_show.show()
        else:
            card2b_show.close(), card3_show.show()

    def card2b_certain(self):
        card2b_show.close()


class CARD2C(QMainWindow, Card2c_Form):
    def __init__(self):
        super(CARD2C, self).__init__()
        self.setupUi(self)
        self.BEFORE_pushButton.clicked.connect(self.card2c_before)
        self.NEXT_pushButton.clicked.connect(self.card2c_next)
        self.INSURE_pushButton.clicked.connect(self.card2c_certain)
        self.IRD1_comboBox.currentIndexChanged.connect(self.card2c_tiaozhuan)
        self.IRD2_comboBox.currentIndexChanged.connect(self.card2c_tiaozhuan)
        card1_show.MDEF_comboBox.currentIndexChanged.connect(self.card2c_tiaozhuan)

    def card2c_tiaozhuan(self):
        ird1 = self.IRD1_comboBox.currentIndex()
        ird2 = self.IRD2_comboBox.currentIndex()
        mdef= card1_show.MDEF_comboBox.currentIndex()
        #CARD2C2 条件
        if ird1 == 1:
            self.WMOL2_lineEdit.setEnabled(True)
            if mdef == 1:
                self.WMOLX_lineEdit.setEnabled(True)
            else:
                self.WMOLX_lineEdit.setEnabled(False)
        else:
            self.WMOL2_lineEdit.setEnabled(False)

        #CARD2C3条件
        if ird2 ==1:
            self.AHAZE_lineEdit.setEnabled(True)
            self.EQLWCZ_lineEdit.setEnabled(True)
            self.RRATZ_lineEdit.setEnabled(True)
            self.IHA1_lineEdit.setEnabled(True)
            self.ICLD1_lineEdit.setEnabled(True)
            self.IVUL1_lineEdit.setEnabled(True)
            self.ISEA1_lineEdit.setEnabled(True)
            self.ICHR_comboBox.setEnabled(True)
        else:
            self.AHAZE_lineEdit.setEnabled(False)
            self.EQLWCZ_lineEdit.setEnabled(False)
            self.RRATZ_lineEdit.setEnabled(False)
            self.IHA1_lineEdit.setEnabled(False)
            self.ICLD1_lineEdit.setEnabled(False)
            self.IVUL1_lineEdit.setEnabled(False)
            self.ISEA1_lineEdit.setEnabled(False)
            self.ICHR_comboBox.setEnabled(False)

    def card2c_gen(self):
        def card2c_geshi1(data):
            if data != '':
                data = geshi_float(geshi1(douhao_cut(data)))
                return data
            else:
                return [0]
        def card2c_geshi2(data):
            if data != '':
                data = geshi_int(geshi1(douhao_cut(data)))
                return data
            else:
                data=0
                data= int(data)
                return [data]
        def card2c_geshi3(data):
            if data != '':
                data = geshi1(douhao_cut(data))
                return data
            else:
                return ['']

        ml = self.ML_lineEdit.text()
        if ml == '':
            ml = 1
        ird1 = self.IRD1_comboBox.currentIndex()
        ird2 = self.IRD2_comboBox.currentIndex()
        hmodel = self.HMODEL_lineEdit.text()
        card2c = CARD2C_tog(ml, ird1, ird2, hmodel)
        cards2c = ''
        for i in range(ml):
            zm = card2c_geshi1(self.ZM_lineEdit.text())
            p = card2c_geshi1(self.P_lineEdit.text())
            t = card2c_geshi1(self.T_lineEdit.text())
            wmol = card2c_geshi1(self.WMOL1_lineEdit.text())
            if len(wmol) == 1:
                wmol=['', '', '']
            jchar = card2c_geshi3(self.JCHAR_lineEdit.text())
            jcharx = self.JCHARX_lineEdit.text()
            mdef = card1_show.MDEF_comboBox.currentIndex()
            card2c1 = CARD2C1_tog(zm[i], p[i], t[i], wmol[3*i], wmol[3*i+1], wmol[3*i+2], jchar[i], jcharx)
            cards2c += card2c1 +'\n'
            if ird1 == 1:
                wmol2 = card2c_geshi1(self.WMOL2_lineEdit.text())
                card2c2 = CARD2C2_tog(wmol2[i])
                cards2c += card2c2 + '\n'
            if ird1 == 1 and mdef == 2:
                wmolx = card2c_geshi1(self.WMOLX_lineEdit.text())
                card2c2x = CARD2C2X_tog(wmolx[i])
                cards2c += card2c2x + '\n'
            if ird2 == 1 :
                ahaze = card2c_geshi1(self.AHAZE_lineEdit.text())
                eqlwcz = card2c_geshi1(self.EQLWCZ_lineEdit.text())
                rratz = card2c_geshi1(self.RRATZ_lineEdit.text())
                iha1 = card2c_geshi2(self.IHA1_lineEdit.text())
                icld1 = card2c_geshi2(self.ICLD1_lineEdit.text())
                ivul1 = card2c_geshi2(self.IVUL1_lineEdit.text())
                isea1 = card2c_geshi2(self.ISEA1_lineEdit.text())
                ichr = self.ICHR_comboBox.currentIndex()
                card2c3 = CARD2C3_tog(ahaze[i], eqlwcz[i], rratz[i], iha1[i], icld1[i], ivul1[i], isea1[i], ichr)
                cards2c += card2c3 + '\n'
        #去除最后回车
        cards2c = cards2c[:-2]
        return card2c, cards2c

    def card2c_before(self):
        self.card2c_tiaozhuan()
        if start_show.actionCARD2B.isEnabled():
            card2c_show.close(), card2b_show.show()
        elif start_show.actionCARD2A.isEnabled():
            card2c_show.close(), card2a_show.show()
        else:
            card2c_show.close(), card2_show.show()

    def card2c_next(self):
        self.card2c_tiaozhuan()
        if start_show.actionCARD2D.isEnabled():
            card2c_show.close(), card2d_show.show()
        elif start_show.actionCARD2E.isEnabled():
            card2c_show.close(), card2e_show.show()
        else:
            card2c_show.close(), card3_show.show()

    def card2c_certain(self):
        self.card2c_tiaozhuan()
        card2c_show.close()


class CARD2D(QMainWindow, Card2d_Form):
    def __init__(self):
        super(CARD2D, self).__init__()
        self.setupUi(self)
        self.IREG1_comboBox.currentIndexChanged.connect(self.card2d_tiaozhuan)
        self.IREG2_comboBox.currentIndexChanged.connect(self.card2d_tiaozhuan)
        self.IREG3_comboBox.currentIndexChanged.connect(self.card2d_tiaozhuan)
        self.IREG4_comboBox.currentIndexChanged.connect(self.card2d_tiaozhuan)
        self.BEFORE_pushButton.clicked.connect(self.card2d_before)
        self.NEXT_pushButton.clicked.connect(self.card2d_next)
        self.INSURE_pushButton.clicked.connect(self.card2d_certain)

    def card2d_tiaozhuan(self):
        ireg1 = self.IREG1_comboBox.currentIndex()
        ireg2 = self.IREG2_comboBox.currentIndex()
        ireg3 = self.IREG3_comboBox.currentIndex()
        ireg4 = self.IREG4_comboBox.currentIndex()
        if ireg1 == 1 or ireg2 == 1 or ireg3 == 1 or ireg4 == 1:
            card2d_show.AWCCON_lineEdit.setEnabled(True)
            card2d_show.TITLE_lineEdit.setEnabled(True)
            card2d_show.VARSPC_lineEdit.setEnabled(True)
            card2d_show.EXTC_lineEdit.setEnabled(True)
            card2d_show.ABSC_lineEdit.setEnabled(True)
            card2d_show.ASYM_lineEdit.setEnabled(True)
        else:
            card2d_show.AWCCON_lineEdit.setEnabled(False)
            card2d_show.TITLE_lineEdit.setEnabled(False)
            card2d_show.VARSPC_lineEdit.setEnabled(False)
            card2d_show.EXTC_lineEdit.setEnabled(False)
            card2d_show.ABSC_lineEdit.setEnabled(False)
            card2d_show.ASYM_lineEdit.setEnabled(False)

    def card2d_gen(self):
        ireg1 = self.IREG1_comboBox.currentIndex()
        ireg2 = self.IREG2_comboBox.currentIndex()
        ireg3 = self.IREG3_comboBox.currentIndex()
        ireg4 = self.IREG4_comboBox.currentIndex()
        card2d = CARD2D_tog(ireg1, ireg2, ireg3, ireg4)
        awccon = geshi_float(self.AWCCON_lineEdit.text())
        title = geshi_float(self.TITLE_lineEdit.text())
        card2d1 = CARD2D1_tog(awccon, title)
        varspc = geshi_float(self.VARSPC_lineEdit.text())
        extc = geshi_float(self.EXTC_lineEdit.text())
        absc = geshi_float(self.ABSC_lineEdit.text())
        asym = geshi_float(self.ASYM_lineEdit.text())
        card2d2 = CARD2D2_tog(varspc, extc, absc, asym)
        return card2d, card2d1, card2d2

    def card2d_before(self):
        if start_show.actionCARD2C.isEnabled():
            card2d_show.close(), card2c_show.show()
        elif start_show.actionCARD2B.isEnabled():
            card2d_show.close(), card2b_show.show()
        elif start_show.actionCARD2A.isEnabled():
            card2d_show.close(), card2a_show.show()
        else:
            card2c_show.close(), card2_show.show()

    def card2d_next(self):
        if start_show.actionCARD2E.isEnabled():
            card2d_show.close(), card2e_show.show()
        else:
            card2d_show.close(), card3_show.show()

    def card2d_certain(self):
        card2d_show.close()


class CARD2E(QMainWindow, Card2e_Form):
    def __init__(self):
        super(CARD2E, self).__init__()
        self.setupUi(self)
        self.BEFORE_pushButton.clicked.connect(self.card2e_before)
        self.NEXT_pushButton.clicked.connect(self.card2e_next)
        self.INSURE_pushButton.clicked.connect(self.card2e_certain)

    def card2e_gen(self):
        zcld = geshi_float(self.ZCLD_lineEdit.text())
        cld = geshi_float(self.CLD_lineEdit.text())
        cldice = geshi_float(self.CLDICE_lineEdit.text())
        rr = geshi_float(self.RR_lineEdit.text())
        card2e1 = CARD2E1_tog(zcld, cld, cldice, rr)

        wavlen = geshi_float(self.WAVLEN_lineEdit.text())
        extc = geshi_float(self.EXTC_lineEdit.text())
        absc = geshi_float(self.ABSC_lineEdit.text())
        asym = geshi_float(self.ASYM_lineEdit.text())
        extc2 = geshi_float(self.EXTC2_lineEdit.text())
        absc2 = geshi_float(self.ABSC2_lineEdit.text())
        asym2 = geshi_float(self.ASYM2_lineEdit.text())
        card2e2 = CARD2E2_tog(wavlen, extc, absc, asym, extc2, absc2 , asym2)
        return card2e1, card2e2

    def card2e_before(self):
        if start_show.actionCARD2D.isEnabled():
            card2e_show.close(), card2d_show.show()
        elif start_show.actionCARD2C.isEnabled():
            card2e_show.close(), card2c_show.show()
        elif start_show.actionCARD2B.isEnabled():
            card2e_show.close(), card2b_show.show()
        elif start_show.actionCARD2A.isEnabled():
            card2e_show.close(), card2a_show.show()
        else:
            card2e_show.close(), card2_show.show()

    def card2e_next(self):
        card2e_show.close(), card3_show.show()

    def card2e_certain(self):
        card2e_show.close()


class CARD3(QMainWindow, Card3_Form):
    def __init__(self):
        super(CARD3, self).__init__()
        self.setupUi(self)
        self.BEFORE_pushButton.clicked.connect(self.card3_before)
        self.NEXT_pushButton.clicked.connect(self.card3_next)
        self.CERTAIN_pushButton.clicked.connect(self.card3_certain)
        self.COR_pushButton.clicked.connect(self.card3_cor)
        self.INSURE_pushButton.clicked.connect(self.card3_insure)

    def card3_gen(self):
        h1 = geshi_float(self.H1_lineEdit.text())
        h2 = geshi_float(self.H2_lineEdit.text())
        angle = geshi_float(self.ANGLE_lineEdit.text())
        range1 = geshi_float(self.RANGE_lineEdit.text())
        beta = geshi_float(self.BETA_lineEdit.text())
        ro = geshi_float(self.RO_lineEdit.text())
        lenn = self.LENN_comboBox.currentIndex()
        phi = geshi_float(self.PHI_lineEdit.text())
        card3 = CARD3_tog(h1, h2, angle, range1, beta, ro, lenn, phi)
        return card3

    def card3_before(self):
        if start_show.actionCARD2E.isEnabled():
            card3_show.close(), card2e_show.show()
        elif start_show.actionCARD2D.isEnabled():
            card3_show.close(), card2d_show.show()
        elif start_show.actionCARD2C.isEnabled():
            card3_show.close(), card2c_show.show()
        elif start_show.actionCARD2B.isEnabled():
            card3_show.close(), card2b_show.show()
        elif start_show.actionCARD2A.isEnabled():
            card3_show.close(), card2a_show.show()
        else:
            card3_show.close(), card2_show.show()

    def card3_next(self):
        if start_show.actionCARD3A.isEnabled():
            card3_show.close(), card3a_show.show()
        elif start_show.actionCARD3B.isEnabled():
            card3_show.close(), card3b_show.show()
        else:
            card3_show.close(), card4_show.show()

    def card3_cor(self):
        self.H1_lineEdit.setEnabled(True)
        self.ANGLE_lineEdit.setEnabled(True)
        self.RANGE_lineEdit.setEnabled(True)
        self.BETA_lineEdit.setEnabled(True)
        self.RO_lineEdit.setEnabled(True)
        self.LENN_comboBox.setEnabled(True)

    def card3_insure(self):
        self.H1_lineEdit.setEnabled(False)
        self.ANGLE_lineEdit.setEnabled(False)
        self.RANGE_lineEdit.setEnabled(False)
        self.BETA_lineEdit.setEnabled(False)
        self.RO_lineEdit.setEnabled(False)
        self.LENN_comboBox.setEnabled(False)

    def card3_certain(self):
        card3_show.close()


class CARD3A(QMainWindow, Card3a_Form):
    def __init__(self):
        super(CARD3A, self).__init__()
        self.setupUi(self)
        self.IPARM_comboBox.currentIndexChanged.connect(self.card3a_tiaozhuan)
        self.ISOURC_comboBox.currentIndexChanged.connect(self.card3a_tiaozhuan)
        self.IPH_comboBox.currentIndexChanged.connect(self.card3a_tiaozhuan)
        self.BEFORE_pushButton.clicked.connect(self.card3a_before)
        self.NEXT_pushButton.clicked.connect(self.card3a_next)
        self.INSURE_pushButton.clicked.connect(self.card3a_certain)

    def card3a_tiaozhuan(self):
        iparm = self.IPARM_comboBox.currentIndex()
        isourc = self.ISOURC_comboBox.currentIndex()
        iph= self.IPH_comboBox.currentIndex()
        if isourc==1 and (iparm == 0 or iparm==1 or iparm == 3 or iparm==4):
            self.ANGLEM_lineEdit.setEnabled(True)
        else:
            self.ANGLEM_lineEdit.setEnabled(False)

        if iph == 0:
            self.G_comboBox.setEnabled(True)
        else:
            self.G_comboBox.setEnabled(False)

        if iparm == 0 or iparm==3:     #IPARM值为12或2
            self.PARM3_lineEdit.setEnabled(False)
            self.PARM4_lineEdit.setEnabled(False)
            self.TIME_lineEdit.setEnabled(False)
            self.PSIPO_lineEdit.setEnabled(False)
        elif iparm == 1 or iparm== 4:     #IPARM值为0或10
            self.PARM3_lineEdit.setEnabled(True)
            self.PARM4_lineEdit.setEnabled(True)
            self.TIME_lineEdit.setEnabled(False)
            self.PSIPO_lineEdit.setEnabled(True)
        else:      #IPARM值为11或1
            self.PARM3_lineEdit.setEnabled(False)
            self.PARM4_lineEdit.setEnabled(False)
            self.TIME_lineEdit.setEnabled(True)
            self.PSIPO_lineEdit.setEnabled(True)

        #CARD3B 条件
        if iph ==1:
            start_show.actionCARD3B.setEnabled(True)
            card3b_show.NANGLS_lineEdit.setEnabled(True)
            card3b_show.ANGF_lineEdit.setEnabled(True)
            card3b_show.F1_lineEdit.setEnabled(True)
            card3b_show.F2_lineEdit.setEnabled(True)
            card3b_show.F3_lineEdit.setEnabled(True)
            card3b_show.F4_lineEdit.setEnabled(True)
        else:
            start_show.actionCARD3B.setEnabled(True)

    def card3a_gen(self):
        iparm= self.IPARM_comboBox.currentIndex()
        iph = self.IPH_comboBox.currentIndex()
        iday = self.IDAY_lineEdit.text()
        if iday == '':
            iday = 93
        else:
            iday = geshi_int(iday)
        isourc = self.ISOURC_comboBox.currentIndex()
        card3a1 = CARD3A1_tog(iparm, iph, iday, isourc)

        parm1 = geshi2(self.PARM1_lineEdit.text())
        parm2 = geshi2(self.PARM2_lineEdit.text())
        parm3 = geshi2(self.PARM3_lineEdit.text())
        parm4 = geshi2(self.PARM4_lineEdit.text())
        time = geshi2(self.TIME_lineEdit.text())
        psipo = geshi2(self.PSIPO_lineEdit.text())
        anglem = geshi2(self.ANGLEM_lineEdit.text())
        g = self.G_comboBox.currentIndex()
        card3a2 = CARD3A2_tog(parm1, parm2, parm3, parm4, time, psipo, anglem, g)
        return card3a1, card3a2

    def card3a_before(self):
        card3a_show.close(), card3_show.show()

    def card3a_next(self):
        if start_show.actionCARD3B.isEnabled():
            card3a_show.close(), card3b_show.show()
        else:
            card3a_show.close(), card4_show.show()

    def card3a_certain(self):
        card3a_show.close()


class CARD3B(QMainWindow, Card3b_Form):
    def __init__(self):
        super(CARD3B, self).__init__()
        self.setupUi(self)
        self.BEFORE_pushButton.clicked.connect(self.card3b_before)
        self.NEXT_pushButton.clicked.connect(self.card3b_next)
        self.INSURE_pushButton.clicked.connect(self.card3b_certain)

    def card3b_gen(self):
        nangls = geshi_int(card3b_show.NANGLS_lineEdit.text())
        card3b1 = CARD3B1_tog(nangls)

        angf = geshi_float(card3b_show.ANGF_lineEdit.text())
        f1 = geshi_float(card3b_show.F1_lineEdit.text())
        f2 = geshi_float(card3b_show.F2_lineEdit.text())
        f3 = geshi_float(card3b_show.F3_lineEdit.text())
        f4 = geshi_float(card3b_show.F4_lineEdit.text())
        card3b2 = CARD3B2_tog(angf, f1, f2, f3, f4)
        return card3b1, card3b2

    def card3b_before(self):
        card3b_show.close(), card3a_show.show()

    def card3b_next(self):
        card3b_show.close(), card4_show.show()

    def card3b_certain(self):
        card3b_show.close()


class CARD4(QMainWindow, Card4_Form):
    def __init__(self):
        super(CARD4, self).__init__()
        self.setupUi(self)
        self.BEFORE_pushButton.clicked.connect(self.card4_before)
        self.NEXT_pushButton.clicked.connect(self.card4_next)
        self.CERTAIN_pushButton.clicked.connect(self.card4_certain)
        self.COR_pushButton.clicked.connect(self.card4_cor)
        self.INSURE_pushButton.clicked.connect(self.card4_insure)

    def card4_gen(self):
        v1 = geshi_float(self.V1_lineEdit.text())
        v2 = geshi_float(self.V2_lineEdit.text())
        dv = geshi_float(self.DV_lineEdit.text())
        fwhm = geshi_float(self.FWHM_lineEdit.text())
        yflag_r = self.YFLAG_comboBox.currentIndex()
        yflag_t = ['R', 'T']
        yflag = yflag_t[yflag_r]
        xflag_r = self.XFLAG_comboBox.currentIndex()
        xflag_t = ['W', 'M', 'N']
        xflag = xflag_t[xflag_r]
        dlimit = self.DLIMIT_lineEdit.text()
        flags1_r = self.FLAGS1_comboBox.currentIndex()
        flags1_t = ['W', 'M', 'N']
        flags1 = flags1_t[flags1_r]
        flags2 = str(self.FLAGS2_comboBox.currentIndex()+1)
        flags3_r = self.FLAGS3_comboBox.currentIndex()
        flags3_t = ['A', 'R']
        flags3 = flags3_t[flags3_r]
        flags4_r = self.FLAGS3_comboBox.currentIndex()
        flags4_t = [' ', 'A']
        flags4 = flags4_t[flags4_r]
        flags5_r = self.FLAGS3_comboBox.currentIndex()
        flags5_t = [' ', 'S']
        flags5 = flags5_t[flags5_r]
        flags6_r = self.FLAGS3_comboBox.currentIndex()
        flags6_t = [' ', 'R']
        flags6 = flags6_t[flags6_r]
        flags7_r = self.FLAGS3_comboBox.currentIndex()
        flags7_t = [' ', 'T', 'F']
        flags7 = flags7_t[flags7_r]
        flags = flags1+ flags2+ flags3+ flags4+ flags5+ flags6+ flags7
        card4 = CARD4_tog(v1, v2, dv, fwhm, yflag, xflag, dlimit, flags)
        return card4

    def card4_cor(self):
        self.YFLAG_comboBox.setEnabled(True)
        self.DLIMIT_lineEdit.setEnabled(True)
        self.XFLAG_comboBox.setEnabled(True)
        self.FLAGS1_comboBox.setEnabled(True)
        self.FLAGS2_comboBox.setEnabled(True)
        self.FLAGS3_comboBox.setEnabled(True)
        self.FLAGS4_comboBox.setEnabled(True)
        self.FLAGS5_comboBox.setEnabled(True)
        self.FLAGS6_comboBox.setEnabled(True)
        self.FLAGS7_comboBox.setEnabled(True)

    def card4_insure(self):
        self.YFLAG_comboBox.setEnabled(False)
        self.DLIMIT_lineEdit.setEnabled(False)
        self.XFLAG_comboBox.setEnabled(False)
        self.FLAGS1_comboBox.setEnabled(False)
        self.FLAGS2_comboBox.setEnabled(False)
        self.FLAGS3_comboBox.setEnabled(False)
        self.FLAGS4_comboBox.setEnabled(False)
        self.FLAGS5_comboBox.setEnabled(False)
        self.FLAGS6_comboBox.setEnabled(False)
        self.FLAGS7_comboBox.setEnabled(False)

    def card4_before(self):
        if start_show.actionCARD3B.isEnabled():
            card4_show.close(), card3b_show.show()
        elif start_show.actionCARD3A.isEnabled():
            card4_show.close(), card3a_show.show()
        else:
            card4_show.close(), card3_show.show()

    def card4_next(self):
        if start_show.actionCARD4plus.isEnabled():
            card4_show.close(), card4_plus_show.show()
        else:
            card4_show.close(), card5_show.show()

    def card4_certain(self):
        card4_show.close()


class CARD4_PLUS(QMainWindow, Card4_plus_Form):
    def __init__(self):
        super(CARD4_PLUS, self).__init__()
        self.setupUi(self)
        self.BEFORE_pushButton.clicked.connect(self.card4_plus_before)
        self.NEXT_pushButton.clicked.connect(self.card4_plus_next)
        self.INSURE_pushButton.clicked.connect(self.card4_plus_certain)

    def card4_plus_gen(self):
        nsurf = self.NSURF_comboBox.currentIndex() + 1
        aatemp = geshi1(self.AATEMP_lineEdit.text())
        card4a = CARD4A_tog(nsurf, aatemp)

        cbrdf = self.CBRDF_lineEdit.text()
        card4b1 = CARD4B1_tog(cbrdf)

        nwvsrf = self.NWVSRF_lineEdit.text()
        surfzn = self.SURFZN_lineEdit.text()
        surfaz = self.SURFAZ_lineEdit.text()
        card4b2 = CARD4B2_tog(nwvsrf, surfzn, surfaz)

        wvsurf = self.WVSURF_lineEdit.text()
        params = self.PARAMS_lineEdit.text()
        card4b3 = CARD4B3_tog(wvsurf, params)

        salbfl = self.SALBFL_lineEdit.text()
        card4l1 = CARD4L1_tog(salbfl)

        csalb = self.CSALB_lineEdit.text()
        card4l2 = CARD4L2_tog(csalb)
        return card4a, card4b1, card4b2, card4b3, card4l1, card4l2

    def card4_plus_before(self):
        card4_plus_show.close(), card4_show.show()

    def card4_plus_next(self):
        card4_plus_show.close(), card5_show.show()

    def card4_plus_certain(self):
        card4_plus_show.close()


class CARD5(QMainWindow, Card5_Form):
    def __init__(self):
        super(CARD5, self).__init__()
        self.setupUi(self)
        self.BEFORE_pushButton.clicked.connect(self.card5_before)
        self.NEXT_pushButton.clicked.connect(self.card5_next)
        self.INSURE_pushButton.clicked.connect(self.card5_certain)
        self.FUYUAN_pushButton.clicked.connect(self.card5_fuyuan)
        self.TAPE5_pushButton.clicked.connect(self.tape5_gen)

    def card5_tiaozhuan(self):
        irpt = self.IRPT_comboBox.currentIndex()
        if irpt == 0:
            start_show.actionCARD1.setEnabled(False)
            start_show.actionCARD1A.setEnabled(False)
            start_show.actionCARD2.setEnabled(False)
            start_show.actionCARD3.setEnabled(False)
            start_show.actionCARD4.setEnabled(False)
            start_show.actionCARD5.setEnabled(False)
            start_show.actionCARD1Aplus.setEnabled(False)
            start_show.actionCARD4plus.setEnabled(False)
            start_show.menuCARD_2.setEnabled(False)
            start_show.menuCARD_3.setEnabled(False)

        elif irpt == 1:
            start_show.actionCARD1.setEnabled(True)
            start_show.actionCARD1A.setEnabled(True)
            start_show.actionCARD2.setEnabled(True)
            start_show.actionCARD3.setEnabled(True)
            start_show.actionCARD4.setEnabled(True)
        elif irpt == 2:
            start_show.actionCARD1.setEnabled(False)
            start_show.actionCARD1A.setEnabled(False)
            start_show.actionCARD1Aplus.setEnabled(False)
            start_show.actionCARD2.setEnabled(False)
            start_show.menuCARD_2.setEnabled(False)
            start_show.actionCARD3.setEnabled(True)
            start_show.actionCARD4.setEnabled(True)
        else:
            start_show.actionCARD1.setEnabled(False)
            start_show.actionCARD1A.setEnabled(False)
            start_show.actionCARD1Aplus.setEnabled(False)
            start_show.actionCARD2.setEnabled(False)
            start_show.actionCARD3.setEnabled(False)
            start_show.menuCARD_2.setEnabled(False)
            start_show.menuCARD_3.setEnabled(False)
            start_show.actionCARD4.setEnabled(True)

    def tape5_gen(self):
        self.BEFORE_pushButton.setEnabled(True)
        self.NEXT_pushButton.setEnabled(True)
        self.INSURE_pushButton.setEnabled(True)
        self.TAPE5_pushButton.setEnabled(False)
        tape5_tog()

    def card5_gen(self):
        irpt_r = self.IRPT_comboBox.currentIndex()
        irpt_t = [0, -1, -3, -4]
        irpt = irpt_t[irpt_r]
        card5 = CARD5_tog(irpt)
        return card5

    def card5_before(self):
        if start_show.actionCARD4plus.isEnabled():
            card5_show.close(), card4_plus_show.show()
        else:
            card5_show.close(), card4_show.show()

    def card5_next(self):
        self.card5_tiaozhuan()
        self.NEXT_pushButton.setEnabled(False)
        self.INSURE_pushButton.setEnabled(False)
        self.TAPE5_pushButton.setEnabled(True)
        irpt = self.IRPT_comboBox.currentIndex()
        if irpt == 0:
            card5_show.close(), out_show.show()
        elif irpt == 1:
            card5_show.close(), card1_show.show()
        elif irpt == 2:
            card5_show.close(), card3_show.show()
        else:
            card5_show.close(), card4_show.show()

    def card5_certain(self):
        self.card5_tiaozhuan()
        self.NEXT_pushButton.setEnabled(False)
        self.INSURE_pushButton.setEnabled(False)
        self.TAPE5_pushButton.setEnabled(True)
        irpt = self.IRPT_comboBox.currentIndex()
        if irpt == 0:
            card5_show.close(), out_show.show()
        elif irpt == 1:
            card5_show.close(), card1_show.show()
        elif irpt == 2:
            card5_show.close(), card3_show.show()
        else:
            card5_show.close(), card4_show.show()

    def card5_fuyuan(self):
        self.NEXT_pushButton.setEnabled(True)
        self.INSURE_pushButton.setEnabled(True)
        self.TAPE5_pushButton.setEnabled(False)


class OUT(QMainWindow, Out_Form):
    def __init__(self):
        super(OUT, self).__init__()
        self.setupUi(self)
        self.out_toolButton.clicked.connect(self.out_path)
        self.modtran_toolButton.clicked.connect(self.modtran_path)
        self.BEFORE_pushButton.clicked.connect(self.out_before)
        self.tape5_pushButton.clicked.connect(self.tape5_gen)
        self.modtran_pushButton.clicked.connect(self.modtran_gen)

    def out_before(self):
        out_show.close(), card5_show.show()

    def out_path(self):
        path_tape5 = QFileDialog.getExistingDirectory(self,"选取tape5文件输出路径", "./")
        self.out_lineEdit.setText(path_tape5)

    def modtran_path(self):
        path_modtran = QFileDialog.getExistingDirectory(self, "选取MODTRAN所在路径", "./")
        self.modtran_lineEdit.setText(path_modtran)

    def tape5_gen(self):
        path_tape5 = self.out_lineEdit.text()
        path = os.getcwd()  # 获取当前路径
        tape5_path_before = path + '/tape5.npy'
        tape5 = np.load(tape5_path_before)
        tape5 = list(str(tape5))  # 变列表
        tape5[-2] = '0'
        tape5 = ''.join(tape5)  # 变字符串
        tape5_path_now = path_tape5 + '/tape5'
        with open(tape5_path_now, 'w') as f:
            f.write(tape5)

    def modtran_gen(self):
        path_modtran = self.modtran_lineEdit.text()
        path_tape5 = self.out_lineEdit.text()
        if path_modtran != path_tape5:
            shutil.copy(path_tape5 + '/tape5', path_modtran)
        modtran_exe(path_modtran)

# 定义固定输入字符函数    '%.5f' %
def get_str_btw(s, f):
    par = s.partition(f)
    a = par[0][:]
    b = par[1][:]
    return a + b
#固定输入字符个数
def GDSR(length, input=' '):
    a = len(input)
    if a < length:
        b = ' ' * (length - a)
        return b + input
    else:
        return input
# 无输入与三位浮点数
def IN1(A):
    if A == '':
        return A
    else:
        return '%.3f' % A
# 零位浮点数
def IN2(A):
    if A == '':
        return A
    else:
        return str(A) + '.'
# 无输入与int
def IN3(A):
    if A == '':
        return A
    else:
        return str(A)
# 无输入与五位浮点数
def IN4(A):
    if A == '':
        return A
    else:
        return '%.5f' % A
#必选参数
# CARD1
def CARD1_tog(MODTRAN, SPEED, MODEL, ITYPE, IEMSCT, IMULT, M1, M2, M3, M4, M5, M6, MDEF, IM, NOPRNT, TPTEMP, SURREF):
    MODTRAN = GDSR(1, MODTRAN)
    SPEED = GDSR(1, SPEED)
    MODEL = GDSR(3, str(MODEL))
    ITYPE = GDSR(5, str(ITYPE))
    IEMSCT = GDSR(5, str(IEMSCT))
    IMULT = GDSR(5, str(IMULT))
    M1 = GDSR(5, str(M1))
    M2 = GDSR(5, str(M2))
    M3 = GDSR(5, str(M3))
    M4 = GDSR(5, str(M4))
    M5 = GDSR(5, str(M5))
    M6 = GDSR(5, str(M6))
    MDEF = GDSR(5, str(MDEF))
    IM = GDSR(5, str(IM))
    NOPRNT = GDSR(5, str(NOPRNT))
    TPTEMP = GDSR(8, '%.3f' % TPTEMP)
    SURREF = GDSR(7, str(SURREF))

    return MODTRAN + SPEED + MODEL + ITYPE + IEMSCT + IMULT + M1 + M2 \
           + M3 + M4 + M5 + M6 + MDEF + IM + NOPRNT + TPTEMP + SURREF
# CARD1A
def CARD1A_tog(DIS, DISAZM, NSTR, LSUN, ISUN, CO2MX, H2OSTR, O3STR, LSUNFL, LBMNAM, LFLTNM, H2OAER, SOLCON):
    DIS = GDSR(1, DIS)
    DISAZM = GDSR(1, DISAZM)
    NSTR = GDSR(3, str(NSTR))
    LSUN = GDSR(1, LSUN)
    ISUN = GDSR(4, str(ISUN))
    CO2MX = GDSR(10, '%.5f' % CO2MX)
    H2OSTR = GDSR(10, H2OSTR)
    O3STR = GDSR(10, O3STR)
    LSUNFL = ' ' + GDSR(1, LSUNFL)
    LBMNAM = ' ' + GDSR(1, LBMNAM)
    LFLTNM = ' ' + GDSR(1, LFLTNM)
    H2OAER = ' ' + GDSR(1, H2OAER)
    SOLCON = GDSR(10, IN1(SOLCON))
    return DIS + DISAZM + NSTR + LSUN + ISUN + CO2MX + H2OSTR + \
           O3STR + LSUNFL + LBMNAM + LFLTNM + H2OAER + ' ' * 2 + SOLCON
# CARD2
def CARD2_tog(APLUS, IHAZE, CNOVAM, ISEASN, ARUSS, IVULCN, ICSTL, ICLD, IVSA, VIS, WSS, WHH, RAINRT, GNDALT):
    APLUS = GDSR(2, APLUS)
    IHAZE = GDSR(3, str(IHAZE))
    CNOVAM = GDSR(1, CNOVAM)
    ISEASN = GDSR(4, str(ISEASN))
    ARUSS = GDSR(3, ARUSS)
    IVULCN = GDSR(2, str(IVULCN))
    ICSTL = GDSR(5, str(ICSTL))
    ICLD = GDSR(5, str(ICLD))
    IVSA = GDSR(5, str(IVSA))
    VIS = GDSR(10, '%.5f' % VIS)
    WSS = GDSR(10, '%.5f' % WSS)
    WHH = GDSR(10, '%.5f' % WHH)
    RAINRT = GDSR(10, '%.5f' % RAINRT)
    GNDALT = GDSR(10, '%.5f' % GNDALT)
    return APLUS + IHAZE + CNOVAM + ISEASN + ARUSS + IVULCN + ICSTL \
           + ICLD + IVSA + VIS + WSS + WHH + RAINRT + GNDALT
# CARD3
def CARD3_tog(H1, H2, ANGLE, RANGE, BETA, RO, LENN, PHI):
    H1 = GDSR(10, IN1(H1))
    H2 = GDSR(10, IN1(H2))
    ANGLE = GDSR(10, IN1(ANGLE))
    RANGE = GDSR(10, IN1(RANGE))
    BETA = GDSR(10, IN1(BETA))
    RO = GDSR(10, IN1(RO))
    LENN = GDSR(5, str(LENN))
    PHI = GDSR(10, IN1(PHI))
    return H1 + H2 + ANGLE + RANGE + BETA + RO + LENN + 5 * ' ' + PHI
# ALT CARD3
def ALT_CARD3(H1, H2, ANGLE, IDAY, RO, ISOURC, ANGLEM):
    H1 = GDSR(10, IN1(H1))
    H2 = GDSR(10, IN1(H2))
    ANGLE = GDSR(10, IN1(ANGLE))
    IDAY = GDSR(5, str(IDAY))
    RO = GDSR(10, IN1(RO))
    ISOURC = GDSR(5, str(ISOURC))
    ANGLEM = GDSR(10, IN1(ANGLEM))
    return H1 + H2 + ANGLE + IDAY + ' ' * 5 + RO + ISOURC + ANGLEM
# CARD4
def CARD4_tog(V1, V2, DV, FWHM, YFLAG, XFLAG, DLIMIT, FLAGS):
    V1 = GDSR(10, str(V1))
    V2 = GDSR(10, str(V2))
    DV = GDSR(10, str(DV))
    FWHM = GDSR(10, str(FWHM))
    YFLAG = GDSR(1, YFLAG)
    XFLAG = GDSR(1, XFLAG)
    DLIMIT = GDSR(8, DLIMIT)
    FLAGS = GDSR(7, FLAGS)
    return V1 + V2 + DV + FWHM + YFLAG + XFLAG + DLIMIT + FLAGS
# CARD5
def CARD5_tog(IRPT):
    IRPT = GDSR(5, str(IRPT))
    return IRPT
#可选参数
# CARD 1A1
def CARD1A1_tog(SUNFL2):
    SUNFL2 = GDSR(80, SUNFL2)
    return SUNFL2
# CARD 1A2
def CARD1A2_tog(BMNAME):
    BMNAME = GDSR(80, BMNAME)
    return BMNAME
# CARD 1A3
def CARD1A3_tog(FILTNM):
    FILTNM = GDSR(80, FILTNM)
    return FILTNM
# CAED2A+
def CARD2A_PLUS_tog(ZAER11, ZAER12, SCALE1, ZAER21, ZAER22, SCALE2, ZAER31, ZAER32, SCALE3, ZAER41, ZAER42, SCALE4):
    ZAER11 = GDSR(10, ' ' + IN2(ZAER11))
    ZAER21 = GDSR(10, ' ' + IN2(ZAER21))
    ZAER31 = GDSR(10, ' ' + IN2(ZAER31))
    ZAER41 = GDSR(10, ' ' + IN2(ZAER41))
    ZAER12 = GDSR(10, ' ' + IN2(ZAER12))
    ZAER22 = GDSR(10, ' ' + IN2(ZAER22))
    ZAER32 = GDSR(10, ' ' + IN2(ZAER32))
    ZAER42 = GDSR(10, ' ' + IN2(ZAER42))
    SCALE1 = GDSR(10, ' ' + IN2(SCALE1))
    SCALE2 = GDSR(10, ' ' + IN2(SCALE2))
    SCALE3 = GDSR(10, ' ' + IN2(SCALE3))
    SCALE4 = GDSR(10, ' ' + IN2(SCALE4))
    return ZAER11 + ZAER12 + SCALE1 + ' ' * 20 + ZAER21 + ZAER22 + SCALE2 + ' ' * 20 + ZAER31 + \
           ZAER32 + SCALE3 + ' ' * 20 + ZAER41 + ZAER42 + SCALE4
# CARD2A
def CARD2A_tog(CTHIK, CALT, CEXT):
    CTHIK = GDSR(8, IN1(CTHIK))
    CALT = GDSR(8, IN1(CALT))
    CEXT = GDSR(8, IN1(CEXT))
    return CTHIK + CALT + CEXT
# CARD2A替代格式
def CARD2A_ALT_tog(CTHIK, CALT, CEXT, NCRALT, NCRSPC, CWAVLN, CCOLWD, CCOLIP, CHUMID, ASYMWD, ASYMIP):
    CTHIK = GDSR(8, IN1(CTHIK))
    CALT = GDSR(8, IN1(CALT))
    CEXT = GDSR(8, IN1(CEXT))
    NCRALT = GDSR(4, IN3(NCRALT))
    NCRSPC = GDSR(4, IN3(NCRSPC))
    CWAVLN = GDSR(8, IN1(CWAVLN))
    CCOLWD = GDSR(8, IN1(CCOLWD))
    CCOLIP = GDSR(8, IN1(CCOLIP))
    CHUMID = GDSR(8, IN1(CHUMID))
    ASYMWD = GDSR(8, IN1(ASYMWD))
    ASYMIP = GDSR(8, IN1(ASYMIP))
    return CTHIK + CALT + CEXT + NCRALT + NCRSPC + CWAVLN + CCOLWD + CCOLIP + CHUMID + ASYMWD + ASYMIP
# CARD2B
def CARD2B_tog(ZCVSA, ZTVSA, ZINVSA):
    ZCVSA = GDSR(10, ZCVSA)
    ZTVSA = GDSR(10, ZTVSA)
    ZINVSA = GDSR(10, ZINVSA)
    return ZCVSA + ZTVSA + ZINVSA
# CARD2C
def CARD2C_tog(ML, IRD1, IRD2, HMODEL):
    ML = GDSR(5, IN3(ML))
    IRD1 = GDSR(5, IN3(IRD1))
    IRD2 = GDSR(5, IN3(IRD2))
    HMODEL = GDSR(65, HMODEL)
    return ML + IRD1 + IRD2 + HMODEL
# CARD2C1
def CARD2C1_tog(ZM, P, T, WMOL1, WMOL2, WMOL3, JCHAR, JCHARX):
    ZM = GDSR(10, IN1(ZM))
    P = GDSR(10, IN1(P))
    T = GDSR(10, IN1(T))
    WMOL1 = GDSR(10, IN1(WMOL1))
    WMOL2 = GDSR(10, IN1(WMOL2))
    WMOL3 = GDSR(10, IN1(WMOL3))
    JCHAR = GDSR(14, JCHAR)
    JCHARX = GDSR(1, JCHARX)
    return ZM + P + T + WMOL1 + WMOL2 + WMOL3 + JCHAR + ' ' + JCHARX
# CARD2C2
def CARD2C2_tog(WMOL):
    WMOL = GDSR(10, IN1(WMOL))
    return WMOL
# CARD2C2X
def CARD2C2X_tog(WMOLX):
    WMOLX = GDSR(10, IN1(WMOLX))
    return WMOLX
# CARD2C3
def CARD2C3_tog(AHAZE, EQLWCZ, RRATZ, IHA1, ICLD1, IVUL1, ISEA1, ICHR):
    AHAZE = GDSR(10, IN1(AHAZE))
    EQLWCZ = GDSR(10, IN1(EQLWCZ))
    RRATZ = GDSR(10, IN1(RRATZ))
    IHA1 = GDSR(5, IN3(IHA1))
    ICLD1 = GDSR(5, IN3(ICLD1))
    IVUL1 = GDSR(5, IN3(IVUL1))
    ISEA1 = GDSR(5, IN3(ISEA1))
    ICHR = GDSR(5, IN3(ICHR))
    return ' ' * 10 + AHAZE + EQLWCZ + RRATZ + IHA1 + ICLD1 + IVUL1 + ISEA1 + ICHR
# CARD2D
def CARD2D_tog(IREG1, IREG2, IREG3, IREG4):
    IREG1 = GDSR(5, IN3(IREG1))
    IREG2 = GDSR(5, IN3(IREG2))
    IREG3 = GDSR(5, IN3(IREG3))
    IREG4 = GDSR(5, IN3(IREG4))
    return IREG1 + IREG2 + IREG3 + IREG4
# CARD2D1
def CARD2D1_tog(AWCCON, TITLE):
    AWCCON = GDSR(10, AWCCON)
    TITLE = GDSR(4, TITLE)
    return AWCCON + TITLE * 18
# CARD2D2
def CARD2D2_tog(VARSPC, EXTC, ABSC, ASYM):
    VARSPC = GDSR(6, IN1(VARSPC))
    EXTC = GDSR(5, IN1(EXTC))
    ABSC = GDSR(5, IN1(ABSC))
    ASYM = GDSR(5, IN1(ASYM))
    return VARSPC + EXTC + ABSC + ASYM
# CARD2E1
def CARD2E1_tog(ZCLD, CLD, CLDICE, RR):
    ZCLD = GDSR(10, IN4(ZCLD))
    CLD = GDSR(10, IN4(CLD))
    CLDICE = GDSR(10, IN4(CLDICE))
    RR = GDSR(10, IN4(RR))
    return ZCLD + CLD + CLDICE + RR
# CARD2E2
def CARD2E2_tog(WAVLEN, EXTC, ABSC, ASYM, EXTC2, ABSC2, ASYM2):
    WAVLEN = GDSR(10, IN4(WAVLEN))
    EXTC = GDSR(10, IN4(EXTC))
    ABSC = GDSR(10, IN4(ABSC))
    ASYM = GDSR(10, IN4(ASYM))
    EXTC2 = GDSR(10, IN4(EXTC2))
    ABSC2 = GDSR(10, IN4(ABSC2))
    ASYM2 = GDSR(10, IN4(ASYM2))
    return WAVLEN + EXTC + ABSC + ASYM + EXTC2 + ABSC2 + ASYM2
# CARD3A1
def CARD3A1_tog(IPARM, IPH, IDAY, ISOURC):
    IPARM = GDSR(5, IN3(IPARM))
    IPH = GDSR(5, IN3(IPH))
    IDAY = GDSR(5, IN3(IDAY))
    ISOURC = GDSR(5, IN3(ISOURC))
    return IPARM + IPH + IDAY + ISOURC
# CARD3A2
def CARD3A2_tog(PARM1, PARM2, PARM3, PARM4, TIME, PSIPO, ANGLEM, G):
    PARM1 = GDSR(10, IN1(PARM1))
    PARM2 = GDSR(10, IN1(PARM2))
    PARM3 = GDSR(10, IN1(PARM3))
    PARM4 = GDSR(10, IN1(PARM4))
    TIME = GDSR(10, IN1(TIME))
    PSIPO = GDSR(10, IN1(PSIPO))
    ANGLEM = GDSR(10, IN1(ANGLEM))
    G = GDSR(10, IN1(G))
    return PARM1 + PARM2 + PARM3 + PARM4 + TIME + PSIPO + ANGLEM + G
# CARD3B1
def CARD3B1_tog(NANGLS):
    NANGLS = GDSR(5, IN3(NANGLS))
    return NANGLS
# CARD3B2
def CARD3B2_tog(ANGF, F1, F2, F3, F4):
    ANGF = GDSR(10, IN1(ANGF))
    F1 = GDSR(10, IN1(F1))
    F2 = GDSR(10, IN1(F2))
    F3 = GDSR(10, IN1(F3))
    F4 = GDSR(10, IN1(F4))
    return ANGF + F1 + F2 + F3 + F4
# CARD4A
def CARD4A_tog(NSURF, AATEMP):
    NSURF = GDSR(1, IN3(NSURF))
    AATEMP = GDSR(9, IN2(AATEMP))
    return NSURF + AATEMP
# CARD4B1
def CARD4B1_tog(CBRDFE):
    CBRDFE = GDSR(80, CBRDFE)
    return CBRDFE
# CARD4B2
def CARD4B2_tog(NWVSRF, SURFZN, SURFAZ):

    return NWVSRF + SURFZN + SURFAZ
# CARD4B3
def CARD4B3_tog(WVSURF, PARAMS):

    return WVSURF + PARAMS
# CARD4L1
def CARD4L1_tog(SALBFL):
    SALBFL = GDSR(80, SALBFL)
    return SALBFL
# CARD4L2
def CARD4L2_tog(CSALB):
    CSALB = GDSR(80, CSALB)
    return CSALB
#modtran运行
def modtran_exe(modtran_path):
    #当前程序路径
    pyth = os.getcwd()
    #更改为modtran所在路径
    main = modtran_path +  '\MOD4v1r1.exe'
    os.chdir(modtran_path)
    os.system(main)
    #再次改为原始程序路径
    os.chdir(pyth)

def tiaozhuan():
    start_show.actionCARD1.triggered.connect(
        lambda: {card1_show.show()}
    )
    start_show.actionCARD1A.triggered.connect(
        lambda: {card1a_show.show()}
    )
    start_show.actionCARD2.triggered.connect(
        lambda: {card2_show.show()}
    )
    start_show.actionCARD3.triggered.connect(
        lambda: {card3_show.show()}
    )
    start_show.actionCARD4.triggered.connect(
        lambda: {card4_show.show()}
    )
    start_show.actionCARD5.triggered.connect(
        lambda: {card5_show.show()}
    )
    start_show.actionCARD1Aplus.triggered.connect(
        lambda: {card1_plus_show.show()}
    )
    start_show.actionCARD2A.triggered.connect(
        lambda: {card2a_show.show()}
    )
    start_show.actionCARD2B.triggered.connect(
        lambda: {card2b_show.show()}
    )
    start_show.actionCARD2C.triggered.connect(
        lambda: {card2c_show.show()}
    )
    start_show.actionCARD2D.triggered.connect(
        lambda: {card2d_show.show()}
    )
    start_show.actionCARD2E.triggered.connect(
        lambda: {card2e_show.show()}
    )
    start_show.actionCARD3A.triggered.connect(
        lambda: {card3a_show.show()}
    )
    start_show.actionCARD3B.triggered.connect(
        lambda: {card3b_show.show()}
    )
    start_show.actionCARD4plus.triggered.connect(
        lambda: {card4_plus_show.show()}
    )
    start_show.actionRUN.triggered.connect(
        lambda: {out_show.show()}
    )
    return 0

def geshi_int(a):
    if len(a) == 0:
        return ''
    else:
        return int(a)

def geshi_float(a):
    if len(a) == 0:
        return ''
    else:
        return float(a)

def geshi1(a):
    if a == '':
        a = 0
        return a
    else:
        return a

def geshi2(a):
    if a == '':
        return a
    else:
        return geshi_float(a)

def geshi3(a):
    if a == '':
        return a
    else:
        return geshi_int(a)

def douhao_cut(data):
    data_cut= re.split(',', data)
    return data_cut
def tape5_tog():
    def insure(tape5 , card, tf):
        if tf:
            tape5 = tape5 + card + '\n'
            return tape5
        else:
            return tape5
    path = os.getcwd()  # 获取当前路径
    listDir = os.listdir(path)  # 获取当前目录下的所有内容
    path1 = path + '/tape5.npy'
    # 导入已构建tape5文件
    if 'tape5.npy' in listDir:
        tape5 = str(np.load(path1))
    else:
        tape5 = ''
    print('已创建/导入tape5文件')

    # 构建tape5文件
    card1 = card1_show.card1_gen()
    card1_sure = start_show.actionCARD1.isEnabled()     #卡片是否可用
    tape5 = insure(tape5, card1, card1_sure)    #添加该卡片
    print('已生成card1')

    card1a = card1a_show.card1a_gen()
    card1a_sure = start_show.actionCARD1A.isEnabled()
    tape5 = insure(tape5, card1a, card1a_sure)
    print('已生成card1a')

    card1a1, card1a2, card1a3 = card1_plus_show.card1_plus_gen()
    card1_plus_sure = start_show.actionCARD1Aplus.isEnabled()
    if card1a1 != '':
        tape5 = insure(tape5, card1a1, card1_plus_sure)
    if card1a2 != '':
        tape5 = insure(tape5, card1a2, card1_plus_sure)
    if card1a3 != '':
        tape5 = insure(tape5, card1a3, card1_plus_sure)
    print('已生成card1a+')

    card2 = card2_show.card2_gen()
    card2_sure = start_show.actionCARD2.isEnabled()
    tape5 = insure(tape5, card2, card2_sure)
    print('已生成card2')

    card2a_plus, card2a, card2a_alt = card2a_show.card2a_gen()
    card2a_sure = start_show.actionCARD2A.isEnabled()
    if card2a_plus != '':
        tape5 = insure(tape5, card2a_plus, card2a_sure)
    if card2a != '':
        tape5 = insure(tape5, card2a, card2a_sure)
    if card2a_alt != '':
        tape5 = insure(tape5, card2a_alt, card2a_sure)
    print('已生成card2a')

    card2b = card2b_show.card2b_gen()
    card2b_sure = start_show.actionCARD2B.isEnabled()
    tape5 = insure(tape5, card2b, card2b_sure)
    print('已生成card2b')

    card2c, cards2c = card2c_show.card2c_gen()
    card2c_sure = start_show.actionCARD2C.isEnabled()
    if card2c != '':
        tape5 = insure(tape5,card2c, card2c_sure)
    if cards2c != '':
        tape5 = insure(tape5, cards2c, card2c_sure)
    print('已生成card2c')

    card2d, card2d1, card2d2 = card2d_show.card2d_gen()
    card2d_sure = start_show.actionCARD2D.isEnabled()
    if card2d != '':
        tape5 = insure(tape5, card2d, card2d_sure)
    if card2d1 != '':
        tape5 = insure(tape5, card2d1, card2d_sure)
    if card2d2 != '':
        tape5 = insure(tape5, card2d2, card2d_sure)
    print('已生成card2d')

    card2e1, card2e2 = card2e_show.card2e_gen()
    card2e_sure = start_show.actionCARD2E.isEnabled()
    if card2e1 != '':
        tape5 = insure(tape5, card2e1, card2e_sure)
    if card2e2 != '':
        tape5 = insure(tape5, card2e2, card2e_sure)
    print('已生成card2e')

    card3 = card3_show.card3_gen()
    card3_sure = start_show.actionCARD3.isEnabled()
    tape5 = insure(tape5, card3, card3_sure)
    print('已生成card3')

    card3a1, card3a2 = card3a_show.card3a_gen()
    card3a_sure = start_show.actionCARD3A.isEnabled()
    if card3a1 != '':
        tape5 = insure(tape5, card3a1, card3a_sure)
    if card3a2 != '':
        tape5 = insure(tape5, card3a2, card3a_sure)
    print('已生成card3a')

    card3b1, card3b2 = card3b_show.card3b_gen()
    card3b_sure = start_show.actionCARD3B.isEnabled()
    if card3b1 != '':
        tape5 = insure(tape5, card3b1, card3b_sure)
    if card3b2 != '':
        tape5 = insure(tape5, card3b2, card3b_sure)
    print('已生成card3b')

    card4 = card4_show.card4_gen()
    card4_sure = start_show.actionCARD4.isEnabled()
    tape5 = insure(tape5, card4, card4_sure)
    print('已生成card4')

    card4a, card4b1, card4b2, card4b3, card4l1, card4l2 = card4_plus_show.card4_plus_gen()
    card4_plus_sure = start_show.actionCARD4plus.isEnabled()
    if card4a != '':
        tape5 = insure(tape5, card4a, card4_plus_sure)
    if card4b1 != '':
        tape5 = insure(tape5, card4b1, card4_plus_sure)
    if card4b2 != '':
        tape5 = insure(tape5, card4b2, card4_plus_sure)
    if card4b3 != '':
        tape5 = insure(tape5, card4b3, card4_plus_sure)
    if card4l1 != '':
        tape5 = insure(tape5, card4l1, card4_plus_sure)
    if card4l2 != '':
        tape5 = insure(tape5, card4l2, card4_plus_sure)
    print('已生成card4+')

    card5 = card5_show.card5_gen()
    card5_sure = start_show.actionCARD5.isEnabled()
    tape5 = insure(tape5, card5, card5_sure)
    print('已生成card5')

    np.save(path1, tape5)
    print('已生成tape5文件')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_show =Start()
    card1_show = CARD1()
    card1_plus_show = CARD1_PLUS()
    card1a_show = CARD1A()
    card2_show = CARD2()
    card2a_show = CARD2A()
    card2b_show = CARD2B()
    card2c_show = CARD2C()
    card2d_show = CARD2D()
    card2e_show = CARD2E()
    card3_show = CARD3()
    card3a_show = CARD3A()
    card3b_show = CARD3B()
    card4_show = CARD4()
    card4_plus_show = CARD4_PLUS()
    card5_show = CARD5()
    out_show = OUT()
    tiaozhuan()
    start_show.show()
    sys.exit(app.exec_())
