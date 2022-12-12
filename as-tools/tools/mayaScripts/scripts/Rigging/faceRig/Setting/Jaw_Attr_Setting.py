import maya.cmds as cmds
#Jaw 控制器属性
#1.LibSeal拉链嘴(float 范围0 ~ 10，默认0)
#2.LibSealDelay拉链嘴延迟(float 范围0 ~ 10，默认3)
#3.Auto_Corner_Pin,中心嘴角开关
#4.Input_Ty嘴角上抬(float 范围-10 ~ 10，默认-10)
#5.Jaw_Follow下巴扩张(Ty float 范围-10 ~ 10，默认0.32，Tz float 范围-10 ~ 10，默认0.15)
LibSeal = 'L_LipSeal','R_LipSeal'
LibSealDelay = 'L_LipSeal_Delay','R_LipSeal_Delay'
Auto_Corner_Pin = 'L_Auto_Corner_Pin','R_Auto_Corner_Pin'
Input_Ty = 'L_Input_Ty','R_Input_Ty'
Jaw_Follow = 'Jaw_Ty_Follow','Jaw_Tz_Follow'

def add_float_attr(obj,ln,min,max,dv):
    '''
    单一物体,单一属性[Float]
    obj=物体名称,ln=添加属性名称,min=最小值,max=最大值,dv=初始默认值
    '''
    cmds.addAttr(obj,ln=ln,at='double',min=min,max=max,dv=dv,k=True)

def add_multiObj_float_attr(objlist,ln,min,max,dv):
    '''
    多个物体,单一属性[Float]
    objlist=物体列表,ln=添加属性名称,min=最小值,max=最大值,dv=初始默认值
    '''
    for obj in objlist:
        cmds.addAttr(obj, ln=ln, at='double', min=min, max=max, dv=dv, k=True)

def add_multiLn_float_attr(obj,listln,min,max,dv):
    '''
    单一物体,多个属性[Float]
    objlist=物体列表,ln=添加属性名称,min=最小值,max=最大值,dv=初始默认值
    '''
    for ln in listln:
        cmds.addAttr(obj, ln=ln, at='double', min=min, max=max, dv=dv, k=True)


def add_multiObjLn_float_attr(objlist,lnlist,min,max,dv):
    '''
    多个物体,多个属性,[Float]
    objlist=物体列表,lnlist=添加列表,min=最小值,max=最大值,dv=初始默认值
    '''
    for obj in objlist:
        for ln in lnlist:
            cmds.addAttr(obj, ln=ln, at='double', min=min, max=max, dv=dv, k=True)

def add_bool_attr(obj,ln):
    '''
    单一物体,单一属性
    obj=物体名称,ln=添加属性名称
    '''
    cmds.addAttr(obj,ln=ln,at='bool',k=True)

def add_multiObj_bool_attr(objlist,ln):
    '''
    多个物体,单一属性
    obj=物体名称,ln=添加属性名称
    '''
    for obj in objlist:
        cmds.addAttr(obj,ln=ln,at='bool',k=True)
def add_multiLn_bool_attr(obj,lnlist):
    '''
    单个物体,多个属性
    obj=物体名称,ln=添加属性名称
    '''
    for ln in lnlist:
        cmds.addAttr(obj,ln=ln,at='bool',k=True)

def add_multiObjLn_bool_attr(objlist,lnlist):
    '''
    多个物体,多个属性,[Bool]
    obj=物体名称,ln=添加属性名称
    '''
    for obj in objlist:
        for ln in lnlist:
            cmds.addAttr(obj,ln=ln,at='bool',k=True)


grp = 'Jaw_Attr_Grp'
if not cmds.objExists(grp):
    cmds.group(em=True, n=grp)

objlist = 'C_jaw_Ctrl', grp
add_multiObjLn_float_attr(objlist, LibSeal, 0, 10, 0)
add_multiObjLn_float_attr(objlist, LibSealDelay, 0, 10, 3)
add_multiObjLn_float_attr(objlist, Input_Ty, -10, 10, -10)
add_multiLn_bool_attr(objlist,Auto_Corner_Pin)
add_multiObjLn_float_attr(objlist, Jaw_Follow, -10, 10, 0.32)

def connect_Jaw_attr(A,A_Attr,B,B_Attr):
    cmds.connectAttr('%s.%s'%(A,A_Attr),'%s.%s'%(B,B_Attr),f=True)