import os
import subprocess
import maya.cmds as cd
import maya.mel as mel

# ============================================================

def create_new_dir(item = "", dir_name = ""):
	
	# check item is file or dir
	check_isfile = os.path.isfile(item)
	# if item is file then extract item name from the path
	if check_isfile == True:
		item_name = os.path.basename(item)
		item = item.split( "/" + item_name )[0]
	# create new dir
	os.mkdir( os.path.join( item, dir_name ) )

def open_window_explorer(item = ""):
	
	# check item is file or dir
	check_isfile = os.path.isfile(item)
	# if item is file then extract item name from the path
	if check_isfile == True:
		item_name = os.path.basename(item)
		item = item.split( item_name )[0]
	
	# change / to \ for windows only
	current_item = item.replace( "/", "\\" )
	subprocess.Popen( 'explorer {}'.format(current_item) )

def open_window_with(item = ""):
	
	# this function is similar to open_window_explorer but not extract file name from item
	# change / to \ for windows only
	current_item = item.replace( "/", "\\" )
	subprocess.Popen( 'explorer {}'.format(current_item) )

def export_fbx_file(
		fileName = "",
		output = "",
		exportAll = True):
	
	fileName = fileName.replace( " ", "" )
	export_file_name = fileName + ".fbx"
	full_path = os.path.join( output, export_file_name )
	
	# change \ to / for prevent export error
	full_path = full_path.replace( "\\", "/" )
	# check space if space is in the path export function will error
	full_path = full_path.replace( " ", "" )
	# check export all
	if exportAll:
		mel_cmd = 'FBXExport -f "{}";'.format( full_path )
	else:
		mel_cmd = 'FBXExport -f "{}" -s;'.format( full_path )

	mel.eval(mel_cmd)

def export_obj_file(
		fileName = "",
		output = "",
		exportAll = True,
		groups = 1,
		ptgroups = 1,
		materials = 1,
		smoothing = 1,
		normals = 1 ):
	
	# create export file name
	export_file_name = fileName + ".obj"
	full_path = os.path.join( output, export_file_name )
	
	# set exort options
	options = ""
	if groups:
		options += "groups=1;"
	else:
		options += "groups=0;"
	
	if ptgroups:
		options += "ptgroups=1;"
	else:
		options += "ptgroups=0;"
	
	if materials:
		options += "materials=1;"
	else:
		options += "materials=0;"
	
	if smoothing:
		options += "smoothing=1;"
	else:
		options += "smoothing=0;"
	
	if normals:
		options += "normals=1;"
	else:
		options += "normals=0;"
	
	# check export all
	if exportAll:
		cd.file(
			full_path,
			preserveReferences = True,
			type = "OBJexport",
			exportAll = True ,
			op = options
		)
	
	else:
		cd.file(
			full_path,
			preserveReferences = True,
			type = "OBJexport",
			exportSelected = True ,
			op = options
		)

def import_file(
		item = "",
		path = ""):
	
	# check file type
	fileType = item.split( "." )[-1]
	namespace = item.split( "." + fileType )[0]
	
	if fileType in ["obj", "OBJ"]:
		importType = "OBJ"
	
	elif fileType in ["fbx", "FBX"]:
		importType = "FBX"
	
	elif fileType == "ma":
		importType = "mayaAscii"
	
	elif fileType == "mb":
		importType = "mayaBinary"
	
	cd.file( 
		path,
		i = True,
		type = importType,
		mergeNamespaceWithRoot = True,
		mergeNamespacesOnClash = True,
		namespace = namespace,
		importTimeRange = "keep"
	)

# ============================================================