from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QFrame, QHBoxLayout
from .calculate_interface import CalculateInterface
from .setting_interface import SettingInterface
from .statistics_interface import StatisticsInterface
from .coding_interface import CodingInterface
from qfluentwidgets import NavigationItemPosition, SplitFluentWindow, setFont, SubtitleLabel
from qfluentwidgets import FluentIcon as FIF


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignmentFlag.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))

        # !IMPORTANT: leave some space for title bar
        self.hBoxLayout.setContentsMargins(0, 32, 0, 0)


class MainWindow(SplitFluentWindow):

    def __init__(self):
        super().__init__()
        self.calculateInterface = CalculateInterface(self)
        self.settingInterface = SettingInterface(self)
        self.statisticsInterface = StatisticsInterface(self)
        self.codingInterface = CodingInterface(self)
        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        # add sub interface
        self.addSubInterface(self.calculateInterface, FIF.APPLICATION, self.tr('Calculate'))
        self.addSubInterface(self.statisticsInterface, FIF.PIE_SINGLE, self.tr('Statistics'))
        self.addSubInterface(self.codingInterface, FIF.CODE, self.tr('Coding'))
        self.addSubInterface(self.settingInterface, FIF.SETTING,
                             self.tr('Settings'), NavigationItemPosition.BOTTOM)
        self.navigationInterface.setExpandWidth(280)

    def initWindow(self):
        self.resize(500, 700)
        # self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle(self.tr('Scientific Calculator'))

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
