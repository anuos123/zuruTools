import logging
import os,sys
import json
import PySide2.QtWidgets as QtWidgets
import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui
import shutil
import maya.cmds as cmds
from datetime import date
from shiboken2 import wrapInstance
from maya import OpenMayaUI as omui
import importlib

#library config
from . import config
current_path = os.path.abspath(os.path.dirname(__file__))
config_json = os.path.abspath(os.path.join(current_path,'config.json'))
template_json = os.path.abspath(os.path.join(current_path,'template.json'))
project_path = config.project_path

# noinspection PyInterpreter
def getMainWindowPtr():
    prt = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(prt), QtWidgets.QWidget)
    return mayaMainWindow

class asset_window(QtWidgets.QMainWindow):
    WINDOW_TITLE = "Asset Library"
    UI_NAME = "assetUI"

    def __init__(self, parent = getMainWindowPtr()):
        super(asset_window, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        self.setWindowFlags(QtCore.Qt.WindowType.Window)
        self.resize(1080,720)

        self.createMenuBar()

        self.main_layout =  QtWidgets.QVBoxLayout()

        self.asset_name_layout = QtWidgets.QHBoxLayout()
        self.asset_view_layout = QtWidgets.QHBoxLayout()
        self.asset_type_layout = QtWidgets.QVBoxLayout()
        self.asset_update_layout = QtWidgets.QVBoxLayout()

        self.asset_widget = QtWidgets.QWidget()
        self.asset_widget_layout = QtWidgets.QGridLayout()
        self.asset_widget.setLayout(self.asset_widget_layout)

        self.asset_scroll = QtWidgets.QScrollArea()
        self.asset_scroll.setWidget(self.asset_widget)
        self.load_image_to_layout()
        self.asset_scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.asset_scroll.setWidgetResizable(True)

        self.asset_mods_riubut = QtWidgets.QRadioButton('Mods')
        self.asset_rigs_riubut = QtWidgets.QRadioButton('Rigs')
        self.asset_seek_line = QtWidgets.QLineEdit()
        self.asset_seek_line.setPlaceholderText('Enter text content!')

        self.aseet_all_cb = QtWidgets.QCheckBox('All')
        self.aseet_char_cb = QtWidgets.QCheckBox('Char')
        self.aseet_prop_cb = QtWidgets.QCheckBox('Prop')
        self.aseet_envs_cb = QtWidgets.QCheckBox('Envs')

        self.asset_update_bnt = QtWidgets.QPushButton('Submit')

        self.asset_name_layout.addWidget(self.asset_mods_riubut)
        self.asset_name_layout.addWidget(self.asset_rigs_riubut)
        self.asset_name_layout.addWidget(self.asset_seek_line)

        self.asset_type_layout.addWidget(self.aseet_all_cb)
        self.asset_type_layout.addWidget(self.aseet_char_cb)
        self.asset_type_layout.addWidget(self.aseet_prop_cb)
        self.asset_type_layout.addWidget(self.aseet_envs_cb)

        self.asset_mods_riubut.setChecked(True)

        self.asset_update_layout.addWidget(self.asset_update_bnt)

        self.aseet_all_cb.stateChanged.connect(self.all_asset)
        self.asset_seek_line.editingFinished.connect(self.asset_seek)

        self.asset_update_bnt.clicked.connect(self.asset_submit)

        self.main_layout.addLayout(self.asset_name_layout)
        self.main_layout.addLayout(self.asset_view_layout)
        self.main_layout.addLayout(self.asset_update_layout)


        self.asset_view_layout.addLayout(self.asset_type_layout)
        self.asset_view_layout.addWidget(self.asset_scroll)


        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(self.main_layout)
        self.setCentralWidget(main_widget)


    def createMenuBar(self):
        # create menu bar
        menuBar = QtWidgets.QMenuBar(self)
        self.setMenuBar(menuBar)

        fileMenu = QtWidgets.QMenu("&File")
        menuBar.addMenu(fileMenu)

        helpMenu = QtWidgets.QMenu("&Help")
        menuBar.addMenu(helpMenu)

        preferences_ac = QtWidgets.QAction("Create Asset", fileMenu)
        fileMenu.addAction(preferences_ac)

        about_ac = QtWidgets.QAction("About", helpMenu)
        helpMenu.addAction(about_ac)

        # create connections
        preferences_ac.triggered.connect(self.show_asset_widget)
        # about_ac.triggered.connect(self.about_widget)

    def all_asset(self):
        if self.aseet_all_cb.checkState() == QtCore.Qt.Checked:
            self.aseet_char_cb.setChecked(True)
            self.aseet_prop_cb.setChecked(True)
            self.aseet_envs_cb.setChecked(True)
            print('all')

        elif self.aseet_all_cb.checkState() == QtCore.Qt.Unchecked:
            self.aseet_char_cb.setChecked(False)
            self.aseet_prop_cb.setChecked(False)
            self.aseet_envs_cb.setChecked(False)

    def load_image_to_layout(self):
        image_list = []
        with open(config_json) as f:
            result = json.load(f)
        asset_name = result.get("asset")
        type_name = result.get("type")
        file_path = os.path.abspath(os.path.join(project_path, asset_name, type_name))
        for root,dirs,files in os.walk(file_path):
            for file in files:
                if ".png" in file:
                    image_list.append(os.path.join(root,file))

        row = -1
        column = 0
        coordineteList = []
        for index in range(len(image_list)):
            if index%5:
                column +=1
                coordineteList.append([row,column])
            else:
                row+=1
                column=0
                coordineteList.append([row, column])

        for i in range(len(image_list)):
            print(image_list[i])
            self.toolButton = MyQToolButton()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(image_list[i]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton.setIcon(icon)
            self.toolButton.setIconSize(QtCore.QSize(100, 100))
            npg_path = os.path.basename(image_list[i]).split('.')[0]
            self.toolButton.setObjectName('toolButton_{}'.format(npg_path))
            self.toolButton.setText('{}'.format(npg_path))

            self.asset_widget_layout.addWidget(self.toolButton,coordineteList[i][0],coordineteList[i][1],1,1)

    def load_file_path(self):
        file_list = []
        with open(config_json) as f:
            result = json.load(f)
        asset_name = result.get("asset")
        type_name = result.get("type")
        file_path = os.path.abspath(os.path.join(project_path, asset_name, type_name))
        for root,dirs,files in os.walk(file_path):
            for file in files:
                file_list.append(file)

        return file_list

    def button_press(self):
        print(self.toolButton.btext())

    def asset_seek(self):
        print(self.asset_seek_line.text())
        self.load_image_to_layout()

    def asset_submit(self):
        print('asset_submit')


    def show_asset_widget(self):
        from . import create_aseet_window
        importlib.reload(create_aseet_window)
        global cs_win
        try:
            cs_win.close()
        except:
            pass
        cs_win = create_aseet_window.create_asset_window()
        cs_win.show()
        #self.load_image_to_layout()

class MyQToolButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        menu = QtWidgets.QMenu()
        menu.addAction('>>>Open File', self.open_file)
        menu.addAction('>>>Import File', self.import_file)
        menu.addAction('>>>Reference File', self.reference_file)
        menu.addAction('>>>ReMove File', self.remove_file)
        menu.addAction('>>>Go to Folder', self.go_to_file)

        self.ENABLE_STYLESHEET = """
            QPushButton {
                border: 1px solid #007a94;
                border-radius: 6px;
                color:#ffffff;
                background-color: #007a94;
                min-width: 80px;
                }
            QPushButton:pressed {
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #008aa6, stop: 1 #008aa6);
                }

            QPushButton:flat {
                border: none;
                }
        """
        self.DISABLE_STYLESHEET = """
            QPushButton {
               border: 1px solid #808080;
               border-radius: 6px;
               color:#ffffff;
               background-color: #808080;
               min-width: 80px;
               }
           QPushButton:flat {
               border: none;
               }

        """
        self.setStyleSheet(self.DISABLE_STYLESHEET)
        self.setMenu(menu)

    def setMenu(self, menu):
        self.menu = menu
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.open_context_menu)

    def open_context_menu(self, point=None):
        point = QtCore.QPoint(7, 23)
        self.menu.exec_(self.mapToGlobal(point))
        event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonRelease, QtCore.QPoint(10, 10), QtCore.Qt.LeftButton,
                                  QtCore.Qt.LeftButton, QtCore.Qt.NoModifier)
        self.mouseReleaseEvent(event)

    def btext(self):
        return self.text()

    # def mouse_press(self,e):
    #     if e.key()==QtCore.Qt.Key_Tab:
    #         print('Tab')
    #         return True
    #     return QtWidgets.QWidget.mouse_press(self,e)

    def mousePressEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:   ##判断是否鼠标左键点击
            self.setStyleSheet(self.ENABLE_STYLESHEET)
            print(print(self.sender().toolTip()))

    def open_file_path(self):
        file_name = self.text()
        with open(config_json) as f:
            result = json.load(f)
        asset_name = result.get("asset")
        type_name = result.get("type")
        open_file_path = os.path.abspath(os.path.join(project_path, asset_name, type_name,file_name,file_name+'_Mod.ma'))
        return open_file_path

    def open_file(self):
        open_file = self.open_file_path()
        if os.path.exists(open_file):
            cmds.file(open_file, o=True,f=True)
        else:
            logging.error('Open File No Exists!')

    def import_file(self):
        import_file = self.open_file_path()
        if os.path.exists(import_file):
            cmds.file(import_file, i=True,dns=True,f=True)
        else:
            logging.error('Import File No Exists!')
        cmds.file(import_file, i=True,dns=True,f=True)

    def reference_file(self):
        referenct_file = self.open_file_path()
        if os.path.exists(referenct_file):
            file_namespace = os.path.basename(referenct_file).split('.')[0]
            cmds.file(referenct_file, r=True,ns=file_namespace)
        else:
            logging.error('Reference File No Exists!')

    def remove_file(self):
        remove_file = self.open_file_path()
        if os.path.exists(remove_file):
            shutil.rmtree(os.path.dirname(remove_file))
        else:
            logging.error('File No Exists!')

    def go_to_file(self):
        goto_file = self.open_file_path()
        file_path = os.path.dirname(goto_file)
        os.startfile(file_path)

def show():
    global win
    try:
        win.close()
    except:
        pass
    win = asset_window()
    win.show()
