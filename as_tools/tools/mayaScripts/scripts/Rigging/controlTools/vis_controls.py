# coding=utf8
import maya.cmds as cmds

vis = 'Visibility'
cmds.setAttr('{}.displayType'.format(vis),0)

def add_Atribute(controls, name):
    cmds.addAttr(controls, ln='%s_Vis' % name, at='bool', k=True)

def set_hiddenControls(listVis,ctrl,attr):
    for vis in listVis:
        cmds.connectAttr(ctrl + '.%s'%attr, vis + '.v', f=True)

def set_model_vis(vis):
    cmds.setAttr('{}.displayType'.format(vis), 0)
    list = cmds.ls(sl=True)
    shape_list = cmds.listRelatives(list, s=True)
    for shape in shape_list:
        cmds.setAttr("{}.overrideEnabled".format(shape), 1)
        cmds.connectAttr('{}.displayType'.format(vis), '{}.overrideDisplayType'.format(shape), f=True)

# faceVis = 'head_vis', 'body_vis', 'clothVis','hairVis'
# list = cmds.ls(sl=1)
# set_hiddenControls(list,vis,'clothVis')
set_model_vis(vis)