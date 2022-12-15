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


def getMainWindowPtr():
    prt = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(prt), QWidget)
    return mayaMainWindow

class controls_win(QMainWindow):
    def __init__(self, parent=getMainWindowPtr()):
        super(controls_win, self).__init__(parent=parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Add Controls Tools')
        self.setWindowFlags(Qt.Window)
        self.resize(400, 200)
        MainLayout = QVBoxLayout()

        controls_layout = QHBoxLayout()
        shape_layout = QHBoxLayout()
        color_layout = QHBoxLayout()

        self.AddControls_Bnt = QPushButton(u'Add Controls')
        self.AddControls_China_Bnt = QPushButton(u'Add China Controls')
        self.rep_ctrlshape_Bnt = QPushButton(u'Replace Controls Shapes')
        controls_layout.addWidget(self.AddControls_Bnt)
        controls_layout.addWidget(self.AddControls_China_Bnt)
        shape_layout.addWidget(self.rep_ctrlshape_Bnt)

        colors = 'blue','light_red','red','green','yellow'
        for c in colors:
            boxs = QCheckBox(c)
            color_layout.addWidget(boxs)
            boxs.stateChanged.connect(self.box_connection)

        self.AddControls_Bnt.clicked.connect(self.select_jntCtrl)
        self.AddControls_China_Bnt.clicked.connect(self.china_jntCtrl)
        self.rep_ctrlshape_Bnt.clicked.connect(self.replace_controlShape)

        MainLayout.addLayout(controls_layout)
        MainLayout.addLayout(shape_layout)
        MainLayout.addLayout(color_layout)

        Main_Frame = QWidget()
        self.setCentralWidget(Main_Frame)
        Main_Frame.setLayout(MainLayout)

    def sip_createControls(self,jnt):
        '''
        创建圆环控制[三级]
        层级关系:
            offGrp---偏移组
            skd---驱动组
            cons---curve圆环曲线
        设置函数
        '''
        offGrp = cmds.group(em=True, n=jnt + '_offGrp')
        sdkGrp = cmds.group(em=True, n=jnt + '_sdkGrp', p=offGrp)
        cons = cmds.circle(nr=(0, 1, 0), ch=False, n=jnt + '_Con')[0]
        cmds.parent(cons, sdkGrp)
        cmds.matchTransform(offGrp, jnt)
        cmds.parentConstraint(cons, jnt, mo=True)
        cmds.scaleConstraint(cons, jnt, mo=True)
        return offGrp, sdkGrp, cons

    def select_jntCtrl(self):
        for jnt in cmds.ls(sl=True):
            self.sip_createControls(jnt)

    def china_jntCtrl(self):
        '''
        选择骨骼,增加控制器[三级]
        执行函数
        '''
        cons = []
        sdkGrp = []
        offGrp = []

        jnt_list = cmds.ls(sl=True, type='joint')
        for jnt in range(len(jnt_list) - 1):
            sip = self.sip_createControls(jnt_list[jnt])
            offGrp.append(sip[0])
            sdkGrp.append(sip[1])
            cons.append(sip[2])

        for ctrl, offset in zip(cons, offGrp[1:]):
            cmds.parent(offset, ctrl)

    def curveToJoint(self):
        cvs = cmds.ls('curve1.cv[*]', fl=True)
        jnt_list = []
        for cv in range(len(cvs)):
            if cvs[cv] == 'curve1.cv[1]' or cvs[cv] == 'curve1.cv[1410]':
                pass
            else:
                pos = cmds.xform(cvs[cv], q=True, ws=True, t=True)
                cmds.select(cl=True)
                jnt = cmds.joint(n='China_Jnt_' + str(cv + 1))
                cmds.xform(jnt, t=pos)
                jnt_list.append(jnt)
        for i in range(len(jnt_list) - 1):
            cmds.parent(jnt_list[i + 1], jnt_list[i])

    def replace_controlShape(self):
        '''
        选择变形物体和需要变形物体
        '''
        sel = cmds.ls(sl=True)
        new_ctrl = sel[-1]
        old_ctrls = sel[:-1]

        for old_ctrl in old_ctrls:
            dup = cmds.duplicate(new_ctrl, rc=True)
            cmds.delete(cmds.parentConstraint(old_ctrl, dup))
            cmds.parent(dup, old_ctrl)
            cmds.makeIdentity(dup, apply=True)
            old_shapes = cmds.listRelatives(old_ctrl, type="shape", f=True)
            ctrl_shapes = cmds.listRelatives(dup, type="shape", f=True)
            color = cmds.getAttr(old_shapes[0] + ".overrideColor")

            for ctrl_shape in ctrl_shapes:
                cmds.setAttr(ctrl_shape + ".overrideEnabled", 1)
                cmds.setAttr(ctrl_shape + ".overrideColor", color)
                ren = cmds.rename(ctrl_shape, old_ctrl + "Shape#")
                cmds.parent(ren, old_ctrl, relative=True, shape=True)

            cmds.delete(dup)
            cmds.delete(old_shapes)

        cmds.select(clear=True)
    def box_connection(self):
        if self.sender().text()=='blue':
            self.change_color(6)
        elif self.sender().text() == 'light_red':
            self.change_color(9)
        elif self.sender().text() == 'red':
            self.change_color(13)
        elif self.sender().text() == 'green':
            self.change_color(14)
        elif self.sender().text() == 'yellow':
            self.change_color(17)
    def change_color(self,color):
        list = cmds.ls(sl=True)
        list_shape = cmds.listRelatives(list,s=True)
        for shape in list_shape:
            cmds.setAttr(shape + ".overrideEnabled", 1)
            cmds.setAttr(shape + ".overrideColor", color)
def main():
    global win
    try:
        win.close()
    except:
        pass
    win = controls_win()
    win.show()