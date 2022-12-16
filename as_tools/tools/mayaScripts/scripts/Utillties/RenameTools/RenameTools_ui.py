# coding=utf-8
# 2021/12/2
# likangwen
import logging
import maya.cmds as cmds
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from shiboken2 import wrapInstance
from maya import OpenMayaUI as omui

#Get Maya MainWindow
def get_maya_mainWindow():
    prt = omui.MQtUtil.mainWindow()
    return wrapInstance(int(prt), QWidget)

#Undo decorator
def undo( function ):
    def funcCall(*args,**kwargs):

        result = None
        try:
            ## here we open the undo chunk and we give it the name of the fuction
            cmds.undoInfo( openChunk= True)
            result = function( *args,**kwargs )
        except Exception as e:
            pass
            ## If we have an error we will print the stack of the error
            #print traceback.format_exc()
            ## we also make sure the maya ui shows an error.
            #cmds.error( "## Error, see script editor: %s"%e )
        finally:
            ## we always need to close the chunk at the end else we corrupt the stack.
            cmds.undoInfo( closeChunk = True )
        return result
    return funcCall

class Rename_Win(QWidget):
    def __init__(self,name='',parent=get_maya_mainWindow()):
        super(Rename_Win, self).__init__(parent=parent)
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle('Renamer v0.2')
        self.resize(300,300)

        self.name = name

        self.mainlayout = QVBoxLayout()

        self.selHierarchy_layout = QHBoxLayout()
        self.selHierarchy_cb = QCheckBox('Hierarchy')
        self.selHierarchy_multicb = QCheckBox('Multi')
        self.selHierarchy_layout.addWidget(self.selHierarchy_cb)
        self.selHierarchy_layout.addWidget(self.selHierarchy_multicb)
        self.selHierarchy_cb.setChecked(True)
        self.renameNameLayout = QHBoxLayout()
        self.renameName_Line = QLineEdit()
        self.renameName_but = QPushButton('Ren')

        self.renameName_Line.setPlaceholderText(u'Add replace obj name!')
        self.renameName_but.clicked.connect(self.sip_renameName)
        self.renameName_Line.returnPressed.connect(self.sip_renameName)
        self.renameNameLayout.addWidget(self.renameName_Line)
        self.renameNameLayout.addWidget(self.renameName_but)


        self.prefixNameLayout = QHBoxLayout()
        self.prefixName_Line = QLineEdit()
        self.prefixName_but = QPushButton('Add')

        self.prefixName_Line.setPlaceholderText(u'Prefix')
        self.prefixName_but.clicked.connect(self.sip_addPrefix)
        self.prefixName_Line.returnPressed.connect(self.sip_addPrefix)
        self.prefixNameLayout.addWidget(self.prefixName_Line)
        self.prefixNameLayout.addWidget(self.prefixName_but)

        self.suffixNameLayout = QHBoxLayout()
        self.suffixName_Line = QLineEdit()
        self.suffixName_but = QPushButton('Add')

        self.suffixName_Line.setPlaceholderText(u'Suffix')
        self.suffixName_but.clicked.connect(self.sip_addSuffix)
        self.suffixName_Line.returnPressed.connect(self.sip_addSuffix)
        self.suffixNameLayout.addWidget(self.suffixName_Line)
        self.suffixNameLayout.addWidget(self.suffixName_but)

        #Geo/Jnt/Loc/Ctrl/Grp
        suffixOs = 'Geo','Jnt','Loc','Ctrl','Grp'
        self.suffixOSNameLayout = QHBoxLayout()
        for os in suffixOs:
            self.suffixOS_bnt = QPushButton(os)
            self.suffixOS_bnt.setObjectName(os)
            self.suffixOS_bnt.clicked.connect(self.sip_suffixosName)
            self.suffixOSNameLayout.addWidget(self.suffixOS_bnt)

        self.removeNameLayout = QHBoxLayout()
        self.removeName_Line = QLineEdit()
        self.removeName_but = QPushButton('Rom')

        self.removeName_Line.setPlaceholderText(u'Remove')
        self.removeName_but.clicked.connect(self.sip_removeName)
        self.removeName_Line.returnPressed.connect(self.sip_removeName)
        self.removeNameLayout.addWidget(self.removeName_Line)
        self.removeNameLayout.addWidget(self.removeName_but)

        self.replaceNameLayout = QHBoxLayout()
        self.replaceName_Lineer = QLineEdit()
        self.replaceName_Label = QLabel('To')
        self.replaceName_Lineven = QLineEdit()
        self.replaceName_but = QPushButton('Rep')

        self.replaceName_Lineer.setPlaceholderText(u'Replacer')
        self.replaceName_Lineven.setPlaceholderText(u'Replacen')
        self.replaceName_but.clicked.connect(self.sip_replaceName)
        self.replaceName_Lineven.returnPressed.connect(self.sip_replaceName)
        self.replaceNameLayout.addWidget(self.replaceName_Lineer)
        self.replaceNameLayout.addWidget(self.replaceName_Label)
        self.replaceNameLayout.addWidget(self.replaceName_Lineven)
        self.replaceNameLayout.addWidget(self.replaceName_but)

        self.mainlayout.addLayout(self.selHierarchy_layout)
        self.mainlayout.addLayout(self.renameNameLayout)
        self.mainlayout.addLayout(self.prefixNameLayout)
        self.mainlayout.addLayout(self.suffixNameLayout)
        self.mainlayout.addLayout(self.suffixOSNameLayout)
        self.mainlayout.addLayout(self.removeNameLayout)
        self.mainlayout.addLayout(self.replaceNameLayout)
        self.setLayout(self.mainlayout)
    @undo
    def sip_renameName(self):
        self.name = self.renameName_Line.text()

        if self.selHierarchy_cb.isChecked():
            for index, obj in enumerate(self.sip_hierarchy()):
                cmds.rename(obj, self.name + str(index + 1))

        else:
            if self.name:
                select_obj = cmds.ls(sl=True,fl=True)
                for index,obj in enumerate(select_obj):
                    cmds.rename(obj,self.name + str(index + 1))
            else:
                logging.error(u'add replace obj name!')
    @undo
    def sip_addPrefix(self):
        self.name = self.prefixName_Line.text()
        if self.name:
            select_obj = cmds.ls(sl=True,fl=True)
            for obj in select_obj:
                cmds.rename(obj,self.name + obj)
        else:
            logging.error(u'Add obj prefix name!')
    @undo
    def sip_addSuffix(self):
        self.name = self.suffixName_Line.text()
        if self.name:
            select_obj = cmds.ls(sl=True,fl=True)
            for obj in select_obj:
                cmds.rename(obj,obj + self.name)
        else:
            logging.error(u'Add obj suffix name!')
    @undo
    def sip_removeName(self):
        self.name = self.removeName_Line.text()
        if self.name:
            select_obj = cmds.ls(sl=True,fl=True)
            for obj in select_obj:
                if self.name in obj:
                    cmds.rename(obj, obj.replace(self.name, ''))
        else:
            logging.error(u'Add remove name!')
    @undo
    def sip_replaceName(self):
        self.name = self.replaceName_Lineer.text()
        self.namen = self.replaceName_Lineven.text()
        if self.name:
            select_obj = cmds.ls(sl=True,fl=True)
            for obj in select_obj:
                if self.name in obj:
                    cmds.rename(obj, obj.replace(self.name, self.namen))
        else:
            logging.error(u'Add remove name!')
    @undo
    def sip_suffixosName(self):
        select_obj = cmds.ls(sl=True,fl=True)
        for obj in select_obj:
            cmds.rename(obj, obj + '_' + self.sender().objectName())

    def sip_hierarchy(self):
        sel = cmds.ls(sl=True)
        cmds.select(sel[0], hi=True)
        list = cmds.ls(sl=1)
        cmds.select(cl=True)
        return  list

def main():
    global win
    try:
        win.close()
    except:
        pass
    win = Rename_Win()
    win.show()
