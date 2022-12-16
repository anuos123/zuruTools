# create default config
import json
import os
import getpass
import PySide2.QtWidgets as QtWidgets

from maya_asset_viewer.widgets.pyside2_helper import maya_main_window

# ============================================================

def create_progress_update_config():
	
	# get output path
	username = getpass.getuser()
	outputPath = "C:/Users/{}/Documents/maya/scripts".format( username )
	# create config file name
	config_path = os.path.join( outputPath, "assetViewer.json" )
	
	# create warning message
	message = QtWidgets.QMessageBox()
	file_dialog = QtWidgets.QFileDialog()
	
	# show warning message
	message.warning(
		maya_main_window(),
		"Select directory",
		'Please select your default directory'
	)
	
	# get your main project path
	default_path = file_dialog.getExistingDirectory(
		parent = maya_main_window(),
		caption = "Select directory"
	)
	
	# if no path from file dialog then set main project path and preview image path as ""
	if default_path == "":
		message.warning(
			maya_main_window(),
			"Warning", 'No directory is select. No default directory'
		)
		previewImages_path = ""
	
	else:
		# create preview image path
		previewImages_path = os.path.join( default_path, "images" )
		if os.path.isdir(previewImages_path) == False:
			os.makedirs( previewImages_path )
		
	# toolbars visible
	show_bookmark 		= False
	show_preview_image 	= False
	show_quickSave		= True
	show_channelBox		= False
	# reminder
	double_warning_delete = True
	
	project_template = [ "models", "rigs", "images", "original materials", "complete" ]
	date_folder_format = "yyyymmdd"
	
	# bookmark
	bookmark = []
	
	# quick save
	quick_save_type = [ "model", "add_joints", "bind_skin", "edit_skin", "add_ctrl", "pose", "bind_pose", "clear", "fix" ]
	
	# snapshot
	width = "300"
	height = "300"
	image_format = "jpg"
	show_mesh = True
	show_joint = False
	show_curve = False
	
	config = {
		"defaultPath": default_path,
		"previewImagePath" : previewImages_path,
		"showBookmarkBar" : show_bookmark,
		"showPreviewImageBar" : show_preview_image,
		"showQuickSaveBar" : show_quickSave,
		"showChannelBox" : show_channelBox,
		"doubleWarningDelete" : double_warning_delete,
		"projectTemplate" : project_template,
		"dateFolderFormat" : date_folder_format,
		"bookmark" : bookmark,
		"quickSaveType" : quick_save_type,
		"width" : width,
		"height" : height,
		"imageFormat" : image_format,
		"showMesh" : show_mesh,
		"showJoint" : show_joint,
		"showCurve" : show_curve
	}
	
	# create config file
	with open(config_path, 'w') as f:
		json.dump(config, f)

# ============================================================