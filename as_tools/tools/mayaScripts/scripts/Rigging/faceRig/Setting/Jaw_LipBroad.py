import maya.cmds as cmds
M_Lip_Broad = 'M_Lip_Broad'

#选择四个顶点位置,为嘴皮添加四个定位,Right,Left,Low,Up

def lib_broad_con(name, loc):
    notrans = cmds.group(em=True, n=name + '_notransGrp')
    offGrp = cmds.group(em=True, n=name + '_offGrp', p=notrans)
    sdkGrp = cmds.group(em=True, n=name + '_sdkGrp', p=offGrp)
    compGrp = cmds.group(em=True, n=name + '_compGrp', p=sdkGrp)
    cons = cmds.curve(d=1, p=([0, 0, -0.5], [0.5, 0, 0], [0, 0, 0.5], [-0.5, 0, 0], [0, 0, -0.5]), n=name + '_Con')
    cmds.parent(cons, compGrp)
    cmds.matchTransform(notrans, loc)
    return cons

Side_Lip_Broad = 'Upper','Lower','Left','Right'
M_Lip_Broad_Grp = M_Lip_Broad+'_Grp'

if not cmds.objExists(M_Lip_Broad_Grp):
    cmds.group(em=True,n=M_Lip_Broad_Grp)

for lip in Side_Lip_Broad:
    jnt = cmds.joint(n=M_Lip_Broad +'_'+lip +'_Jnt')
    cmds.group(jnt,n=M_Lip_Broad +'_'+lip +'_Grp')


#对组,约束关系,1.上颚对上嘴2.下颚对下嘴----组级
#上下颚组对左右组约束