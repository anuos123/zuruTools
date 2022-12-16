#coding=utf-8
import maya.cmds as cmds


def clear_ngskinNode():
    #清理ngskin节点
    ng_node = cmds.ls(type='ngst2SkinLayerData')
    cmds.delete(ng_node)