from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QProcess
from .Ui_CodingInterface import Ui_CodingInterface
import tempfile
import sys
import os



class CodingInterface(Ui_CodingInterface, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        if getattr(sys, 'frozen', False):
            if sys._MEIPASS:
                self.base_dir = sys._MEIPASS
                self.python_path = os.path.join(self.base_dir, 'python.exe')
            else:
                self.base_dir = os.path.dirname(sys.executable)
                self.python_path = os.path.join(self.base_dir, '_internal', 'python.exe')
                sys.path.append(os.path.join(self.base_dir, '_internal'))
        else:
            self.base_dir = os.path.dirname(__file__)
            self.python_path = sys.executable
        
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        # self.pushButton.setShortcut('Shift + Enter')
        font = QFont()
        font.setFamily('Consolas')
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.setFont(font)
        self.plainTextEdit.setFont(font)
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.handle_output)
        self.process.readyReadStandardError.connect(self.handle_output)
        self.process.finished.connect(self.handle_finished)

    def run(self):
        code = self.codeeditor.text()
        self.plainTextEdit.setPlainText(self.plainTextEdit.toPlainText(
        ) + '\n' + '------------------------------------------------------')
        dir = 'Temp'
        os.makedirs(dir, exist_ok=True)
        with tempfile.NamedTemporaryFile(suffix='.py', mode='w+', dir=dir, delete=False) as tmp:
            tmp.write(code)
            tmp.flush()
            self.temp_file_path = tmp.name
        self.process.start(self.python_path, [self.temp_file_path])

    def handle_output(self):
        output = self.process.readAllStandardOutput().data().decode()
        error = self.process.readAllStandardError().data().decode()
        self.plainTextEdit.setPlainText(
            self.plainTextEdit.toPlainText() + '\n' + output + error)
    def handle_finished(self):
        if os.path.exists(self.temp_file_path):
            try:
                os.unlink(self.temp_file_path)
            except:
                pass
