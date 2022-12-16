import json
import os
import sys
import PySide2.QtWidgets as QtWidgets
import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui

class open_project_window(QtWidgets.QMainWindow):
    WINDOW_TITLE = "Open Project Folder"
    def __init__(self, parent = None):
        super(open_project_window, self).__init__(parent)

    def open_folder(self):
        current_path = os.path.abspath(os.path.dirname(__file__))
        config_json = os.path.abspath(os.path.join(current_path, 'folderPaht.json'))

        with open(config_json) as f:
            result = json.load(f)
        asset_name = result.get("folder")

        for name in asset_name:
            os.startfile(name)



if __name__=='__main__':
    app = QtWidgets.QApplication([])
    win = open_project_window()
    win.show()
    sys.exit(app.exec_())