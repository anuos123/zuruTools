# coding=utf8
import maya.cmds as cmds
import logging
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
try:
    import imp
except:
    import importlib as imp

##Test Func
import numpy as np
from decimal import Decimal


def getMainWindowPtr():
    prt = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(prt), QWidget)
    return mayaMainWindow

class FaceRigUI(QWidget):
    def __init__(self, parent=getMainWindowPtr()):
        super(FaceRigUI, self).__init__(parent=parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('FaceRig')
        self.setWindowFlags(Qt.Window)
        self.resize(600, 400)
        main_ly = QVBoxLayout()
        test_ly = QHBoxLayout()
        self.but = QPushButton('test_but')
        self.rbut = QPushButton('reb_but')
        self.but.clicked.connect(self.test_bnt)
        self.rbut.clicked.connect(self.rebuild_ui)
        test_ly.addWidget(self.but)
        test_ly.addWidget(self.rbut)
        main_ly.addLayout(test_ly)
        self.setLayout(main_ly)

    def test_bnt(self):
        print('cc')

    def rebuild_ui(self):
        print('None')


def main():
    global ui
    try:
        ui.close()
    except:
        pass
    ui = FaceRigUI()
    ui.show()
