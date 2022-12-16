import numpy as np
import maya.cmds as cmds
from decimal import Decimal


# 环形点,获取X&Y轴最大最小值的点
# 环形点生成locator

class liplocation:
    def __init__(self, name):
        # name = 'M_Lip'
        self.name = name

    def get_lip_pos(self, vtx_list):
        # 返回嘴巴环形点的位置信息 , vtx_list是选择点的列表
        pos_list = []
        for vtx in vtx_list:
            pos = cmds.xform(vtx, q=1, ws=1, t=1)
            pos_list.append(pos[0])
        return pos_list

    def broad(self):
        # 嘴型主控定位
        pass

    def annular(self):
        # 环形嘴次级定位
        pass

    def loc_Parent_grp(self, loc, grp):
        if cmds.objExists(grp):
            cmds.parent(loc, grp)

    def lip_grp(self):
        # 创建main,broad,annular组
        try:
            lipGrp = 'main', 'broad', 'annular'
            lipGrpList = []
            for grp in lipGrp:
                if not cmds.objExists(self.name + '_' + grp + '_LocGrp'):
                    em_grp = cmds.group(em=True, n=self.name + '_' + grp + '_LocGrp')
                    lipGrpList.append(em_grp)
            cmds.parent(lipGrpList[1], lipGrpList[2], lipGrpList[0], a=1)
            cmds.select(cl=True)
        except:
            pass


def get_lip_pos(vtx_list):
    # 返回嘴巴环形点的位置信息 , vtx_list是选择点的列表
    pos_list = []
    for vtx in vtx_list:
        pos = cmds.xform(vtx, q=1, ws=1, t=1)
        loc = cmds.spaceLocator(n='_Loc')
        cmds.xform(loc, t=pos)
        pos_list.append(pos[0])
    return pos_list

def follicle_To_Loc(mesh, obj, grp):
    #选择定位器和模型,添加毛囊
    closest = cmds.createNode('closestPointOnMesh', n=obj + '_CPOM')
    # print(closest)
    cmds.connectAttr(mesh + '.outMesh', closest + '.inMesh')
    x = cmds.xform(obj, t=1, q=1)

    cmds.setAttr(closest + '.inPositionX', x[0])
    cmds.setAttr(closest + '.inPositionY', x[1])
    cmds.setAttr(closest + '.inPositionZ', x[2])

    follicle = cmds.createNode('follicle', n=obj + '_Folicle')
    follicleTrans = cmds.listRelatives(follicle, type='transform', p=True)
    if cmds.objExists(grp):
        cmds.parent(follicleTrans, grp)
    else:
        cmds.group(em=True, n=grp)
        cmds.parent(follicleTrans, grp)
    cmds.connectAttr(follicle + '.outRotate', follicleTrans[0] + '.rotate')
    cmds.connectAttr(follicle + '.outTranslate', follicleTrans[0] + '.translate')
    cmds.connectAttr(mesh + '.worldMatrix', follicle + '.inputWorldMatrix')
    cmds.connectAttr(mesh + '.outMesh', follicle + '.inputMesh')

    cmds.setAttr(follicle + '.simulationMethod', 0)
    u = cmds.getAttr(closest + '.result.parameterU')
    v = cmds.getAttr(closest + '.result.parameterV')
    cmds.setAttr(follicle + '.parameterU', u)
    cmds.setAttr(follicle + '.parameterV', v)
    cmds.parentConstraint(follicleTrans[0], obj, mo=True)
    cmds.delete(closest)
    cmds.rename(follicleTrans[0], obj + '_FolicleTrans')
    return follicle

def sip_createControls(obj, grp):
    #创建5级控制器和反向mul
    off_grp = cmds.group(em=True, n=obj + '_offGrp')
    trans_grp = cmds.group(em=True, n=obj + '_transGrp', p=off_grp)
    sdk_grp = cmds.group(em=True, n=obj + '_sdkGrp', p=trans_grp)
    comp_grp = cmds.group(em=True, n=obj + '_compGrp', p=sdk_grp)
    cons = cmds.circle(nr=(0, 1, 0), ch=False, n=obj + '_con')[0]
    cmds.parent(cons, comp_grp)
    cmds.matchTransform(off_grp, obj)

    compMul = cmds.createNode('multiplyDivide', n='compMul')
    cmds.setAttr(compMul + '.input2X', -1)
    cmds.setAttr(compMul + '.input2Y', -1)
    cmds.setAttr(compMul + '.input2Z', -1)

    cmds.connectAttr(cons + '.translate', compMul + '.input1')
    cmds.connectAttr(compMul + '.output', comp_grp + '.translate')
    if cmds.objExists(grp):
        cmds.parent(off_grp, grp)
    else:
        cmds.group(em=True, n=grp)
        cmds.parent(off_grp, grp)
    #follicle_To_Loc(mesh, obj, grp)
    return cons

def set_Color(obj,col):
    #6-blue,9-light red,13-red,14-green,17-yellow
    cmds.setAttr('%s.overrideEnabled' % obj,1)
    cmds.setAttr('%s.overrideColor' % obj, col)

#part = Lip,Eye,Brow,Nose
#M,L,R
#Up,Low

Lip = 'M_Lip'
part = '_Up_', '_Low_','_L_', '_R_'

Lip_Grp = Lip + '_LocGrp'
# 主控制 & 环形控制
lip_broad_grp = Lip + 'broad' + '_LocGrp'
lip_annular_grp = Lip + 'annular' + '_LocGrp'

lip_vtxlist = cmds.ls(sl=True, fl=True)
pos_list = []
for vtx in lip_vtxlist:
    pos = cmds.xform(vtx, q=1, ws=1, t=1)
    loc = cmds.spaceLocator(n='_Loc')
    cmds.xform(loc, t=pos)
    pos_list.append(pos[0])

x_np = np.array(pos_list)
x_min, x_max = min(x_np), max(x_np)

section_vtx = []
for vtx in range(len(lip_vtxlist)):
    pos = cmds.xform(lip_vtxlist[vtx], q=1, ws=1, t=1)
    if x_min == pos[0]:
        section_vtx.append(lip_vtxlist[vtx])
    if x_max == pos[0]:
        section_vtx.append(lip_vtxlist[vtx])
    if Decimal(str(pos_list[vtx])).quantize(Decimal('0.00')) == 0:
        section_vtx.append(lip_vtxlist[vtx])

if not cmds.objExists(Lip_Grp):
    cmds.group(em=True, n=Lip_Grp)

if len(section_vtx) == 4:
    for vtx in range(len(section_vtx)):
        pos = cmds.xform(section_vtx[vtx], q=1, ws=1, t=1)
        loc = cmds.spaceLocator(n=Lip +  part[vtx] + 'Loc')
        cmds.xform(loc, t=pos)
        cmds.parent(loc, Lip_Grp)
        for l in loc:
            if '_L_' in l:
                set_Color(l, 6)
            elif '_R_' in l:
                set_Color(l, 13)
            else:
                set_Color(l, 17)
else:
    print('More that 4 vtx!')
