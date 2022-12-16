##### insert file name widget
# ============================================================

import PySide2.QtWidgets as qw
import PySide2.QtCore as qc

# ============================================================

class insertFileNameWidget( qw.QWidget ):
	
	def __init__( self, parent = None, windowTitle = "title", newName = "" ):
		
		self.newName = newName
		
		super( insertFileNameWidget, self ).__init__( parent)
		
		self.setWindowTitle( windowTitle )
		self.setWindowFlags( qc.Qt.WindowType.Window )
		
		self.create_widgets()
		self.create_layouts()
		self.create_connections()
		
		self.resize( 300, 1 )
	
	def create_widgets( self ):
		
		self.fileName_le 	= qw.QLineEdit()
		self.outputPath_le	= qw.QLineEdit()
		self.create_btn 	= qw.QPushButton( "Create" )
	
	def create_layouts( self ):
		
		# create main layout
		main_layout = qw.QVBoxLayout( self )
		main_layout.setSpacing( 1 )
		main_layout.setContentsMargins( 3, 3, 3, 3 )
		
		info_formLayout = qw.QFormLayout()
		info_formLayout.addRow( self.newName, self.fileName_le )
		info_formLayout.addRow( "Output path : ", self.outputPath_le )
		
		main_layout.addLayout( info_formLayout )
		main_layout.addWidget( self.create_btn )
	
	def create_connections( self ):
		pass

# ============================================================