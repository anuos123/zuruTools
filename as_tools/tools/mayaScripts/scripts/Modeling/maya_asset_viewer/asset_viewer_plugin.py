"""Asset Viewer Plug-in for Maya"""

import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

from maya_asset_viewer.widgets.asset_viewer import assetViewerWidget

commandName = "assetViewerWidget"

class assetViewer(OpenMayaMPx.MPxCommand):
	
	def __init__(self):
		OpenMayaMPx.MPxCommand.__init__(self)
		
		workspace_control_name = assetViewerWidget.get_workspace_control_name()
		if cmds.window(workspace_control_name, exists=True):
			cmds.deleteUI(workspace_control_name)
	
		try:
			assetViewer_ui.setParent(None)
			assetViewer_ui.deleteLater()
		except:
			pass
		assetViewer_ui = assetViewerWidget()
	
	def doIt(self, args):
		pass

def cmdCreator():
	
	return OpenMayaMPx.asMPxPtr(assetViewer())

def initializePlugin(mobject):
	'''
		Initialize plug-in when Maya loads it.
	'''
	fn_plugin = OpenMayaMPx.MFnPlugin(mobject)
	fn_plugin.registerCommand(commandName,	cmdCreator)
	return
	try:
		fn_plugin.registerNode(
			commandName,
			cmdCreator
		)
	except:
		print("failed to load.")
	
def uninitializePlugin(mobject):
	'''
		Uninitialize plug-in when Maya un-load it.
	'''
	fn_plugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		fn_plugin.deregisterCommand(
			commandName
		)
	except:
		print("failed.")