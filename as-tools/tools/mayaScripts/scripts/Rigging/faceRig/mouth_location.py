import numpy as np
import logging
import maya.cmds as cmds
from decimal import Decimal

#object instance
JAW = 'Jaw'
GRP = 'Grp'
JNT = 'Jnt'
LOCATION = 'Location'

#side instance
LT = 'L'
RT = 'R'
CENTER = 'M'
MAIN = 'Main'

#up,low,left,right instance
UP = 'Up'
LOW = 'Low'
LEFT = 'Lt'
RIGHT = 'Rt'

def create_guide():
    '''
    创建定位器main和seed组
    '''
    jaw_main_grp = '{}_{}_{}_{}'.format(JAW,MAIN,LOCATION,GRP)
    if not cmds.objExists(jaw_main_grp):
        jaw_main_grp = cmds.group(em=True,n=jaw_main_grp)
        for SIDE in get_ullr_side():
            cmds.group(em=True,n='{}_{}_{}_{}'.format(JAW,SIDE,LOCATION,GRP),p=jaw_main_grp)
    return jaw_main_grp

def get_vtxs():
    '''
    返回选择的点列表
    '''
    vtxs = cmds.ls(sl=True, fl=True)
    if 'vtx' not in vtxs[0]:
        logging.error('place select vtx list!')
    return vtxs


def get_vtxs_posx(vtxs):
    vtxs_pos = []
    for vtx in vtxs:
        pos = cmds.xform(vtx, q=True, ws=True, t=True)
        vtxs_pos.append(pos[0])
    return vtxs_pos

def set_Color(obj,col):
    '''#6=蓝色,9=浅红色,13=红色,14=绿色,17=黄色
    obj:物体sting
    col:颜色:int
    '''
    cmds.setAttr('%sShape.overrideEnabled' % obj,1)
    cmds.setAttr('%sShape.overrideColor' % obj, col)

def get_posx_vtx(vtxs,value):
    '''
    value
    left_vtxs
    '''
    for vtx in vtxs:
        pos = cmds.xform(vtx, q=True, ws=True, t=True)
        if value == pos[0]:
            return pos[1]
def set_loc_scale(loc,rid):
    '''
    loc:定位器Sting
    rid:缩放值Float
    '''
    cmds.setAttr(loc + "Shape.localScaleX", rid)
    cmds.setAttr(loc + "Shape.localScaleY", rid)
    cmds.setAttr(loc + "Shape.localScaleZ", rid)

def create_locator(vtxs,prefix,side,suffix,rid,col):
    loc_list = []
    if not cmds.objExists(prefix + '_Grp'):
        cmds.group(em=True,n=prefix + '_Grp')

    #create_guide()

    for vtx in range(len(vtxs)):
        pos = cmds.xform(vtxs[vtx], q=1, ws=1, t=1)
        loc = cmds.spaceLocator(n=prefix + '_' + side + '_' + suffix + str(vtx + 1))
        set_loc_scale(loc[0],rid)
        set_Color(loc[0], col)
        cmds.xform(loc, t=pos)
        cmds.parent(loc,prefix + '_Grp')
        loc_list.append(loc)
    cmds.select(cl=True)
    return loc_list


def get_maxmin_value(pos):
    """
    pos：
        位置数值列表
    Returns:
        #返回最大最小
        max_value,min_value
    """
    np_pos = np.array(pos)
    max_value = max(np_pos)
    min_value = min(np_pos)
    return max_value, min_value

def get_ullr_side():
    '''
    Returns：
        返回上左,上右，下左，下右分块
    '''
    side_list = []
    for ul in [UP,LOW]:
        for lr in [LEFT,RIGHT]:
            side_list.append('{}{}'.format(ul,lr))
    return side_list

def get_broad_side():
    '''
    Returns：
        返回Broad上,下,左,右 分块
    '''
    broad = 'Broad'
    side_list = []
    sides = 'Up', 'Low','Left', 'Right'
    for side in sides:
        s = broad + '_' + side
        side_list.append(s)
    return side_list

broad_list = []
location_list = []

# 获取选择的点位置信息,转义和区分最大最小值
jaw_vtx = get_vtxs()
vtxs_pos = get_vtxs_posx(jaw_vtx)
x_np = np.array(vtxs_pos)
x_min, x_max = min(x_np), max(x_np)

# 区分左右和中心点列表
left_vtxs = []
right_vtxs = []
mid_vtxs = []
for vtx in jaw_vtx:
    pos = cmds.xform(vtx, q=True, ws=True, t=True)
    if 0 < pos[0]:
        left_vtxs.append(vtx)
    elif 0 > pos[0]:
        right_vtxs.append(vtx)
    else:
        mid_vtxs.append(vtx)

# 判断中心两点的上下(默认上-下)
mid_vtxs_pos = []
for vtx in mid_vtxs:
    pos = cmds.xform(vtx, q=True, ws=True, t=True)
    mid_vtxs_pos.append(pos[1])

condition_np = np.array(mid_vtxs_pos)
y_min, y_max = min(condition_np), max(condition_np)
for vtx in mid_vtxs:
    pos = cmds.xform(vtx, q=True, ws=True, t=True)
    if pos[1] == y_max:
        broad_list.append([str(vtx)])
    else:
        broad_list.append([str(vtx)])


def x_value_vtx(value, x, vtxs):
    # 区分上下点列表和左右Broad点
    x_vtx = get_posx_vtx(vtxs,x)
    up = []
    low = []
    broad = []
    for vtx in vtxs:
        pos = cmds.xform(vtx, q=True, ws=True, t=True)
        if pos[1] > value:
            up.append(vtx)
        elif pos[1] < value:
            low.append(vtx)
        else:
            broad.append(vtx)
    return up, low, broad


x_pos_vtx = get_posx_vtx(left_vtxs,x_max)
x_neg_vtx = get_posx_vtx(right_vtxs,x_min)
up_left, low_left, left_broad = x_value_vtx(x_pos_vtx, x_max, left_vtxs)
up_right, low_right, right_broad = x_value_vtx(x_neg_vtx, x_min, right_vtxs)
#
broad_list.append(left_broad)
broad_list.append(right_broad)


location_list.append(up_left[::-1])
location_list.append(up_right[::-1])
location_list.append(low_left)
location_list.append(low_right)

ullr_side = get_ullr_side()
broad_side = get_broad_side()

for side in  range(len(ullr_side)):
    create_locator(location_list[side],'Jaw',ullr_side[side],'Location',0.1,13)
    create_locator(broad_list[side], 'Jaw', broad_side[side], 'Location',1,17)

cmds.select(cl=True)