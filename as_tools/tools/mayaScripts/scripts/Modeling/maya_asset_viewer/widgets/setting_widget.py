# setting widget
# ============================================================

import os
import json
import getpass

import PySide2.QtWidgets as QtWidgets
import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui

from maya_asset_viewer.widgets.pyside2_helper 			import maya_main_window, tabWidget, intLineEdit
from maya_asset_viewer.widgets.insert_fileName_widget 	import insertFileNameWidget
from maya_asset_viewer.modules.create_config			import create_progress_update_config
from maya_asset_viewer.modules.widget_functions			import open_window_explorer

# ============================================================
USERNAME 	= getpass.getuser()
OUTPUT_PATH 	= "C:/Users/{}/Documents/maya/scripts".format( USERNAME )

CONFIG_PATH = os.path.join( OUTPUT_PATH, "assetViewer.json" )
# ============================================================
# get icon
SCRIPT_PATH = __file__
ICON_PATH = SCRIPT_PATH.split( "\\widgets" )[0]
ICON_PATH = os.path.join( ICON_PATH, "icons" )
ICON_PATH = ICON_PATH.replace( "\\", "/" )

addBookmark_icon = ICON_PATH + "/addBookmark.png"
removeBookmark_icon = ICON_PATH + "/removeBookmark.png"
editBookmark_icon = ICON_PATH + "/editBookmark.png"
# ============================================================

class settingWidget( QtWidgets.QWidget ):
	
	def __init__( self, parent = maya_main_window() ):
		
		super( settingWidget, self ).__init__( parent)
		
		self.setWindowTitle( "Setting" )
		self.setWindowFlags( QtCore.Qt.WindowType.Window )
		
		self.create_widgets()
		self.create_layouts()
		self.create_connections()
		
		self.resize( 400, 1 )
		try:
			self.load_config()
		except:
			self.update_config()
			self.load_config()
	
	# ============================================================
	
	def create_widgets( self ):
		
		# widget setting
		self.default_path_le 		= QtWidgets.QLineEdit()
		self.find_default_path_btn	= QtWidgets.QPushButton("...")
		self.open_default_path_btn	= QtWidgets.QPushButton()
		self.default_imagesPath_le 	= QtWidgets.QLineEdit()
		self.find_imagesPath_btn	= QtWidgets.QPushButton("...")
		self.open_imagesPath_btn	= QtWidgets.QPushButton()
		self.show_bookmark_cb 		= QtWidgets.QCheckBox( "Show bookmark" )
		self.show_previewImage_cb 	= QtWidgets.QCheckBox( "Show preview image" )
		self.show_quickSave_cb 		= QtWidgets.QCheckBox( "Show quick save" )
		self.show_channelBox_cb 	= QtWidgets.QCheckBox( "Show Channel Box" )
		self.ask_before_delete_cb	= QtWidgets.QCheckBox( "Double warning before delete" )
		# set widget setting widgets
		self.open_default_path_btn.setIcon(QtGui.QIcon(":folder-open.png"))
		self.open_default_path_btn.setIconSize(QtCore.QSize(18, 18))
		self.open_imagesPath_btn.setIcon(QtGui.QIcon(":folder-open.png"))
		self.open_imagesPath_btn.setIconSize(QtCore.QSize(18, 18))
		
		# project template
		self.new_folder_le		= QtWidgets.QLineEdit()
		self.add_new_folder_btn	= QtWidgets.QPushButton()
		self.remove_folder_btn	= QtWidgets.QPushButton()
		self.folder_list = QtWidgets.QListWidget()
		self.date_folder_format = QtWidgets.QLineEdit()
		# set project template widgets
		self.new_folder_le.setPlaceholderText( "new folder template" )
		self.date_folder_format.setPlaceholderText( "yyyymmdd" )
		self.add_new_folder_btn.setIcon(QtGui.QIcon(":addClip.png"))
		self.add_new_folder_btn.setIconSize(QtCore.QSize(18, 18))
		self.remove_folder_btn.setIcon(QtGui.QIcon(":trash.png"))
		self.remove_folder_btn.setIconSize(QtCore.QSize(18, 18))
		
		# bookmark
		self.addBookmark_btn			= QtWidgets.QPushButton()
		self.editBookmark_btn			= QtWidgets.QPushButton()
		self.removeBookmark_btn			= QtWidgets.QPushButton()
		self.bookmark_list = QtWidgets.QListWidget()
		self.editBookmarkWidget = insertFileNameWidget( parent = self, windowTitle = "Edit Bookmark", newName = "Bookmark name : " )
		self.editBookmarkWidget.create_btn.setText( "Edit" )
		# set bookmark widgets
		self.addBookmark_btn.setIcon(QtGui.QIcon(addBookmark_icon))
		self.addBookmark_btn.setIconSize(QtCore.QSize(18, 18))
		self.editBookmark_btn.setIcon(QtGui.QIcon(editBookmark_icon))
		self.editBookmark_btn.setIconSize(QtCore.QSize(18, 18))
		self.removeBookmark_btn.setIcon(QtGui.QIcon(removeBookmark_icon))
		self.removeBookmark_btn.setIconSize(QtCore.QSize(18, 18))
		
		# quick save
		self.new_progressType_le		= QtWidgets.QLineEdit()
		self.add_new_progressType_btn	= QtWidgets.QPushButton()
		self.remove_progressType_btn	= QtWidgets.QPushButton()
		self.progressType_list = QtWidgets.QListWidget()
		# set quick save widgets
		self.new_progressType_le.setPlaceholderText( "new type" )
		self.add_new_progressType_btn.setIcon(QtGui.QIcon(":addClip.png"))
		self.add_new_progressType_btn.setIconSize(QtCore.QSize(18, 18))
		self.remove_progressType_btn.setIcon(QtGui.QIcon(":trash.png"))
		self.remove_progressType_btn.setIconSize(QtCore.QSize(18, 18))
		
		# snapshot
		self.width_le = intLineEdit()
		self.height_le = intLineEdit()
		self.image_format_cb = QtWidgets.QComboBox()
		self.image_format_cb.addItem("jpg")
		self.image_format_cb.addItem("png")
		self.show_mesh_ck = QtWidgets.QCheckBox("Show Polymeshes")
		self.show_joint_ck = QtWidgets.QCheckBox("Show Joints")
		self.show_curve_ck = QtWidgets.QCheckBox("Show Nurbs Curves")
		
		
		self.save_config_btn = QtWidgets.QPushButton( "Save Setting" )
		self.save_config_btn.setIcon(QtGui.QIcon(":save.png"))
		self.save_config_btn.setStyleSheet( "background-color:rgb(245, 190, 40);color:Black" )
		
	
	def create_layouts( self ):
		
		main_layout = QtWidgets.QVBoxLayout( self )
		main_layout.setSpacing( 1 )
		main_layout.setContentsMargins( 5, 5, 5, 5 )
		
		# tab
		main_tab = tabWidget()
		
		# widget setting
		wdgSetting_wdg = QtWidgets.QWidget()
		wdgSetting_layout = QtWidgets.QVBoxLayout( wdgSetting_wdg )
		wdgSetting_layout.setSpacing( 1 )
		wdgSetting_layout.setContentsMargins( 5, 5, 5, 5 )
		# default path layout
		defaultPath_layout = QtWidgets.QHBoxLayout()
		defaultPath_layout.addWidget( self.default_path_le )
		defaultPath_layout.addWidget( self.find_default_path_btn )
		defaultPath_layout.addWidget( self.open_default_path_btn )
		# default images path layout
		defaultImagesPath_layout = QtWidgets.QHBoxLayout()
		defaultImagesPath_layout.addWidget( self.default_imagesPath_le )
		defaultImagesPath_layout.addWidget( self.find_imagesPath_btn )
		defaultImagesPath_layout.addWidget( self.open_imagesPath_btn )
		# form layout
		defaultPath_formLayout = QtWidgets.QFormLayout()
		defaultPath_formLayout.addRow( "default path : ", defaultPath_layout )
		defaultPath_formLayout.addRow( " images path : ", defaultImagesPath_layout )
		# add into widget setting layout
		wdgSetting_layout.addLayout( defaultPath_formLayout )
		wdgSetting_layout.addWidget( self.show_bookmark_cb )
		wdgSetting_layout.addWidget( self.show_previewImage_cb )
		wdgSetting_layout.addWidget( self.show_quickSave_cb )
		wdgSetting_layout.addWidget( self.show_channelBox_cb )
		wdgSetting_layout.addWidget( self.ask_before_delete_cb )
		wdgSetting_layout.addStretch()
		
		# project template
		prjTemplate_wdg = QtWidgets.QWidget()
		prjTemplate_layout = QtWidgets.QVBoxLayout( prjTemplate_wdg )
		prjTemplate_layout.setSpacing( 1 )
		prjTemplate_layout.setContentsMargins( 5, 5, 5, 5 )
		# add new progress type layout
		add_folder_layout = QtWidgets.QHBoxLayout()
		add_folder_layout.addWidget( self.new_folder_le )
		add_folder_layout.addWidget( self.add_new_folder_btn )
		add_folder_layout.addWidget( self.remove_folder_btn )
		# add into project template layout
		prjTemplate_layout.addLayout( add_folder_layout )
		prjTemplate_layout.addWidget( self.folder_list )
		#prjTemplate_layout.addWidget( self.date_folder_format )
		
		# bookmark
		bookmark_wdg = QtWidgets.QWidget()
		bookmark_layout = QtWidgets.QVBoxLayout( bookmark_wdg )
		bookmark_layout.setSpacing( 1 )
		bookmark_layout.setContentsMargins( 5, 5, 5, 5 )
		# bookmark button layout
		bookmark_btn_layout = QtWidgets.QHBoxLayout()
		bookmark_btn_layout.addWidget( self.addBookmark_btn )
		bookmark_btn_layout.addWidget( self.editBookmark_btn )
		bookmark_btn_layout.addWidget( self.removeBookmark_btn )
		# add into bookmark layout
		bookmark_layout.addWidget( self.bookmark_list )
		bookmark_layout.addLayout( bookmark_btn_layout )
		#
		self.add_bookmark_widget()
		
		# quick save
		quickSave_wdg = QtWidgets.QWidget()
		quickSave_layout = QtWidgets.QVBoxLayout( quickSave_wdg )
		quickSave_layout.setSpacing( 1 )
		quickSave_layout.setContentsMargins( 5, 5, 5, 5 )
		# add new progress type layout
		add_progress_layout = QtWidgets.QHBoxLayout()
		add_progress_layout.addWidget( self.new_progressType_le )
		add_progress_layout.addWidget( self.add_new_progressType_btn )
		add_progress_layout.addWidget( self.remove_progressType_btn )
		# add into quick save layout
		quickSave_layout.addLayout( add_progress_layout )
		quickSave_layout.addWidget( self.progressType_list )
		
		# snapshot
		snapshot_wdg = QtWidgets.QWidget()
		snapshot_layout = QtWidgets.QVBoxLayout(snapshot_wdg)
		snapshot_layout.setSpacing( 1 )
		snapshot_layout.setContentsMargins( 5, 5, 5, 5 )
		# set width height
		weightHeight_layout = QtWidgets.QFormLayout()
		weightHeight_layout.addRow("Width : ", self.width_le)
		weightHeight_layout.addRow("Height : ", self.height_le)
		weightHeight_layout.addRow("Format : ", self.image_format_cb)
		# add snapshot layout
		snapshot_layout.addLayout(weightHeight_layout)
		snapshot_layout.addWidget(self.show_mesh_ck)
		snapshot_layout.addWidget(self.show_joint_ck)
		snapshot_layout.addWidget(self.show_curve_ck)
		snapshot_layout.addStretch()
		
		main_tab.addTab( "Main", wdgSetting_wdg )
		main_tab.addTab( "Project Template", prjTemplate_wdg )
		main_tab.addTab( "Bookmark", bookmark_wdg )
		main_tab.addTab( "Quick save", quickSave_wdg )
		main_tab.addTab( "Snapshot", snapshot_wdg )
		
		main_layout.addWidget( main_tab )
		main_layout.addWidget( self.save_config_btn )
	
	def create_connections( self ):
		
		self.save_config_btn.clicked.connect( self.save_config_setting_wdg )
		
		self.find_default_path_btn.clicked.connect( self.find_new_default_path )
		self.find_imagesPath_btn.clicked.connect( self.find_new_previewImages_path )
		self.open_default_path_btn.clicked.connect(self.open_default_path)
		self.open_imagesPath_btn.clicked.connect(self.open_images_path)
		
		# add btn
		self.add_new_folder_btn.clicked.connect( self.add_folderTemplate )
		self.add_new_progressType_btn.clicked.connect( self.add_progressType )
		self.addBookmark_btn.clicked.connect( self.addBookmark_widget.show )
		self.editBookmark_btn.clicked.connect( self.show_edit_bookmark_widget )
		self.editBookmarkWidget.create_btn.clicked.connect( self.edit_bookmark )
		self.editBookmarkWidget.create_btn.clicked.connect( self.editBookmarkWidget.close )
		# remove btn
		self.remove_folder_btn.clicked.connect( self.remove_select_folderTemplate )
		self.remove_progressType_btn.clicked.connect( self.remove_select_progressType )
		self.removeBookmark_btn.clicked.connect( self.remove_select_bookmark )
	
	def closeEvent(self, event):
		self.addBookmark_widget.close()
	
	# ============================================================
	# Config
	# ============================================================
	
	def load_config( self ):
		
		check_config_file = os.path.isfile( CONFIG_PATH )
		if check_config_file == False:
			create_progress_update_config()
		
		with open(CONFIG_PATH, 'r') as f:
			config = json.load(f)
			default_path 		= config["defaultPath"]
			preview_images_path	= config["previewImagePath"]
			showBookmarkBar 	= config["showBookmarkBar"]
			showPreviewImageBar = config["showPreviewImageBar"]
			showQuickSaveBar 	= config["showQuickSaveBar"]
			showChannelBox	 	= config["showChannelBox"]
			doubleWarningDelete = config["doubleWarningDelete"]
			projectTemplate 	= config["projectTemplate"]
			dateFolderFormat 	= config["dateFolderFormat"]
			bookmark 			= config["bookmark"]
			quickSaveType 		= config["quickSaveType"]
			width 				= config["width"]
			height 				= config["height"]
			image_format 		= config["imageFormat"]
			show_mesh 			= config["showMesh"]
			show_joint 			= config["showJoint"]
			show_curve 			= config["showCurve"]
		
		# main
		self.default_path_le.setText( default_path )
		self.default_imagesPath_le.setText( preview_images_path )
		# check box
		self.show_bookmark_cb.setChecked( showBookmarkBar )
		self.show_previewImage_cb.setChecked( showPreviewImageBar )
		self.show_quickSave_cb.setChecked( showQuickSaveBar )
		self.show_channelBox_cb.setChecked( showChannelBox )
		self.ask_before_delete_cb.setChecked( doubleWarningDelete )
		
		# project template
		self.folder_list.clear()
		self.date_folder_format.setText( dateFolderFormat )
		for fld in projectTemplate:
			self.folder_list.addItem( fld )
		
		# bookmark
		self.bookmark_list.clear()
		for name, path in bookmark:
			list_wdg_item = QtWidgets.QListWidgetItem(name)
			list_wdg_item.setData( QtCore.Qt.UserRole, path )
			self.bookmark_list.addItem( list_wdg_item )
		
		# quick save
		self.progressType_list.clear()
		for qst in quickSaveType:
			self.progressType_list.addItem( qst )
		
		# snapshot
		self.width_le.setText(width)
		self.height_le.setText(height)
		if image_format == "png":
			self.image_format_cb.setCurrentIndex(1)
		else:
			self.image_format_cb.setCurrentIndex(0)
		self.show_mesh_ck.setChecked(show_mesh)
		self.show_joint_ck.setChecked(show_joint)
		self.show_curve_ck.setChecked(show_curve)
	
	def save_config( self ):
		
		# update main
		default_path 		= self.default_path_le.text()
		previewImages_path 	= self.default_imagesPath_le.text()
		# check box
		show_bookmark 			= self.show_bookmark_cb.isChecked()
		show_preview_image 		= self.show_previewImage_cb.isChecked()
		show_quickSave 			= self.show_quickSave_cb.isChecked()
		showChannelBox 			= self.show_channelBox_cb.isChecked()
		double_warning_delete 	= self.ask_before_delete_cb.isChecked()
		
		# update project template
		date_folder_format = self.date_folder_format.text()
		project_template = []
		count = self.folder_list.count()
		for n in range( count ):
			# set index
			currennt_item = self.folder_list.item(n)
			project_template.append( currennt_item.text() )
		
		# update bookmark
		bookmark = []
		count = self.bookmark_list.count()
		for n in range( count ):
			# set index
			currennt_item = self.bookmark_list.item(n)
			name = currennt_item.text()
			path = currennt_item.data(QtCore.Qt.UserRole)
			bookmark.append( [ name, path ] )
		
		# update quick save
		quick_save_type = []
		count = self.progressType_list.count()
		for n in range( count ):
			# set index
			currennt_item = self.progressType_list.item(n)
			quick_save_type.append( currennt_item.text() )
		
		# update snapshot
		width = self.width_le.text()
		height = self.height_le.text()
		image_format = self.image_format_cb.currentText()
		show_mesh = self.show_mesh_ck.isChecked()
		show_joint = self.show_joint_ck.isChecked()
		show_curve = self.show_curve_ck.isChecked()
		
		config = {
			"defaultPath": default_path,
			"previewImagePath" : previewImages_path,
			"showBookmarkBar" : show_bookmark,
			"showPreviewImageBar" : show_preview_image,
			"showQuickSaveBar" : show_quickSave,
			"showChannelBox" : showChannelBox,
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
		
		with open(CONFIG_PATH, 'w') as f:
			json.dump(config, f)
	
	def save_config_setting_wdg( self ):
		
		self.save_config()
		
		message = QtWidgets.QMessageBox()
		message.warning(
			self,
			"Warning",
			'Save config done'
		)
		self.close()
	
	# update config from v1.0.0 to v1.1.0
	def update_config(self):
		with open(CONFIG_PATH, 'r') as f:
			config = json.load(f)
			config.update({"width" : "300"})
			config.update({"height" : "300"})
			config.update({"imageFormat" : "jpg"})
			config.update({"showMesh" : True})
			config.update({"showJoint" : False})
			config.update({"showCurve" : False})
		
		with open(CONFIG_PATH, 'w') as f:
			json.dump(config, f)
	
	# ============================================================
	
	def open_default_path(self):
		
		path = self.default_path_le.text()
		open_window_explorer(item = path)
	
	def open_images_path(self):
		
		path = self.default_imagesPath_le.text()
		open_window_explorer(item = path)
	
	def find_new_default_path( self ):

		file_dialog = QtWidgets.QFileDialog()
		file_dir = file_dialog.getExistingDirectory(
						parent = self,
						caption = "Select directory"
					)

		if file_dir != "":
			self.default_path_le.setText( file_dir )
	
	def find_new_previewImages_path( self ):

		file_dialog = QtWidgets.QFileDialog()
		file_dir = file_dialog.getExistingDirectory(
						parent = self,
						caption = "Select directory"
					)

		if file_dir != "":
			self.default_imagesPath_le.setText( file_dir )
	
	# ============================================================
	
	def add_folderTemplate( self ):
		new_template = self.new_folder_le.text()
		self.folder_list.addItem( new_template )
	
	def add_progressType( self ):
		new_progress = self.new_progressType_le.text()
		self.progressType_list.addItem( new_progress )
	
	def remove_select_folderTemplate( self ):
		
		currentItem = self.folder_list.currentItem()
		self.folder_list.takeItem(self.folder_list.row(currentItem))
	
	def remove_select_progressType( self ):
		
		currentItem = self.progressType_list.currentItem()
		self.progressType_list.takeItem(self.progressType_list.row(currentItem))
	
	def remove_select_bookmark( self ):
		
		currentItem = self.bookmark_list.currentItem()
		self.bookmark_list.takeItem(self.bookmark_list.row(currentItem))
	
	# ============================================================
		
	def add_bookmark_widget( self ):
		
		# create widget window
		self.addBookmark_widget = QtWidgets.QWidget( self )
		self.addBookmark_widget.setWindowTitle( "Add Bookmark" )
		self.addBookmark_widget.setWindowFlags( QtCore.Qt.WindowType.Window )
		self.addBookmark_widget.resize( 400, 1 )
		# create widget
		self.bookmark_name = QtWidgets.QLineEdit()
		self.bookmark_path = QtWidgets.QLineEdit()
		search_path_btn = QtWidgets.QPushButton()
		self.add_btn = QtWidgets.QPushButton( "Add" )
		
		search_path_btn.setIcon(QtGui.QIcon(":folder-open.png"))
		search_path_btn.setIconSize(QtCore.QSize(18, 18))
		# create layout
		path_layout = QtWidgets.QHBoxLayout()
		path_layout.addWidget( self.bookmark_path )
		path_layout.addWidget( search_path_btn )
		form_layout = QtWidgets.QFormLayout()
		form_layout.addRow( "name : ", self.bookmark_name )
		form_layout.addRow( "path : ", path_layout )
		layout = QtWidgets.QVBoxLayout( self.addBookmark_widget )
		layout.addLayout( form_layout )
		layout.addWidget( self.add_btn )
		
		search_path_btn.clicked.connect( self.insert_bookmark_path )
		self.add_btn.clicked.connect( self.add_bookmark )
		self.add_btn.clicked.connect( self.addBookmark_widget.close )
	
	def insert_bookmark_path( self ):

		file_dialog = QtWidgets.QFileDialog()
		file_dir = file_dialog.getExistingDirectory(
						parent = self,
						caption = "Select directory"
					)

		if file_dir != "":
			self.bookmark_path.setText( file_dir )
	
	def add_bookmark( self ):
		
		name = self.bookmark_name.text()
		path = self.bookmark_path.text()
		
		# clear line
		self.bookmark_name.setText("")
		self.bookmark_path.setText("")
		
		list_wdg_item = QtWidgets.QListWidgetItem(name)
		list_wdg_item.setData(QtCore.Qt.UserRole, path)
		self.bookmark_list.addItem( list_wdg_item )
		
	def show_edit_bookmark_widget( self ):
		
		currennt_item = self.bookmark_list.currentItem()
		item = currennt_item.data(QtCore.Qt.UserRole)
		
		self.editBookmarkWidget.fileName_le.setText( currennt_item.text() )
		self.editBookmarkWidget.outputPath_le.setText( item )
		self.editBookmarkWidget.show()
	
	def edit_bookmark( self ):
		
		new_name = self.editBookmarkWidget.fileName_le.text()
		new_path = self.editBookmarkWidget.outputPath_le.text()
		
		currennt_item = self.bookmark_list.currentItem()
		currennt_item.setText( new_name )
		currennt_item.setData(QtCore.Qt.UserRole, new_path )

# ============================================================