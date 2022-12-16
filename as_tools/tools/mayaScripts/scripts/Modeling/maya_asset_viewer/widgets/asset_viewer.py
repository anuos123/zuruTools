# asset manager widget
import sys
import os
import getpass
import json

import PySide2.QtWidgets as QtWidgets
import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui

import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaUI as omui

from datetime import date
from shiboken2 import wrapInstance

from maya_asset_viewer.widgets.pyside2_helper 				import maya_main_window, WorkspaceControl, customTreeView, imageWidget, tabWidget
from maya_asset_viewer.widgets.insert_fileName_widget 		import insertFileNameWidget
from maya_asset_viewer.widgets.quick_save_progress_widget	import quickSaveProgressWidget
from maya_asset_viewer.widgets.setting_widget				import settingWidget
from maya_asset_viewer.modules.widget_functions				import create_new_dir, open_window_explorer, open_window_with, export_fbx_file, export_obj_file, import_file
from maya_asset_viewer.modules.create_project_template		import create_project_template
from maya_asset_viewer.modules.snapshot_function			import take_screenshot

# ============================================================
# get icon
SCRIPT_PATH = __file__
ICON_PATH = SCRIPT_PATH.split( "\\widgets" )[0]
ICON_PATH = os.path.join( ICON_PATH, "icons" )
ICON_PATH = ICON_PATH.replace( "\\", "/" )


folder_icon 	= ICON_PATH + "/folder.svg"
maya_icon 		= ICON_PATH + "/mayaIcon.png"
bookmark_icon 	= ICON_PATH + "/bookmark.png"
newPrj_icon		= ICON_PATH + "/newPrj.png"
import_icon		= ICON_PATH + "/import.png"
addBookmark_icon = ICON_PATH + "/addBookmark.png"
removeBookmmark_icon = ICON_PATH + "/removeBookmark.png"
snapshot_icon = ICON_PATH + "/snapshot.svg"
# ============================================================

class QChannelBox( QtWidgets.QWidget ):
	
	def __init__( self ):
		super( QChannelBox, self ).__init__()
		layout = QtWidgets.QVBoxLayout( self )
		
		layout.setObjectName( "channelBoxLayout" )
	
		cmds.setParent( "channelBoxLayout" )
		pane_layout = cmds.paneLayout()
		
		self.channelBox = cmds.channelBox( 'Qchb', parent = pane_layout )
		ptr = omui.MQtUtil.findControl( pane_layout )
		if sys.version_info.major >= 3:
			self.pane_layout_qt = wrapInstance( int( ptr ), QtWidgets.QWidget )
		else:
			self.pane_layout_qt = wrapInstance( int( ptr ), QtWidgets.QWidget )
		
		layout.addWidget( self.pane_layout_qt )

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

class assetViewerWidget( QtWidgets.QMainWindow ):
	
	WINDOW_TITLE = "Asset Viewer"
	UI_NAME = "assetViewerUI"
	ui_instance = None
	
	@classmethod
	def display(cls):
		if cls.ui_instance:
			cls.ui_instance.show_workspace_control()
		else:
			cls.ui_instance = assetViewerWidget()
	
	@classmethod
	def get_workspace_control_name(cls):
		return "{0}WorkspaceControl".format(cls.UI_NAME)
	
	def __init__( self, parent = None ):
		
		super( assetViewerWidget, self ).__init__( parent )
		
		self.setWindowTitle( self.WINDOW_TITLE )
		self.setWindowFlags( QtCore.Qt.WindowType.Window )
		
		self.setting_widget = settingWidget(parent = self)
		self.setting_widget.setWindowTitle("Preferences")
		
		self.createMenuBar()
		self.create_widgets()
		self.create_snapshot_widget()
		self.create_toolBar()
		self.create_layouts()
		self.create_connections()
		self.create_workspace_control()
		
		self.load_setting()
	
	# ============================================================
	
	def create_workspace_control(self):
		self.workspace_control_instance = WorkspaceControl(
			self.get_workspace_control_name()
		)
		if self.workspace_control_instance.exists():
			self.workspace_control_instance.restore(self)
		else:
			self.workspace_control_instance.create(
				self.WINDOW_TITLE,
				self,
				ui_script="from workspace_control import assetViewerUI\nassetViewerUI.display()"
			)
	
	def show_workspace_control(self):
		self.workspace_control_instance.set_visible(True)
	
	def showEvent(self, e):
		if self.workspace_control_instance.is_floating():
			self.workspace_control_instance.set_label("Asset Viewer")
		else:
			self.workspace_control_instance.set_label("Asset Viewer")
	
	# ============================================================
	
	def createMenuBar(self):
		
		# create menu bar
		menuBar = QtWidgets.QMenuBar(self)
		self.setMenuBar(menuBar)
		
		editMenu = QtWidgets.QMenu("&Edit")
		menuBar.addMenu(editMenu)
		
		helpMenu = QtWidgets.QMenu("&Help")
		menuBar.addMenu(helpMenu)
		
		preferences_ac = QtWidgets.QAction( "Preferences", editMenu )
		editMenu.addAction( preferences_ac )
		
		about_ac = QtWidgets.QAction( "About", helpMenu )
		helpMenu.addAction( about_ac )
		
		# create connections
		preferences_ac.triggered.connect( self.show_setting_widget )
		about_ac.triggered.connect( self.about_widget )
		
	def create_widgets( self ):
		
		self.quick_save_progress_widget = quickSaveProgressWidget( parent = self )
		
		self.channelBox = QChannelBox()
		
		# create font
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setWeight(50)
		
		# label
		self.bookmark_lb = QtWidgets.QLabel( "Bookmark" )
		self.bookmark_lb.setFont( font )
		self.bookmark_lb.setAlignment( QtCore.Qt.AlignCenter )
		self.bookmark_lb.setStyleSheet( "background-color:rgb(245, 190, 40);color:Black" )
		
		# current path
		self.current_path_le = QtWidgets.QLineEdit()
		self.current_path_le.setPlaceholderText( "Current Path" )
		self.selection_item_le = QtWidgets.QLineEdit()
		
		# tree view
		self.item_tree_view = customTreeView( "" )
		self.item_tree_view.current_item = ""
		self.item_tree_view.setColumnWidth(0, 300)
		self.item_tree_view.setColumnHidden(1, True)
		self.item_tree_view.setColumnHidden(3, True)
		
		# add more menu for tree view
		self.item_tree_view.menu.addSeparator()
		self.add_bookmark_menu			= self.item_tree_view.menu.addAction( "Add Bookmark" )
		self.item_tree_view.menu.addSeparator()
		self.open_window_explorer_menu 	= self.item_tree_view.menu.addAction( "Open Window Explorer" )
		self.open_window_with_menu 		= self.item_tree_view.menu.addAction( "Open With..." )
		self.item_tree_view.menu.addSeparator()
		self.newDir_menu 				= self.item_tree_view.menu.addAction( "Create New Folder" )
		self.newDir_date_menu 			= self.item_tree_view.menu.addAction( "Create current date Folder" )
		self.item_tree_view.menu.addSeparator()
		self.delete_menu 				= self.item_tree_view.menu.addAction( "Delete" )
		
		# bookmark
		self.bookmark_list = QtWidgets.QListWidget()
		self.bookmark_list_menu = QtWidgets.QListWidget()
		self.bookmark_list.setFixedWidth(250)
		
		self.addBookmark_btn 		= QtWidgets.QPushButton( "" )
		self.addBookmark_btn.setIcon(QtGui.QIcon(addBookmark_icon))
		self.addBookmark_btn.setIconSize(QtCore.QSize(18, 18))
		self.removeBookmark_btn 	= QtWidgets.QPushButton( "" )
		self.removeBookmark_btn.setIcon(QtGui.QIcon(removeBookmmark_icon))
		self.removeBookmark_btn.setIconSize(QtCore.QSize(18, 18))
		
		# preview image
		self.preview_image = imageWidget( image = ":objectSet.svg", width = 250 )
		self.preview_image.setFixedWidth(250)
		self.preview_image.setFixedHeight(250)
		
		# popup widget
		self.newDir_widget = insertFileNameWidget(
			parent = self,
			windowTitle = "New Folder",
			newName = "Folder name : "
		)
		self.newPrj_widget = insertFileNameWidget(
			parent = self,
			windowTitle = "New Project",
			newName = "Project name : "
		)
		
		self.credit_lb = QtWidgets.QLabel( "Created by faruq00" )
		self.credit_lb.setStyleSheet( "background-color:rgb(245, 190, 40);color:Black" )
		self.credit_lb.setAlignment( QtCore.Qt.AlignCenter )
	
	def create_snapshot_widget(self):
		
		# create model editor for preview image size
		self.model_editor = modelPanel()
		# set hide all object first
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
		self.model_editor.setFixedHeight(250)
		self.model_editor.setFixedWidth(250)
		self.capture_btn = QtWidgets.QPushButton( "Capture!" )
		
		self.snapshot_widget = QtWidgets.QWidget()
		layout = QtWidgets.QVBoxLayout(self.snapshot_widget)
		layout.setSpacing(2)
		layout.setContentsMargins(0, 0, 0, 0)
		layout.addWidget(self.model_editor)
		layout.addWidget(self.capture_btn)
	
	def create_toolBar( self ):
		
		# tools toolbar
		tools_tb = QtWidgets.QToolBar("Tools", self)
		self.addToolBar( QtCore.Qt.TopToolBarArea, tools_tb )
		self.addToolBarBreak()
		
		# create action
		self.bookmark_Action = QtWidgets.QAction( "Bookmark", self )
		self.bookmark_Action.setIcon( QtGui.QIcon(bookmark_icon) )
		
		self.newPrj_Action = QtWidgets.QAction( "New Project", self )
		self.newPrj_Action.setIcon( QtGui.QIcon(newPrj_icon) )
		
		self.newFld_Action = QtWidgets.QAction( "New Folder", self )
		self.newFld_Action.setIcon( QtGui.QIcon(":folder-new.png") )
		
		self.openfile_Action = QtWidgets.QAction( "open file", self )
		self.openfile_Action.setIcon( QtGui.QIcon(":openScript.png") )
		
		self.import_Action = QtWidgets.QAction( "Import", self )
		self.import_Action.setIcon( QtGui.QIcon(import_icon) )
		
		self.export_Action = QtWidgets.QAction( "Export", self )
		self.export_Action.setIcon( QtGui.QIcon(":output.png") )
		
		tools_tb.addAction( self.bookmark_Action )
		tools_tb.addAction( self.newPrj_Action )
		tools_tb.addAction( self.newFld_Action )
		tools_tb.addAction( self.openfile_Action )
		tools_tb.addAction( self.import_Action )
		#tools_tb.addAction( self.export_Action )
		
		# preview image
		self.preview_image_tb = QtWidgets.QToolBar( "Preview Image", self )
		self.addToolBar( QtCore.Qt.LeftToolBarArea, self.preview_image_tb)
		image_tab = tabWidget()
		image_tab.addTab( "Preview", self.preview_image )
		image_tab.addTab( "Snapshot", self.snapshot_widget )
		self.preview_image_tb.addWidget( image_tab )
		self.preview_image_tb.setVisible( False )
		
		# bookmark
		self.bookmark_tb = QtWidgets.QToolBar( "Bookmark", self )
		self.addToolBar( QtCore.Qt.LeftToolBarArea, self.bookmark_tb)
		self.bookmark_tb.addWidget( self.bookmark_lb )
		self.bookmark_tb.addWidget( self.bookmark_list )
		# create bookmark menu
		self.create_bookmark_menu()
		
		bookmark_widget = QtWidgets.QWidget()
		bookmark_layout = QtWidgets.QHBoxLayout( bookmark_widget )
		bookmark_layout.setSpacing( 1 )
		bookmark_layout.setContentsMargins( 3, 3, 3, 3 )
		
		bookmark_layout.addWidget( self.addBookmark_btn )
		bookmark_layout.addWidget( self.removeBookmark_btn )
		self.bookmark_tb.addWidget( bookmark_widget )
		self.bookmark_tb.setVisible( False )
		
		# quick save progress
		self.quickSave_tb = QtWidgets.QToolBar( "Quick save", self )
		self.addToolBar( QtCore.Qt.TopToolBarArea, self.quickSave_tb)
		self.quickSave_tb.addWidget( self.quick_save_progress_widget )
		
	
	def create_layouts( self ):
		
		# create main layout
		main_widget = QtWidgets.QWidget()
		main_layout = QtWidgets.QVBoxLayout( main_widget )
		main_layout.setSpacing( 1 )
		main_layout.setContentsMargins( 3, 3, 3, 3 )
		
		current_path_layout = QtWidgets.QFormLayout()
		current_path_layout.addRow( "Path : ", self.current_path_le )
		current_path_layout.addRow( "Selection : ", self.selection_item_le )
		
		main_layout.addLayout( current_path_layout )
		main_layout.addWidget( self.item_tree_view )
		main_layout.addWidget( self.credit_lb )
		
		spliter = QtWidgets.QSplitter()
		spliter.setOrientation( QtCore.Qt.Vertical )

		spliter.addWidget( self.channelBox )
		spliter.addWidget( main_widget )
		spliter.setStretchFactor(1, 1)
		#spliter.setSizes([50, 50])
		
		self.setCentralWidget( spliter )
	
	def create_connections( self ):
		
		self.setting_widget.save_config_btn.clicked.connect( self.load_setting )
		self.item_tree_view.doubleClicked.connect( self.double_click_file )
		self.item_tree_view.pressed.connect( self.update_preview_image )
		self.item_tree_view.pressed.connect( self.update_selection )
		
		# toolbar actions
		self.bookmark_Action.triggered.connect(self.open_bookmark_menu )
		self.newPrj_Action.triggered.connect( self.create_new_project_popup )
		self.newFld_Action.triggered.connect( self.create_new_dir_popup )
		self.openfile_Action.triggered.connect( self.open_file )
		self.import_Action.triggered.connect( self.import_select_file )
		
		# snapshot
		self.capture_btn.clicked.connect(self.snapshot)
		
		# connections for menu
		self.open_window_explorer_menu.triggered.connect( self.open_window_explorer )
		self.open_window_with_menu.triggered.connect( self.open_window_with )
		self.add_bookmark_menu.triggered.connect( self.rightClick_add_bookmark )
		self.newDir_menu.triggered.connect( self.create_new_dir_popup )
		self.newDir_date_menu.triggered.connect( self.create_current_date_dir )
		self.delete_menu.triggered.connect( self.delete_select )
		
		# bookmark
		self.bookmark_list_menu.clicked.connect( self.switch_path_from_bookmark_menu )
		self.bookmark_list.clicked.connect( self.switch_path_from_bookmark )
		# add reload bookmark for add new bookmark from setting widget
		self.addBookmark_btn.clicked.connect( self.setting_widget.addBookmark_widget.show )
		self.setting_widget.add_btn.clicked.connect( self.add_new_bookmark )
		self.removeBookmark_btn.clicked.connect( self.delete_bookmark )
		
		# update path
		self.current_path_le.returnPressed.connect( self.update_current_path )
		
		# popup widget
		self.newDir_widget.create_btn.clicked.connect( self.create_new_dir )
		self.newDir_widget.create_btn.clicked.connect( self.newDir_widget.close )
		self.newPrj_widget.create_btn.clicked.connect( self.create_new_project )
		self.newPrj_widget.create_btn.clicked.connect( self.newPrj_widget.close )
		
		# quick save
		self.quick_save_progress_widget.addPath_btn.clicked.connect( self.add_select_item_from_tree )
		self.quick_save_progress_widget.outputPath_le.returnPressed.connect( self.add_select_item_from_tree )
	
	# ============================================================
	# load setting
	# ============================================================
	
	def load_setting( self ):
		
		#
		default_path = self.setting_widget.default_path_le.text()
		# reload treeview
		self.current_path_le.setText( default_path )
		self.item_tree_view.update_root( default_path )
		
		# toolbar visible
		show_bookmark 			= self.setting_widget.show_bookmark_cb.isChecked()
		show_preview_image 		= self.setting_widget.show_previewImage_cb.isChecked()
		show_quickSave 			= self.setting_widget.show_quickSave_cb.isChecked()
		show_channelBox 		= self.setting_widget.show_channelBox_cb.isChecked()
		double_warning_delete 	= self.setting_widget.ask_before_delete_cb.isChecked()
		
		self.bookmark_tb.setVisible( show_bookmark )
		self.preview_image_tb.setVisible( show_preview_image )
		self.quickSave_tb.setVisible( show_quickSave )
		self.channelBox.setVisible( show_channelBox )
		
		# bookmark
		self.load_bookmark()
		
		# quick save
		self.quick_save_progress_widget.progressType_cb.clear()
		count = self.setting_widget.progressType_list.count()
		for n in range( count ):
			# set index
			currennt_item = self.setting_widget.progressType_list.item(n)
			self.quick_save_progress_widget.progressType_cb.addItem( currennt_item.text() )
	
	# ============================================================
	
	def closeEvent(self, event):
		# it's not working. I don't know how to fix yet.
		self.setting_widget.close()
	
	def update_current_path( self ):
		
		path = self.current_path_le.text()
		self.item_tree_view.update_root( path )
	
	def update_selection( self ):
		
		self.selection_item_le.setText(
			self.item_tree_view.current_item
		)
	
	def show_setting_widget( self ):
		
		self.setting_widget.load_config()
		self.setting_widget.show()
	
	# ============================================================
	
	def open_file( self ):
		
		item = self.item_tree_view.current_item
		check_isfile = os.path.isfile( item )
		if check_isfile == True:
			
			fileName = os.path.basename( item )
			fileType = fileName.split( "." )[-1]
			
			if fileType in [ "ma", "mb" ]:
				reply = QtWidgets.QMessageBox.question(self, 'Warning',
					"Do you want to open {}?".format( fileName ), QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
				
				if reply == QtWidgets.QMessageBox.Yes:
					cmds.file( item, open = True, force = True )
	
	def double_click_file( self ):
		
		item = self.item_tree_view.current_item
		check_isfile = os.path.isfile( item )
		if check_isfile == True:
			
			fileName = os.path.basename( item )
			fileType = fileName.split( "." )[-1]
			
			if fileType in [ "ma", "mb" ]:
				self.open_file()
			
			else:
				reply = QtWidgets.QMessageBox.question(self, 'Warning',
					"Do you want to import {}?".format( fileName ), QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
				
				if reply == QtWidgets.QMessageBox.Yes:
					import_file( fileName, item )
	
	def open_window_explorer( self ):
		
		item = self.item_tree_view.current_item
		open_window_explorer( item = item )
	
	def open_window_with( self ):
		
		item = self.item_tree_view.current_item
		open_window_with( item = item )
	
	def create_new_dir_popup( self ):
		
		item = self.item_tree_view.current_item
	
		check_isfile = os.path.isfile( item )
		if check_isfile == True:
			item_name = os.path.basename(item)
			item = item.split( "/" + item_name )[0]
		
		self.newDir_widget.outputPath_le.setText( item )
		self.newDir_widget.show()
	
	def create_new_dir( self ):
		
		dir_name 	= self.newDir_widget.fileName_le.text()
		item 		= self.newDir_widget.outputPath_le.text()
		create_new_dir( item, dir_name )
		self.newDir_widget.fileName_le.setText( "" )
	
	def create_current_date_dir(self):
		
		today = str(date.today())
		dir_name = today.replace("-", "")
		
		item = self.item_tree_view.current_item
	
		check_isfile = os.path.isfile( item )
		if check_isfile == True:
			item_name = os.path.basename(item)
			item = item.split( "/" + item_name )[0]
		
		create_new_dir( item, dir_name )
		self.newDir_widget.fileName_le.setText( "" )
	
	def import_select_file( self ):
		
		item_path = self.item_tree_view.current_item
		item = os.path.basename( item_path )
		
		if os.path.isfile( item_path ) == True:
			import_file( item, item_path )
	
	def create_new_project_popup( self ):
		
		item = self.item_tree_view.current_item
	
		check_isfile = os.path.isfile( item )
		if check_isfile == True:
			item_name = os.path.basename(item)
			item = item.split( "/" + item_name )[0]
		
		self.newPrj_widget.outputPath_le.setText( item )
		self.newPrj_widget.show()
	
	def create_new_project( self ):
		
		destination = self.newPrj_widget.outputPath_le.text()
		prjName 	= self.newPrj_widget.fileName_le.text()
		
		create_project_template( destination, prjName )
		
		# add into bookmark
		prjPath = os.path.join( destination, prjName )
		
		list_wdg_item = QtWidgets.QListWidgetItem(prjName)
		list_wdg_item.setData(QtCore.Qt.UserRole, prjPath)
		self.setting_widget.bookmark_list.addItem( list_wdg_item )
		self.setting_widget.save_config()
		self.load_bookmark()
	
	def delete_select( self ):
		
		current_item = self.item_tree_view.current_item
		
		reply = QtWidgets.QMessageBox.question(self, 'Warning',
			"Do you want to delete this item?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
		
		if reply == QtWidgets.QMessageBox.No:
			return
		
		check_double = self.setting_widget.ask_before_delete_cb.isChecked()
		if check_double == True:
			reply = QtWidgets.QMessageBox.question(self, 'Warning',
				"Are you sure to delete?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
			
			if reply == QtWidgets.QMessageBox.No:
				return
			
		if os.path.isfile( current_item ) == True:
			os.remove( current_item )
		else:
			os.rmdir( current_item )
	
	# ============================================================
	# Bookmark
	# ============================================================
	
	def load_bookmark( self ):
		
		# clear list
		self.bookmark_list.clear()
		self.bookmark_list_menu.clear()
		
		# set default bookmark
		list_wdg_item = QtWidgets.QListWidgetItem("Default")
		list_wdg_item.setData(QtCore.Qt.UserRole, self.setting_widget.default_path_le.text() )
		self.bookmark_list.addItem( list_wdg_item )
		
		list_wdg_item_menu = QtWidgets.QListWidgetItem("Default")
		list_wdg_item_menu.setData(QtCore.Qt.UserRole, self.setting_widget.default_path_le.text() )
		self.bookmark_list_menu.addItem( list_wdg_item_menu )
		
		count = self.setting_widget.bookmark_list.count()
		for n in range( count ):
			# set index
			currennt_item = self.setting_widget.bookmark_list.item(n)
			name = currennt_item.text()
			path = currennt_item.data(QtCore.Qt.UserRole)
			
			list_wdg_item = QtWidgets.QListWidgetItem(name)
			list_wdg_item.setData(QtCore.Qt.UserRole, path)
			self.bookmark_list.addItem( list_wdg_item )
			
			list_wdg_item_menu = QtWidgets.QListWidgetItem(name)
			list_wdg_item_menu.setData(QtCore.Qt.UserRole, path)
			self.bookmark_list_menu.addItem( list_wdg_item_menu )
	
	def create_bookmark_menu( self ):
		
		self.bookmark_menu = QtWidgets.QMenu()

		bookmark_wdg	= QtWidgets.QWidget()
		layout			= QtWidgets.QVBoxLayout( bookmark_wdg )
		layout.setContentsMargins( 1, 1, 1, 1 )
		layout.setSpacing( 1 )
		layout.addWidget( QtWidgets.QLabel( "Bookmark" ) )
		layout.addWidget( self.bookmark_list_menu )

		bookmark_action = QtWidgets.QWidgetAction( self.bookmark_menu )
		bookmark_action.setDefaultWidget( bookmark_wdg )

		self.bookmark_menu.addAction( bookmark_action )
	
	def open_bookmark_menu( self, position ):

		if not position:
			position = QtGui.QCursor.pos()
		
		self.bookmark_menu.exec_(maya_main_window().mapToGlobal(position))
	
	def switch_path_from_bookmark( self ):
		
		currennt_item = self.bookmark_list.currentItem()
		item = currennt_item.data(QtCore.Qt.UserRole)
		self.item_tree_view.update_root( item )
		self.item_tree_view.current_item = item

		self.current_path_le.setText( item )
	
	def switch_path_from_bookmark_menu( self ):
		
		currennt_item = self.bookmark_list_menu.currentItem()
		item = currennt_item.data(QtCore.Qt.UserRole)
		self.item_tree_view.update_root( item )
		self.item_tree_view.current_item = item

		self.current_path_le.setText( item )

		self.bookmark_menu.close()
	
	def add_new_bookmark( self ):
		
		self.load_bookmark()
		self.setting_widget.save_config()
	
	def delete_bookmark( self ):
		
		currentItem = self.bookmark_list.currentItem()
		self.bookmark_list.takeItem(self.bookmark_list.row(currentItem))
		
		# remove from setting widget
		count = self.setting_widget.bookmark_list.count()
		for n in range( count ):
			# set index
			currennt_item = self.setting_widget.bookmark_list.item(n)
			if currennt_item.text() == currentItem.text():
				self.setting_widget.bookmark_list.takeItem(self.setting_widget.bookmark_list.row(currennt_item))
		self.setting_widget.save_config()
		self.load_bookmark()
	
	def rightClick_add_bookmark( self ):
		
		item = self.item_tree_view.current_item
		name = os.path.basename( item )
		
		if os.path.isdir( item ) == True:
			self.setting_widget.bookmark_name.setText( name )
			self.setting_widget.bookmark_path.setText( item )
			self.setting_widget.add_bookmark()
		self.setting_widget.save_config()
		self.load_bookmark()
	
	# ============================================================
	# Quick save
	# ============================================================
	
	def add_select_item_from_tree( self ):
		
		current_path = self.item_tree_view.current_item
		if os.path.isfile( current_path ) == True:
			fileName = os.path.basename( current_path )
			current_path = current_path.split( fileName )[0]
		
		self.quick_save_progress_widget.outputPath_le.setText( current_path )
		self.quick_save_progress_widget.check_progress_files()
	
	# ============================================================
	# Preview image
	# ============================================================
	
	def update_preview_image( self ):
		
		item = self.item_tree_view.current_item
		preview_image_dir = self.setting_widget.default_imagesPath_le.text()
		
		item_name = os.path.basename(item)
		image_file = "{}/{}.png".format( preview_image_dir, item_name.split(".")[0] )
		if os.path.isfile( image_file ) == False:
			image_file = "{}/{}.jpg".format( preview_image_dir, item_name.split(".")[0] )
			if os.path.isfile( image_file ) == False:
				image_file = "{}/{}.jpeg".format( preview_image_dir, item_name.split(".")[0] )
		
		check_image = os.path.isfile( image_file )

		if check_image == True:
			self.preview_image.update_image( image_file )
		
		else:
			
			check_isfile = os.path.isfile( item )
			if check_isfile == True:
				item_name = os.path.basename(item)
				check_filetype = item_name.split( "." )[-1]
				
				if check_filetype in [ "png", "PNG", "jpg", "JPG", "jpeg" ]:
					self.preview_image.update_image( item )
				
				elif check_filetype in [ "ma", "mb" ]:
					self.preview_image.update_image( maya_icon )
				
				else:
					self.preview_image.update_image( ":objectSet.svg" )
			else:
				self.preview_image.update_image( folder_icon )
	
	# ============================================================
	# Snapshot
	# ============================================================
	
	def snapshot(self):
		
		item = self.item_tree_view.current_item
		item_name = os.path.basename(item)
		if os.path.isfile(item):
			item_name = item_name.split(".")[0]
		
		path = self.setting_widget.default_imagesPath_le.text()
		width = int(self.setting_widget.width_le.text())
		height = int(self.setting_widget.height_le.text())
		image_format = self.setting_widget.image_format_cb.currentText()
		show_mesh = self.setting_widget.show_mesh_ck.isChecked()
		show_joint = self.setting_widget.show_joint_ck.isChecked()
		show_curve = self.setting_widget.show_curve_ck.isChecked()
		
		take_screenshot(
			output = path,
			name = item_name,
			width = width,
			height = height,
			img_format = image_format,
			show_poly = show_mesh,
			show_joint = show_joint,
			show_curve = show_curve
		)
		
		message = QtWidgets.QMessageBox()
		message.warning(
			self,
			"Warning",
			'Capture screen done!'
		)
	
	# ============================================================
	# About
	# ============================================================
	
	def about_widget( self ):
		
		msgBox = QtWidgets.QMessageBox(self)
		msgBox.setStyleSheet("QLabel{min-width: 400px;}");
		msgBox.setWindowTitle("About")
		msgBox.setText("Asset Viewer version 1.1.0\nFacebook page : https://www.facebook.com/Faruq00-110307125021792")
		msgBox.show()

# ============================================================