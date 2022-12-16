# call ui function
import maya.cmds as cmds

from maya_asset_viewer.widgets.asset_viewer import assetViewerWidget

if __name__ == "__main__":
	
	workspace_control_name = assetViewerWidget.get_workspace_control_name()
	if cmds.window(workspace_control_name, exists=True):
		cmds.deleteUI(workspace_control_name)
	
	try:
		assetViewer_ui.setParent(None)
		assetViewer_ui.deleteLater()
	except:
		pass
	assetViewer_ui = assetViewerWidget()