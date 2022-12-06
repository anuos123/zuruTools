#coding=utf-8

#选择控制器列表和需要替换的控制器,执行代码

def ao_shape_change():
    import maya.cmds as mc

    sel = mc.ls(sl=True)

    new_ctrl = sel[-1]
    old_ctrls = sel[:-1]

    for old_ctrl in old_ctrls:
        dup = mc.duplicate(new_ctrl, rc=True)
        mc.delete(mc.parentConstraint(old_ctrl, dup))
        mc.parent(dup, old_ctrl)
        mc.makeIdentity(dup, apply=True)
        old_shapes = mc.listRelatives(old_ctrl, type="shape", f=True)
        ctrl_shapes = mc.listRelatives(dup, type="shape", f=True)
        color = mc.getAttr(old_shapes[0] + ".overrideColor")

        for ctrl_shape in ctrl_shapes:
            mc.setAttr(ctrl_shape + ".overrideEnabled", 1)
            mc.setAttr(ctrl_shape + ".overrideColor", color)
            ren = mc.rename(ctrl_shape, old_ctrl + "Shape#")
            mc.parent(ren, old_ctrl, relative=True, shape=True)

        mc.delete(dup)
        mc.delete(old_shapes)

    mc.select(clear=True)