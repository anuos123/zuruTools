##### Capture Screen
# ============================================================

import os
import sys
import maya.cmds as cmds
import maya.OpenMayaUI as omui

import PySide2.QtWidgets as QtWidgets
import PySide2.QtCore as QtCore

from shiboken2 import wrapInstance
from maya_asset_viewer.widgets.pyside2_helper import maya_main_window

# ============================================================

class modelPanel(QtWidgets.QWidget):
	
	def __init__( self ):
		
		super( modelPanel, self ).__init__()
		
		# create layout
		layout = QtWidgets.QVBoxLayout(self)
		layout.setObjectName("viewportLayout")
		
		# create maya pane layout
		cmds.setParent("viewportLayout")
		pane_layout = cmds.paneLayout()
		
		# create model panel
		self.model_editor = cmds.modelEditor(
			displayAppearance = "smoothShaded",
			parent = pane_layout
		)
		
		# create pane_layout as QWidget
		ptr = omui.MQtUtil.findControl(pane_layout)
		if sys.version_info.major >= 3:
			pane_layout_qt = wrapInstance(int(ptr), QtWidgets.QWidget)
		else:
			pane_layout_qt = wrapInstance(long(ptr), QtWidgets.QWidget)
		
		layout.addWidget(pane_layout_qt)

class captureScreenWidget( QtWidgets.QWidget ):
	
	WINDOW_TITLE = "Capture Screen"
	
	def __init__(self, parent):
		
		super(captureScreenWidget, self).__init__(parent)
		
		self.setWindowTitle(self.WINDOW_TITLE)
		self.setWindowFlags(QtCore.Qt.WindowType.Window)
		
		self.base_size = 300
		self.destination = ""
		
		self.create_widgets()
		self.create_layouts()
		self.create_connections()
	
	# ============================================================
	
	def create_widgets( self ):
		
		self.model_editor = modelPanel()
		
		self.show_mesh_cb  = QtWidgets.QCheckBox( "Polygon" )
		self.show_curve_cb = QtWidgets.QCheckBox( "Nurbs Curve" )
		self.show_joint_cb = QtWidgets.QCheckBox( "Joint" )
		
		self.image_name_le = QtWidgets.QLineEdit()
		
		self.capture_btn = QtWidgets.QPushButton( "Capture!" )
		
		# setting widget
		cmds.modelEditor(
			self.model_editor.model_editor,
			e = True,
			grid = False,
			allObjects = False
		)
		cmds.modelEditor(
			self.model_editor.model_editor,
			e = True,
			grid = False,
			nurbsCurves = True,
			polymeshes = True,
			joints = True,
			headsUpDisplay = False
		)
		
		self.model_editor.setFixedWidth(self.base_size)
		self.model_editor.setFixedHeight(self.base_size)
		
		self.image_name_le.setPlaceholderText( "Image name" )
	
	def create_layouts( self ):
		
		main_layout = QtWidgets.QVBoxLayout( self )
		self.setLayout(main_layout)
		main_layout.setSpacing( 2 )
		main_layout.setContentsMargins( 5, 5, 5, 5 )
		
		# add into main layout
		main_layout.addWidget( self.model_editor )
		main_layout.addWidget( self.image_name_le )
		main_layout.addWidget( self.capture_btn )
	
	def create_connections( self ):
		
		self.capture_btn.clicked.connect( self.save_screenshot )
	
	# ============================================================
	
	def refresh_setting(self, base_size = 300, destination = ""):
		
		self.base_size = base_size
		self.destination = destination
	
	def save_screenshot( self ):
		
		if self.destination == "":
			file_path = cmds.fileDialog2(
				caption = "Save image to",
				fileMode = 3,
				okCaption = "Save"
			)
			if not file_path:
				return
			file_path = file_path[0]
		else:
			file_path = self.destination
		
		self.take_screenshot(path = file_path)
	
	def take_screenshot( self, path ):
		
		# get playblast setting
		current_time = cmds.currentTime(q = True)
		image_name = self.image_name_le.text()
		width  = self.base_size
		height = self.base_size
		model_editor = self.model_editor.model_editor
		
		# get camera
		cam = cmds.modelEditor(
			model_editor,
			query = True,
			camera = True
		)
		# create image file name
		file_name = os.path.join(path, image_name + ".jpg")
		
		# capture screen
		cmds.playblast(
			fr = current_time,
			v = False,
			fmt = "image",
			c = "jpg",
			orn = False,
			cf = file_name,
			wh = [width,height],
			p = 100
		)

# ============================================================
#captureScreenWidget(parent = maya_main_window()).show()