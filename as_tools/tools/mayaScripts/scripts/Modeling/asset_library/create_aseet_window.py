import json
import logging
import os,sys
#from PIL import  Image
import PySide2.QtWidgets as QtWidgets
import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

#config
from . import config

current_path = os.path.abspath(os.path.dirname(__file__))
config_json = os.path.abspath(os.path.join(current_path,'config.json'))
template_json = os.path.abspath(os.path.join(current_path,'template.json'))
project_path = config.project_path

def getMainWindowPtr():
    prt = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(prt), QtWidgets.QWidget)
    return mayaMainWindow

class create_asset_window(QtWidgets.QWidget):

    def __init__(self, parent = getMainWindowPtr()):
        super(create_asset_window, self).__init__(parent)

        self.setWindowTitle("Create Asset")
        self.setWindowFlags(QtCore.Qt.WindowType.Window)
        self.resize(250,50)

        self.cs_mainlayout = QtWidgets.QVBoxLayout()
        self._linelaout = QtWidgets.QHBoxLayout()

        self.create_bnt = QtWidgets.QPushButton('Create')
        self.cs_label = QtWidgets.QLabel('Asset Name:')
        self.cs_line = QtWidgets.QLineEdit()

        self._linelaout.addWidget(self.cs_label)
        self._linelaout.addWidget(self.cs_line)


        self.cs_mainlayout.addLayout(self._linelaout)
        self.cs_mainlayout.addWidget(self.create_bnt)

        self.create_bnt.clicked.connect(self.create_asset_folder)
        self.cs_line.returnPressed.connect(self.create_asset_folder)

        self.setLayout(self.cs_mainlayout)

    def create_asset_folder(self):
        with open(config_json) as f:
            result = json.load(f)
        asset_name = result.get("asset")
        type_name = result.get("type")
        file_path = os.path.abspath(os.path.join(project_path,asset_name,type_name))
        # print(file_path)
        if self.cs_line.text():
            if os.path.exists(file_path):
                with open(template_json) as f:
                    template_result = json.load(f)
                asset_path = os.path.abspath(os.path.join(file_path,self.cs_line.text()))
                if not os.path.exists(asset_path):
                    for cf in template_result.get("config"):
                        template_folder = os.path.abspath(os.path.join(file_path,self.cs_line.text(),cf))
                        os.makedirs(template_folder)

                        if 'Image' in template_folder:
                            png_path = os.path.join(template_folder,'{}.png'.format(self.cs_line.text()))
                            if not os.path.exists(png_path):
                                with open(png_path,'w') as f:
                                    pass
                    maya_asset_path = os.path.join(asset_path,'{}_Mod.ma'.format(self.cs_line.text()))
                    if not os.path.exists(maya_asset_path):
                        with open(maya_asset_path, 'w') as f:
                            pass
                    logging.info("Asset '{}' ,Creation complete !".format(self.cs_line.text()))
                    self.close()
                else:
                    logging.error('Folder "{}" is Exists'.format(self.cs_line.text()))
        else:
            logging.error('Place input text in Line!')