# coding=utf8
#author : likangwen
#time :2021/08/20
import logging
import os
import sys
import maya.cmds as cmds
from PySide2.QtWidgets import QApplication, QWidget,QMainWindow,QCheckBox
from PySide2.QtCore import *
from PySide2.QtUiTools import QUiLoader
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

version = 0.01

def getMainWindowPtr():
    prt = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(prt), QWidget)
    return mayaMainWindow

class BPC_Window(QMainWindow):
    def __init__(self,parent=getMainWindowPtr()):
        super(BPC_Window, self).__init__(parent=parent)
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle(u'约束工具' + ' v' + str(version))
        self.resize(800,600)
        self.load_ui()

        self.list1 = self._ui.pushButton_list1
        self.list2 = self._ui.pushButton_list2
        self.only_rbt = self._ui.only_rbt
        self.multi_rbt = self._ui.multi_rbt
        self.bpc_bnt = self._ui.pushButton_parentContraint
        self.bp_widget = self._ui.Constraint_widget
        self.reset_bnt = self._ui.reset_pushButton
        self.prc = self._ui.CB_parentConstraint
        self.poc = self._ui.CB_pointConstraint
        self.orc = self._ui.CB_orientConstraint
        self.scc = self._ui.CB_scaleConstraint
        self.amc = self._ui.CB_AimConstraint

        self.listW1 = self._ui.listWidget_list1
        self.listW2 = self._ui.listWidget_list2

        self.list1.setText(u"列表1")
        self.list2.setText(u"列表2")
        self.only_rbt.setText(u"单>>多")
        self.multi_rbt.setText(u"多>>多")
        self.bpc_bnt.setText(u"执行")

        self.list1.clicked.connect(self.list1_select)
        self.list2.clicked.connect(self.list2_select)

        self.multi_rbt.setChecked(True)
        self.prc.setChecked(True)
        self.scc.setChecked(True)

        self.reset_bnt.clicked.connect(self.reset_constraint)
        self.bpc_bnt.clicked.connect(self.bat_parentContraint)

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.abspath(os.path.dirname(__file__)+"/BPContraintTools.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self._ui = loader.load(ui_file, self)
        ui_file.close()

    def list1_select(self):
        self.listW1.clear()
        list1 = cmds.ls(sl=1)
        if self.only_rbt.isChecked()==False:
            self.listW1.addItems(list1)
        else:
            if len(list1)==1:
                self.listW1.addItem(list1[0])
            else:
                logging.error('Place Select One Object!')

    def list2_select(self):
        self.listW2.clear()
        list2 = cmds.ls(sl=1)
        self.listW2.addItems(list2)

    def bat_parentContraint(self):
        constraint = [x.text() for x in self.bp_widget.findChildren(QCheckBox) if x.isChecked()]
        list1_counts = self.listW1.count()
        list2_counts = self.listW2.count()
        main_obj = []
        next_obj = []
        if not list1_counts:
            logging.error(u'列表1没有内容')
        else:
            for count in range(list1_counts):
                main_obj.append(self.listW1.item(count).text())
        if not list1_counts:
            logging.error(u'列表2没有内容')
        else:
            for count in range(list2_counts):
                next_obj.append(self.listW2.item(count).text())

        if self.multi_rbt.isChecked():
            if len(constraint) == 1:
                for obj in range(len(main_obj)):
                    self.only_p_multi(main_obj[obj], next_obj[obj], constraint[0])
            else:
                for obj in range(len(main_obj)):
                    self.only_p_multi(main_obj[obj], next_obj[obj], constraint[0], constraint[1])
        else:
            if len(constraint)==1:
                for obj in next_obj:
                    self.only_p_multi(main_obj, obj, constraint[0])
            else:
                for obj in next_obj:
                    self.only_p_multi(main_obj, obj, constraint[0],constraint[1])

    def reset_constraint(self):
        self.prc.setChecked(False)
        self.poc.setChecked(False)
        self.orc.setChecked(False)
        self.scc.setChecked(False)
        self.amc.setChecked(False)

    def only_p_multi(self,main_obj, next_obj, *args):
        if len(args) == 1:
            if args[0] == 'parentConstraint':
                cmds.parentConstraint(main_obj, next_obj, mo=True)
            elif args[0] == 'pointConstraint':
                cmds.pointConstraint(main_obj, next_obj, mo=True)
            elif args[0] == 'orientConstraint':
                cmds.orientConstraint(main_obj, next_obj, mo=True)
            elif args[0] == 'scaleConstraint':
                cmds.scaleConstraint(main_obj, next_obj, mo=True)
            elif args[0] == 'AimConstraint':
                cmds.AimConstraint(main_obj, next_obj, mo=True)
        else:
            cmds.parentConstraint(main_obj, next_obj, mo=True)
            cmds.scaleConstraint(main_obj, next_obj, mo=True)


def show():
    global win
    try:
        win.close()
    except:
        pass
    win = BPC_Window()
    win.show()
