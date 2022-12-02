# pyside2
import sys

import PySide2.QtWidgets as QtWidgets
import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui

import maya.cmds as cmds
import maya.OpenMayaUI as omui

from shiboken2 import wrapInstance, getCppPointer

# ============================================================

def maya_main_window():
	"""
	Return the Maya main window widget as a Python object
	"""
	main_window_ptr = omui.MQtUtil.mainWindow()
	if sys.version_info.major >= 3:
		return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
	else:
		return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

def undo(func):
    def wrapper(*args, **kwargs):
        cmds.undoInfo(openChunk=True)
        try:
            ret = func(*args, **kwargs)
        finally:
            cmds.undoInfo(closeChunk=True)
        return ret
    return wrapper

class WorkspaceControl(object):
	
	def __init__(self, name):
		self.name = name
		self.widget = None
	
	def create(self, label, widget, ui_script=None):
		
		cmds.workspaceControl(self.name, label=label)
		
		if ui_script:
			cmds.workspaceControl(self.name, e=True, uiScript=ui_script)
		
		self.add_widget_to_layout(widget)
		self.set_visible(True)
	
	def restore(self, widget):
		self.add_widget_to_layout(widget)
	
	def add_widget_to_layout(self, widget):
		if widget:
			self.widget = widget
			self.widget.setAttribute(QtCore.Qt.WA_DontCreateNativeAncestors)
		
			if sys.version_info.major >= 3:
				workspace_control_ptr = int(omui.MQtUtil.findControl(self.name))
				widget_ptr = int(getCppPointer(self.widget)[0])
			else:
				workspace_control_ptr = int(omui.MQtUtil.findControl(self.name))
				widget_ptr = int(getCppPointer(self.widget)[0])
			
			omui.MQtUtil.addWidgetToMayaLayout(widget_ptr, workspace_control_ptr)
	
	def exists(self):
		return cmds.workspaceControl(self.name, q=True, exists=True)
	
	def is_visible(self):
		return cmds.workspaceControl(self.name, q=True, visible=True)
	
	def set_visible(self, visible):
		if visible:
			cmds.workspaceControl(self.name, e=True, restore=True)
		
		else:
			cmds.workspaceControl(self.name, e=True, visible=False)
	
	def set_label(self, label):
		cmds.workspaceControl(self.name, e=True, label=label)
	
	def is_floating(self):
		return cmds.workspaceControl(self.name, q=True, floating=True)
	
	def is_collapsed(self):
		return cmds.workspaceControl(self.name, q=True, collapse=True)

class tabWidget( QtWidgets.QWidget ):
	
	def __init__( self, parent = None ):
		super( tabWidget, self ).__init__( parent )
		
		self.create_widgets()
		self.create_layout()
		self.create_connections()
	
	def create_widgets(self):
		self.tab_bar = QtWidgets.QTabBar()
		self.tab_bar.setObjectName( "customTabBar" )
		self.tab_bar.setStyleSheet( "#customTabBar {background-color: #383838}")
		
		self.stacked_wdg = QtWidgets.QStackedWidget()
		self.stacked_wdg.setObjectName( "tabBarStackedWidget" )
		self.stacked_wdg.setStyleSheet( "#tabBarStackedWidget {border: 1px solid #2e2e2e}" )
	
	def create_layout(self):
		main_layout = QtWidgets.QVBoxLayout(self)
		main_layout.setContentsMargins(0, 0, 0, 0)
		main_layout.setSpacing(0)
		main_layout.addWidget(self.tab_bar)
		main_layout.addWidget(self.stacked_wdg)
	
	def create_connections(self):
		self.tab_bar.currentChanged.connect( self.stacked_wdg.setCurrentIndex )
	
	def addTab( self, label, widget ):
		self.tab_bar.addTab( label )
		
		self.stacked_wdg.addWidget(widget)

class imageWidget( QtWidgets.QLabel ):
	
	def __init__( self, image, width = 300, parent = None ):
		
		super( imageWidget, self ).__init__( parent )
		self.width = width
		self.update_image( image )
	
	def update_image( self, image ):
		self.pixmap = QtGui.QPixmap( image )
		
		self.pixmap = self.pixmap.scaledToWidth(self.width)
		
		self.setPixmap(self.pixmap)

class intLineEdit( QtWidgets.QLineEdit ):
	
	def __init__( self, parent = None ):
		
		super( intLineEdit, self ).__init__( parent )
		
		reg_ex = QtCore.QRegExp( '[0-9]+' )
		text_validator = QtGui.QRegExpValidator( reg_ex, self )
		self.setValidator( text_validator )

class customTreeView( QtWidgets.QTreeView ):

    current_item = None

    def __init__( self, root_dir ):
        super( customTreeView, self ).__init__()
		
        self.root_dir = root_dir
        self.current_item = ""
		
        self.create_menu()
		
        self.thismodel = QtWidgets.QFileSystemModel()
        self.update_root( root_dir = root_dir )
		
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect( self.open_menu )
		
        ## custom keypressed event
        collapseKey = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Shift+A"), self )
        collapseKey.activated.connect(self.collapseAll)
		
        self.pressed.connect( self.update_current_item )
    
    def update_root( self, root_dir ):
		
        self.thismodel.setRootPath( root_dir)
        self.thismodel.setFilter( QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllEntries | QtCore.QDir.Dirs | QtCore.QDir.Files )
		
        self.filter_proxy_model = QtCore.QSortFilterProxyModel( filterRole = QtWidgets.QFileSystemModel.FileNameRole )
        self.filter_proxy_model.setSourceModel( self.thismodel )
		
        self.setModel(self.filter_proxy_model)
        self.root_dir = root_dir
        self.adjust_root()
    
    def adjust_root( self ):
        root_index = self.thismodel.index( self.root_dir )
        proxy_index = self.filter_proxy_model.mapFromSource(root_index)
        self.setRootIndex(proxy_index)
    #
    @QtCore.Slot(QtCore.QModelIndex)
    def update_current_item( self, index ):
        
        source_index = self.filter_proxy_model.mapToSource(index)
        indexItem = self.thismodel.index(source_index.row(), 0, source_index.parent())
        filePath = self.thismodel.filePath(indexItem)
        self.current_item = filePath
    #
    # ==================================================
    
    def expand_selected_item( self ):
        self.expandRecursively( self.selectionModel().selectedRows()[0] )
    
    def collapse_selected_item( self ):
        self.collapse( self.selectionModel().selectedRows()[0] )
    
    def create_menu( self ):
        
        self.menu = QtWidgets.QMenu( self )
        
        action_1 = self.menu.addAction("Expand")
        action_2 = self.menu.addAction("Expand All")
        action_3 = self.menu.addAction("Collapse")
        action_4 = self.menu.addAction("Collapse All")

        action_1.triggered.connect( self.expand_selected_item )
        action_2.triggered.connect( self.expandAll )
        action_3.triggered.connect( self.collapse_selected_item )
        action_4.triggered.connect( self.collapseAll )

    def open_menu( self, position ):
        index = self.indexAt(position)
        if not index.isValid():
            return
        self.menu.exec_(self.mapToGlobal(position))

# ============================================================