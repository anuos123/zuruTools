import maya.cmds as cmds

#object constants
GROUP = 'GRP'
JOINT = 'JNT'
GUIDE = 'guide'
JAW = 'jaw'

#side constants
LEFT = 'L'
RIGHT = 'R'
CENTER = 'C'

def createGuides(number = 5):
    #
    jaw_guide_grp = cmds.createNode('transform',n = '{}_{}_{}_{}'.format(CENTER,JAW,GUIDE,GROUP))
    locs_grp = cmds.createNode('transform', n='{}_{}_lip_{}_{}'.format(CENTER, JAW, GUIDE, GROUP),parent=jaw_guide_grp)
    lip_locs_grp = cmds.createNode('transform', n='{}_{}_lipMinor{}_{}'.format(CENTER, JAW, GUIDE, GROUP),parent=locs_grp)

    #create locator
    for part in ['Upper','Lower']:

        part_mult = 1 if part=='Upper' else -1
        mid_data = (0,part_mult,0)

        mid_loc = cmds.spaceLocator(n='{}_{}_{}_lip_{}'.format(CENTER,JAW,part,GUIDE))[0]
        cmds.parent(mid_loc,lip_locs_grp)

        for side in 'LR':
            for x in range(number):
                multiplier = x + 1 if side=='L' else -(x+1)
                loc_data = (multiplier,part_mult,0)
                loc = cmds.spaceLocator(n='{}_{}{}_lip_{:02d}_{}'.format(side,JAW,part,x+1,GUIDE))[0]
                cmds.parent(loc,lip_locs_grp)

                #set data
                cmds.setAttr('{}.t'.format(loc),*loc_data)
        cmds.setAttr('{}.t'.format(mid_loc),*mid_data)

    #create corners
    left_corner_loc = cmds.spaceLocator(n='{}_{}Corner_lip_{}'.format(LEFT,JAW,GUIDE))[0]
    right_corner_loc = cmds.spaceLocator(n='{}_{}Corner_lip_{}'.format(RIGHT, JAW, GUIDE))[0]

    cmds.parent(left_corner_loc,lip_locs_grp)
    cmds.parent(right_corner_loc, lip_locs_grp)

    cmds.setAttr('{}.t'.format(left_corner_loc),*(number+1,0,0))
    cmds.setAttr('{}.t'.format(right_corner_loc), *(-(number + 1), 0, 0))
    cmds.select(cl=True)

    #create jaw base
    jaw_base_guide_grp = cmds.createNode('transform',n = '{}_{}_base_{}_{}'.format(CENTER,JAW,GUIDE,GROUP),parent=jaw_guide_grp)
    jaw_guide = cmds.spaceLocator(n='{}_{}_{}'.format(CENTER,JAW,GUIDE))[0]
    jaw_inverse_guide = cmds.spaceLocator(n='{}_{}_inverse_{}'.format(CENTER,JAW,GUIDE))[0]

    cmds.setAttr('{}.t'.format(jaw_guide),*(0,-1,-number))
    cmds.setAttr('{}.t'.format(jaw_inverse_guide), *(0, 1, -number))

    cmds.parent(jaw_guide,jaw_base_guide_grp)
    cmds.parent(jaw_inverse_guide,jaw_base_guide_grp)
    cmds.select(cl=True)

def lip_guides():
    grp = '{}_{}_lipMinor{}_{}'.format(CENTER, JAW, GUIDE, GROUP)
    return [loc for loc in cmds.listRelatives(grp) if cmds.objExists(grp)]

def jaw_guides():
    grp = '{}_{}_{}_{}'.format(CENTER,JAW,GUIDE,GROUP)
    return [loc for loc in cmds.listRelatives(grp) if cmds.objExists(grp)]
