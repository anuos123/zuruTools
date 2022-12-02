# snapshot current panel
import os
import maya.cmds as cmds

# ============================================================

def take_screenshot(
	output = "",
	name = "",
	width = 300,
	height = 300,
	img_format = "jpg",
	show_poly = True,
	show_joint = False,
	show_curve = False
	):
		
	# get playblast setting
	current_time = cmds.currentTime(q = True)
	width  = width
	height = height
	panel = cmds.getPanel(withFocus = True)
	
	# get current model editor status
	_cameras = cmds.modelEditor(panel, q = True, cameras = True)
	_deformers = cmds.modelEditor(panel, q = True, deformers = True)
	_dimensions = cmds.modelEditor(panel, q = True, dimensions = True)
	_dynamicConstraints = cmds.modelEditor(panel, q = True, dynamicConstraints = True)
	_dynamics = cmds.modelEditor(panel, q = True, dynamics = True)
	_fluids = cmds.modelEditor(panel, q = True, fluids = True)
	_follicles = cmds.modelEditor(panel, q = True, follicles = True)
	_grid = cmds.modelEditor(panel, q = True, grid = True)
	_headsUpDisplay = cmds.modelEditor(panel, q = True, headsUpDisplay = True)
	_ikHandles = cmds.modelEditor(panel, q = True, ikHandles = True)
	_imagePlane = cmds.modelEditor(panel, q = True, imagePlane = True)
	_joints = cmds.modelEditor(panel, q = True, joints = True)
	_lights = cmds.modelEditor(panel, q = True, lights = True)
	_locators = cmds.modelEditor(panel, q = True, locators = True)
	_manipulators = cmds.modelEditor(panel, q = True, manipulators = True)
	_motionTrails = cmds.modelEditor(panel, q = True, motionTrails = True)
	_nCloths = cmds.modelEditor(panel, q = True, nCloths = True)
	_nParticles = cmds.modelEditor(panel, q = True, nParticles = True)
	_nRigids = cmds.modelEditor(panel, q = True, nRigids = True)
	_nurbsCurves = cmds.modelEditor(panel, q = True, nurbsCurves = True)
	_nurbsSurfaces = cmds.modelEditor(panel, q = True, nurbsSurfaces = True)
	_pivots = cmds.modelEditor(panel, q = True, pivots = True)
	_planes = cmds.modelEditor(panel, q = True, planes = True)
	_polymeshes = cmds.modelEditor(panel, q = True, polymeshes = True)
	_strokes = cmds.modelEditor(panel, q = True, strokes = True)
	_subdivSurfaces = cmds.modelEditor(panel, q = True, subdivSurfaces = True)
	_wireframeOnShaded = cmds.modelEditor(panel, q = True, wireframeOnShaded = True)
	_xray = cmds.modelEditor(panel, q = True, xray = True)
	
	# set model editor
	cmds.modelEditor(
		panel,
		e = True,
		grid = False,
		xray = False,
		allObjects = False
	)
	cmds.modelEditor(
		panel,
		e = True,
		displayAppearance = "smoothShaded",
		wireframeOnShaded = False,
		polymeshes = show_poly,
		joints = show_joint,
		nurbsCurves = show_curve
	)
	
	# get camera
	cam = cmds.modelEditor(
		panel,
		query = True,
		camera = True
	)
	image_name = os.path.join(
		output,
		"{}.{}".format(name, img_format)
	)
	
	# capture screen
	cmds.playblast(
		frame = current_time,
		viewer = False,
		format = "image",
		compression = img_format,
		showOrnaments = False,
		completeFilename = image_name,
		widthHeight = [width,height],
		percent = 100,
		quality = 100
	)
	
	# set model editor back
	cmds.modelEditor(panel, e = True, cameras = _cameras)
	cmds.modelEditor(panel, e = True, deformers = _deformers)
	cmds.modelEditor(panel, e = True, dimensions = _dimensions)
	cmds.modelEditor(panel, e = True, dynamicConstraints = _dynamicConstraints)
	cmds.modelEditor(panel, e = True, dynamics = _dynamics)
	cmds.modelEditor(panel, e = True, fluids = _fluids)
	cmds.modelEditor(panel, e = True, follicles = _follicles)
	cmds.modelEditor(panel, e = True, grid = _grid)
	cmds.modelEditor(panel, e = True, headsUpDisplay = _headsUpDisplay)
	cmds.modelEditor(panel, e = True, ikHandles = _ikHandles)
	cmds.modelEditor(panel, e = True, imagePlane = _imagePlane)
	cmds.modelEditor(panel, e = True, joints = _joints)
	cmds.modelEditor(panel, e = True, lights = _lights)
	cmds.modelEditor(panel, e = True, locators = _locators)
	cmds.modelEditor(panel, e = True, manipulators = _manipulators)
	cmds.modelEditor(panel, e = True, motionTrails = _motionTrails)
	cmds.modelEditor(panel, e = True, nCloths = _nCloths)
	cmds.modelEditor(panel, e = True, nParticles = _nParticles)
	cmds.modelEditor(panel, e = True, nRigids = _nRigids)
	cmds.modelEditor(panel, e = True, nurbsCurves = _nurbsCurves)
	cmds.modelEditor(panel, e = True, nurbsSurfaces = _nurbsSurfaces)
	cmds.modelEditor(panel, e = True, pivots = _pivots)
	cmds.modelEditor(panel, e = True, planes = _planes)
	cmds.modelEditor(panel, e = True, polymeshes = _polymeshes)
	cmds.modelEditor(panel, e = True, strokes = _strokes)
	cmds.modelEditor(panel, e = True, subdivSurfaces = _subdivSurfaces)
	cmds.modelEditor(panel, e = True, wireframeOnShaded = _wireframeOnShaded)
	cmds.modelEditor(panel, e = True, xray = _xray)

# ============================================================