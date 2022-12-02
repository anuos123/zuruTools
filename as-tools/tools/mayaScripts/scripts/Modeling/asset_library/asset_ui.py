import os,sys
import json
import PySide2.QtWidgets as QtWidgets
import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui

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

        self.aseet_all_cb = QtWidgets.QCheckBox('All')
        self.aseet_char_cb = QtWidgets.QCheckBox('Char')
        self.aseet_prop_cb = QtWidgets.QCheckBox('Prop')
        self.aseet_envs_cb = QtWidgets.QCheckBox('Envs')

        self.asset_name_layout.addWidget(self.asset_mods_riubut)
        self.asset_name_layout.addWidget(self.asset_rigs_riubut)

        self.asset_type_layout.addWidget(self.aseet_all_cb)
        self.asset_type_layout.addWidget(self.aseet_char_cb)
        self.asset_type_layout.addWidget(self.aseet_prop_cb)
        self.asset_type_layout.addWidget(self.aseet_envs_cb)

        self.aseet_all_cb.stateChanged.connect(self.all_asset)

        self.main_layout.addLayout(self.asset_name_layout)
        self.main_layout.addLayout(self.asset_view_layout)

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
        icon = QtGui.QIcon()

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
            toolButton = QtWidgets.QToolButton()
            toolButton.setObjectName('toolButton_%s'%i)
            toolButton.setText('toolButtons_%s'%i)

            self.asset_widget_layout.addWidget(toolButton,coordineteList[i][0],coordineteList[i][1],1,1)
            icon.addPixmap(QtGui.QPixmap(image_list[i]),QtGui.QIcon.Normal,QtGui.QIcon.Off)
            toolButton.setIcon(icon)
            toolButton.setIconSize(QtCore.QSize(100,100))

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

def show():
    global win
    try:
        win.close()
    except:
        pass
    win = asset_window()
    win.show()
