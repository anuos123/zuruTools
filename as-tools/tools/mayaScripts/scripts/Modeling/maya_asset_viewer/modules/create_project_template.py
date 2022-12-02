import os
import getpass
import json

# ============================================================
username 	= getpass.getuser()
outputPath 	= "C:/Users/{}/Documents/maya/scripts".format( username )

config_path = os.path.join( outputPath, "assetViewer.json" )
# ============================================================

def create_project_template(
		destination = "",
		project_name = ""):
	'''
		destination [string] : path of the place that you want to create new dir project
		project_name [string] : project name
	'''
	
	# check exist config file
	check_config_file = os.path.isfile( config_path )
	
	with open(config_path, 'r') as f:
		config = json.load(f)
		project_template = config[ "projectTemplate" ]
	
	# create main dir for new project
	project_path = os.path.join( destination, project_name )
	os.mkdir( project_path )
	
	# create project sub folder from template config
	for fld in project_template:
		fldPath = os.path.join( project_path, fld )
		os.mkdir( fldPath )

# ============================================================