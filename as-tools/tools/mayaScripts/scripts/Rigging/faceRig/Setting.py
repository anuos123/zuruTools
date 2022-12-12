import maya.cmds as cmds
#Jaw控制,分为上颚和下颚
Jaw = 'Jaw_Low','Jaw_Up'

#Mouth一级控制器
Mouth_Broad_Lip = 'Mouth_Broad_UpLip','Mouth_Broad_LowLip','Mouth_Broad_LeftLip','Mouth_Broad_RightLip'
#Mouth二级控制器
Mouth_Second_Lip = ''
#Mouth三级控制器
Mouth_Three_Lip = ''

############################分界线#######################################
import maya.cmds as cmds

# select loc and mesh
'''
选择点,创建spacelocator
'''


# 1
def create_locToVtx(vtx_list):
    pos_list = []
    loc_list = []
    for index, vtx in enumerate(vtx_list):
        vtx_pos = cmds.xform(vtx, q=1, ws=1, t=1)
        pos_list.append(vtx_pos)
        loc = cmds.spaceLocator(n='loc_' + str(index))
        loc_list.append(loc)
        cmds.xform(loc, t=vtx_pos)
    return loc_list


'''
选择spacelocator,生成最近点folicle
'''


# 2
def follicle_To_Loc(mesh, loc):
    closest = cmds.createNode('closestPointOnMesh', n=loc + '_CPOM')
    # print(closest)
    cmds.connectAttr(mesh + '.outMesh', closest + '.inMesh')
    x = cmds.xform(loc, t=1, q=1)

    cmds.setAttr(closest + '.inPositionX', x[0])
    cmds.setAttr(closest + '.inPositionY', x[1])
    cmds.setAttr(closest + '.inPositionZ', x[2])

    follicle = cmds.createNode('follicle', n=loc + '_Folicle')
    follicleTrans = cmds.listRelatives(follicle, type='transform', p=True)
    cmds.connectAttr(follicle + '.outRotate', follicleTrans[0] + '.rotate')
    cmds.connectAttr(follicle + '.outTranslate', follicleTrans[0] + '.translate')
    cmds.connectAttr(mesh + '.worldMatrix', follicle + '.inputWorldMatrix')
    cmds.connectAttr(mesh + '.outMesh', follicle + '.inputMesh')

    cmds.setAttr(follicle + '.simulationMethod', 0)
    u = cmds.getAttr(closest + '.result.parameterU')
    v = cmds.getAttr(closest + '.result.parameterV')
    cmds.setAttr(follicle + '.parameterU', u)
    cmds.setAttr(follicle + '.parameterV', v)
    cmds.parentConstraint(follicleTrans[0], loc, mo=True)
    cmds.delete(closest)
    cmds.rename(follicleTrans[0], loc + '_FolicleTrans')
    return follicle


def sip_createControls(jnt):
    '''
    创建圆环控制[三级]
    层级关系:
        offGrp---偏移组
        skd---驱动组
        cons---curve圆环曲线
    设置函数
    '''
    notrans = cmds.group(em=True, n=jnt + '_notransGrp')
    offGrp = cmds.group(em=True, n=jnt + '_offGrp', p=notrans)
    sdkGrp = cmds.group(em=True, n=jnt + '_sdkGrp', p=offGrp)
    compGrp = cmds.group(em=True, n=jnt + '_compGrp', p=sdkGrp)
    cons = cmds.circle(nr=(0, 1, 0), ch=False, n=jnt + '_Con')[0]
    cmds.parent(cons, compGrp)
    cmds.matchTransform(notrans, jnt)

    compMul = cmds.createNode('multiplyDivide', n='compMul')
    cmds.setAttr(compMul + '.input2X', -1)
    cmds.setAttr(compMul + '.input2Y', -1)
    cmds.setAttr(compMul + '.input2Z', -1)
    cmds.connectAttr(cons + '.translate', compMul + '.input1')
    cmds.connectAttr(compMul + '.output', compGrp + '.translate')

    return offGrp, sdkGrp, cons


vtx_list = cmds.ls(sl=1, fl=1)
loc_list = create_locToVtx(vtx_list)
mesh = 'Gaga_body3'
for loc in loc_list:
    follicle = follicle_To_Loc(mesh, loc[0])
    cmds.delete(loc)
    follicleTrans = cmds.listRelatives(follicle, type='transform', p=True)
    for fol in follicleTrans:
        jnt = cmds.joint(n=fol + '_Jnt')
        sip_createControls(jnt)


