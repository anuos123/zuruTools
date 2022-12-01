import maya.cmds as cmds
try:
    from lib import reload
except:
    from importlib import reload

cmds.evalDeferred('import Menu;Menu.show()')