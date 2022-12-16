#!/usr/bin/env python
# visit https://tool.lu/pyc/ for more information
# Version: Python 2.7

import maya.cmds as cmds
import maya.OpenMaya as om
import maya.mel as mel

selectionDIC = {}
selectionCcDIC = {}
jointInfluenceDic = {}


class SoftJoint:

    def __init__(self):
        if cmds.window('Soft_Window', exists=True):
            cmds.deleteUI('Soft_Window', window=True)
        color = (0.23, 0.23, 0.23)
        pathIcons = cmds.internalVar(userPrefDir=True) + 'icons'
        Soft_Win = cmds.window('Soft_Window', title='Soft_Window UI', w=150, h=40)
        Layout = cmds.columnLayout(width=245, adjustableColumn=False)
        image = cmds.image(image=pathIcons + '/Softimage.png')
        if not image:
            pass
        cmds.separator(h=5, style='none')
        self.control = cmds.text('Need a Controller for your Soft joint ?')
        self.queyControl = cmds.checkBox('Controller', h=35, v=False, w=95)
        cmds.separator(h=5, style='singleDash')
        self.rowColumnLayout = cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
            (1, 100),
            (2, 5),
            (3, 130)], columnOffset=[
            (1, 'right', 3),
            (2, 'right', 3),
            (3, 'right', 4)])
        self.but00 = cmds.button(l='Root joint >>>', h=35, w=100, command=self.AP_root_joint,
                                 parent=self.rowColumnLayout, bgc=color)
        cmds.separator(h=10, style='none')
        self.textbut01 = cmds.text(l='**Waiting for joint root**', height=35, width=130, parent=self.rowColumnLayout,
                                   bgc=(0.15, 0.15, 0.15))
        cmds.separator(h=5, style='none')
        cmds.separator(h=5, style='none')
        cmds.separator(h=5, style='none')
        self.but001 = cmds.button(l='Root Ctrl >>>', h=35, w=100, command=self.AP_root_CC, parent=self.rowColumnLayout,
                                  bgc=color)
        cmds.separator(h=10, style='none')
        self.textbut02 = cmds.text(l='**Waiting for Ctrl root**', height=35, width=130, parent=self.rowColumnLayout,
                                   bgc=(0.15, 0.15, 0.15))
        Layout2 = cmds.columnLayout(width=245, adjustableColumn=False)
        cmds.separator(h=10, style='none')
        self.but02 = cmds.button(l='Apply', h=35, w=245, command=self.AP_build, parent=Layout2, bgc=color)
        cmds.separator(h=5, style='none')
        self.but02 = cmds.button(l='Parent on Root Ctrl', h=35, w=245, command=self.AP_parent_joint, parent=Layout2,
                                 bgc=color)
        cmds.separator(h=5, style='none')
        cmds.separator(h=5, style='none')
        self.frameLayout = cmds.frameLayout('Influence apply', width=245)
        cmds.separator(h=5, style='none')
        self.rowColumnLayout2 = cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
            (1, 100),
            (2, 5),
            (3, 130)], columnOffset=[
            (1, 'right', 3),
            (2, 'right', 3),
            (3, 'right', 4)])
        self.but03 = cmds.button(l='Target Joint >>>', h=35, w=100, command=self.AP_jointW,
                                 parent=self.rowColumnLayout2, bgc=color)
        cmds.separator(h=5, style='none')
        self.but04 = cmds.text(l='**Wainting for target**', height=35, width=130, parent=self.rowColumnLayout2,
                               bgc=(0.15, 0.15, 0.15))
        cmds.separator(h=10, style='none')
        cmds.separator(h=10, style='none')
        cmds.separator(h=10, style='none')
        self.but03 = cmds.button(l='Apply weight', h=35, w=245, command=self.AP_Paint_jointW,
                                 parent=self.rowColumnLayout2, bgc=color)
        cmds.separator(h=5, style='none')
        cmds.showWindow(Soft_Win)

    def AP_root_joint(self, pressed):
        global selectionDIC
        self.rootSelect = cmds.ls(selection=True, type='joint')
        if not self.rootSelect:
            cmds.warning('Select a joint type to root')
        else:
            selectionDIC = self.rootSelect[0]
            print(selectionDIC)
            cmds.text(self.textbut01, label=selectionDIC, edit=True)
            print('Your joint will be connected to the hierarchy of ' + selectionDIC)

    def AP_root_CC(self, pressed):
        global selectionCcDIC
        self.rootCCSelect = cmds.ls(selection=True, type='nurbsCurve', dag=True)
        if not self.rootCCSelect:
            cmds.warning('Select a curve type to root')
        else:
            selectionCcDIC = self.rootCCSelect[0]
            cmds.text(self.textbut02, label=selectionCcDIC, edit=True)
            print('Your controller will be moved to the hierarchy of ' + selectionCcDIC)

    def AP_build(self, pressed):
        VtxSel = cmds.ls(sl=True, fl=True)
        if not VtxSel:
            cmds.warning('******Vertex not selected******')
        else:
            SelectionPath = VtxSel[0]
            just_the_selected_verts = cmds.filterExpand(sm=31)
            if not just_the_selected_verts:
                cmds.warning('******Select a vertex******')
            elif not cmds.softSelect(q=1, sse=True):
                cmds.warning('******Use soft selection method******')
            else:
                selectionTransform = SelectionPath.split('.')
                selShape = cmds.listRelatives(selectionTransform[0], s=1)
                #SkinSet = cmds.listSets(o=VtxSel[0], type=2)[0]
                SkinSet = cmds.sets(name="clus")
                if not SkinSet:
                    cmds.warning('******SkinSet does not exist******')
                else:
                    SkinNode = mel.eval('findRelatedSkinCluster ' + selectionTransform[0])
                    print('esse eh o meu cluster' + SkinNode)
                    if not SkinNode:
                        cmds.warning('******SkinCluster does not exist******')
                    else:
                        selType = SelectionPath.split('.')[-1].split('[')[0]
                        richSel = om.MRichSelection()
                        om.MGlobal.getRichSelection(richSel)
                        richSelList = om.MSelectionList()
                        richSel.getSelection(richSelList)
                        path = om.MDagPath()
                        component = om.MObject()
                        richSelList.getDagPath(0, path, component)
                        componentFn = om.MFnSingleIndexedComponent(component)
                        ConvertToUV = cmds.polyListComponentConversion(SelectionPath, fv=True, tuv=True)
                        getUVvalue = cmds.polyEditUV(ConvertToUV, query=True)
                        self.joints = cmds.joint(SelectionPath, radius=1, name='Jnt_soft_' + VtxSel[0])
                        Constraint = cmds.pointOnPolyConstraint(SelectionPath, self.joints, mo=0, offset=(0, 0, 0))
                        cmds.setAttr(Constraint[0] + '.' + selectionTransform[0] + 'U0', getUVvalue[0])
                        cmds.setAttr(Constraint[0] + '.' + selectionTransform[0] + 'V0', getUVvalue[1])
                        cmds.parent(self.joints, w=True)
                        cmds.delete(Constraint[0])
                        selecao01 = VtxSel[0]
                        VtxSelsFi = cmds.ls(selecao01)
                        if cmds.checkBox(self.queyControl, query=True, value=True):
                            for each in VtxSelsFi:
                                myPos = cmds.xform(each, q=True, ws=True, t=True)
                                CCtransform = cmds.circle(ch=1, o=1, r=0.6, nr=(0, 0, 1))
                                CCShape1 = cmds.circle(ch=1, o=1, r=0.6, nr=(0, 1, 0))
                                CCShape2 = cmds.circle(ch=1, o=1, r=0.6, nr=(1, 0, 0))
                                CCShapeSelect = cmds.listRelatives(CCShape1, CCShape2)
                                cmds.parent(CCShapeSelect, CCtransform[0], relative=True, shape=True)
                                cmds.select(clear=True)
                                cmds.move(myPos[0], myPos[1], myPos[2], CCtransform)
                                cmds.makeIdentity(CCtransform, apply=True, t=1, r=1, s=1, n=0)
                                cmds.parentConstraint(CCtransform, self.joints, mo=True)
                                cmds.scaleConstraint(CCtransform, self.joints, mo=True)
                                self.grpCC = cmds.group(CCtransform, name='Grp_soft_' + CCtransform[0])
                                toBind = [
                                    self.joints,
                                    selectionTransform]
                                cmds.select(selectionTransform[0])
                                cmds.skinCluster(selectionTransform[0], edit=True, addInfluence=self.joints, weight=0)
                                cmds.select(SelectionPath, r=True)
                                for i in range(0, componentFn.elementCount()):
                                    weight = componentFn.weight(i)
                                    v = componentFn.element(i)
                                    w = weight.influence()
                                    vtx = (selectionTransform[0] + '.%s[%d]') % (selType, v)
                                    cmds.sets(vtx, add=SkinSet)
                                    cmds.skinPercent(SkinNode, vtx, transformValue=(self.joints, w))

                                cmds.select(clear=True)

                        if not cmds.checkBox(self.queyControl, query=True, value=True):
                            for each in VtxSelsFi:
                                toBind = [
                                    self.joints,
                                    selectionTransform]
                                cmds.select(selectionTransform[0])
                                cmds.skinCluster(selectionTransform[0], edit=True, addInfluence=self.joints, weight=0)
                                cmds.select(SelectionPath, r=True)
                                for i in range(0, componentFn.elementCount()):
                                    weight = componentFn.weight(i)
                                    v = componentFn.element(i)
                                    w = weight.influence()
                                    vtx = (selectionTransform[0] + '.%s[%d]') % (selType, v)
                                    cmds.sets(vtx, add=SkinSet)
                                    cmds.skinPercent(SkinNode, vtx, transformValue=(self.joints, w))

                                cmds.select(clear=True)

    def AP_parent_joint(self, pressed):
        if not selectionDIC and selectionCcDIC:
            cmds.warning('******Root not selected******')

        try:
            cmds.parent(self.joints, selectionDIC)
            cmds.parent(self.grpCC, selectionCcDIC)
        except:
            print('Controll root is not defined')

        print('Parent OK')

    def AP_jointW(self, pressed):
        global jointInfluenceDic
        self.jointInflu = cmds.ls(selection=True, type='joint')
        if not self.jointInflu:
            cmds.warning('******Select the joint that received the influence******')
        else:
            jointInfluenceDic = self.jointInflu[0]
            cmds.text(self.but04, label=jointInfluenceDic, edit=True)
            print('which received the influence is' + jointInfluenceDic)

    def AP_Paint_jointW(self, pressed):
        VtxSel = cmds.ls(sl=True, fl=True)
        if not VtxSel:
            cmds.warning('******Vertex not selected******')
        else:
            SelectionPath = VtxSel[0]
            just_the_selected_verts = cmds.filterExpand(sm=31)
            if not just_the_selected_verts:
                cmds.warning('******Select a vertex******')
            elif not cmds.softSelect(q=1, sse=True):
                cmds.warning('******Use soft selection method******')
            else:
                selectionTransform = SelectionPath.split('.')
                selShape = cmds.listRelatives(selectionTransform[0], s=1)
                SkinSet = cmds.listSets(o=VtxSel[0], type=2)[0]
                if not SkinSet:
                    cmds.warning('******SkinSet does not exist******')
                else:
                    SkinNode = mel.eval('findRelatedSkinCluster ' + selectionTransform[0])
                    print('esse eh o meu cluster' + SkinNode)
                    if not SkinNode:
                        cmds.warning('******SkinCluster does not exist******')
                    elif not self.jointInflu:
                        cmds.window('******The joint that received the influence does not exist')
                    else:
                        selType = SelectionPath.split('.')[-1].split('[')[0]
                        richSel = om.MRichSelection()
                        om.MGlobal.getRichSelection(richSel)
                        richSelList = om.MSelectionList()
                        richSel.getSelection(richSelList)
                        path = om.MDagPath()
                        component = om.MObject()
                        richSelList.getDagPath(0, path, component)
                        componentFn = om.MFnSingleIndexedComponent(component)
                        cmds.select(SelectionPath, r=True)
                        for i in range(0, componentFn.elementCount()):
                            weight = componentFn.weight(i)
                            v = componentFn.element(i)
                            w = weight.influence()
                            vtx = (selectionTransform[0] + '.%s[%d]') % (selType, v)
                            cmds.sets(vtx, add=SkinSet)
                            cmds.skinPercent(SkinNode, vtx, transformValue=(jointInfluenceDic, w))

                        cmds.select(clear=True)


if __name__ == '__main__':
    JNT = SoftJoint()