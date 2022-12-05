# -*- coding:utf-8 -*-
import pymel.core as pm
import maya.cmds as cmds
try:
    from lib import reload
except:
    from importlib import reload

as_tools = 'as_tools'


def menuIt(label, func):
    pm.menuItem(label=label, command=func)

def show():
    cmds.currentUnit(time="ntsc")
    if pm.menu(as_tools, exists=True):
        pm.deleteUI(as_tools)
    nztf = pm.menu(as_tools, p="MayaWindow", to=True, aob=True, l=u"Zuru Tools")

    pm.menuItem(p=nztf, l=u"Reload Menu",c="import Menu;""reload(Menu);""Menu.show()")
    pm.setParent(nztf, menu=True)
    pm.menuItem(divider=True)

    # Modelus
    Mods = 'Tools', 'Modeling', 'Rigging', 'Animation', 'Utillties', 'Help'
    for m in Mods:
        pm.menuItem(p=as_tools, sm=True, to=True, l=m)
        if m == 'Tools':
            pm.menuItem(l=u"BCContraint Tools >> 约束工具", c='import BPContraintTools.BPContraintToolsUI as BPC_UI;'
                                                          'reload(BPC_UI);'
                                                          'BPC_UI.show();')
        elif m == 'Modeling':
            pass
        elif m == 'Rigging':
            pass
        elif m == 'Animation':
            pass
        elif m == 'Utillties':
            pm.menuItem(l=u"ReNameTools >> 重命名工具", c='from RenameTools import RenameTools_ui;reload(RenameTools_ui);RenameTools_ui.main()')
        else:
            pm.menuItem(l=u"About >> 工具使用手册", c="Test()")