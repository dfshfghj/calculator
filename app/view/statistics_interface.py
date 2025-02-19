from PyQt6.QtWidgets import QWidget, QHeaderView, QTableWidget, QTableWidgetItem, QApplication
from PyQt6.QtGui import QAction, QImage, QClipboard
from .Ui_StatisticsInterface import Ui_StatisticsInterface
from qfluentwidgets import ImageLabel, PushButton, TableWidget, RoundMenu, setTheme, Theme, Action, MenuAnimationType, MenuItemDelegate, CheckableMenu, MenuIndicatorType
from qfluentwidgets import FluentIcon as FIF
import numpy as np
from PyQt6.QtGui import QPixmap
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

plt.rcParams['font.sans-serif']=['SimSun']
plt.rcParams['font.size']=18
plt.rcParams['axes.unicode_minus']=False

class StatisticsInterface(Ui_StatisticsInterface, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setupUi(self)
        self.scrollArea.enableTransparentBackground()
        self.tableWidget.setSelectRightClickedRow(True)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        if self.tableWidget.columnCount() <= 1:
            self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.draw)
        self.updateRowNumbers()
        self.updateColumnNumbers()

    def updateRowNumbers(self):
        vertical_head_labels = [self.tr('name'), self.tr('unit'), self.tr('comment')]
        for row in range(1, self.tableWidget.rowCount()):
            vertical_head_labels.append(str(row))
        self.tableWidget.setVerticalHeaderLabels(vertical_head_labels)

    def updateColumnNumbers(self):
        #for column in range(self.tableWidget.columnCount()):
        #    pass
        # self.tableWidget.columnCount() <= 26
        horizontal_head_labels = [chr(_ + ord('A')) for _ in range(self.tableWidget.columnCount())]
        self.tableWidget.setHorizontalHeaderLabels(horizontal_head_labels)

    def get_content(self):
        data = []
        for col in range(self.tableWidget.columnCount()):
            col_data = []
            name, unit, comment = self.tableWidget.item(0, col).text(), self.tableWidget.item(1, col).text(), self.tableWidget.item(2, col).text()
            if not name:
                name = ''
            if not unit:
                unit = ''
            if not comment:
                comment = ''

            for row in range(3, self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    col_data.append(float(item.text()))
                else:
                    col_data.append(np.nan)
            col_data = np.array(col_data)
            data.append((name, unit, comment, col_data))
        return data

    def draw(self):
        content = self.get_content()
        x_name, x_unit, x_comment, x_data = content[0]
        y_name, y_unit, y_comment = content[1][0], content[1][1], content[1][2]

        fig, ax = plt.subplots(figsize=(10, 7.1))
        canvas = FigureCanvas(fig)
        ax.minorticks_on()
        ax.tick_params(axis='both', which='major', labelsize=12)
        ax.grid(True, linestyle='--')
        ax.set_xlabel(rf'{x_name}/{x_unit}', math_fontfamily='cm')
        ax.set_ylabel(rf'{y_name}/{y_unit}', math_fontfamily='cm')
        for i in range(1, len(content)):
            ax.plot(x_data, content[i][3], label=content[i][2])
        ax.legend()
        fig.canvas.draw()
        buf, size = canvas.print_to_buffer()
        qimg = QImage(buf, size[0], size[1], QImage.Format.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qimg)
        self.label.setFixedSize(pixmap.size())
        self.label.setPixmap(pixmap)
        

    def add_row(self, selected_rows):
        if len(selected_rows) == 1:
            row_to_insert = selected_rows[0] + 1
        else:
            row_to_insert = self.tableWidget.rowCount()

        self.tableWidget.insertRow(row_to_insert)
        self.updateRowNumbers()

    def delete_row(self, selected_rows):
        for row in sorted(selected_rows, reverse=True):
            self.tableWidget.removeRow(row)
        self.updateRowNumbers()

    def add_column(self):
        pass

    def delete_column(self):
        pass

    def paste_from_clipboard(self):
        clipboard = QApplication.clipboard()
        mime_data = clipboard.mimeData()

        if mime_data.hasText():
            text = mime_data.text()
            rows = [line.split('\t') for line in text.split('\n')]
            
    def contextMenuEvent(self, position):
        menu = RoundMenu(parent=self)

        # add actions
        action_copy = Action(FIF.COPY, self.tr('copy'), shortcut='Ctrl+C')
        action_cut = Action(FIF.CUT, self.tr('cut'), shortcut='Ctrl+X')
        menu.addAction(action_copy)
        menu.addAction(action_cut)
        menu.actions()[0].setCheckable(True)
        menu.actions()[0].setChecked(True)

        # add sub menu
        submenu_1 = RoundMenu(self.tr("import"), self)
        submenu_1.setIcon(FIF.FOLDER)
        submenu_1.addActions([
            Action(FIF.DOCUMENT, 'excel'),
            Action(FIF.CODE, 'LaTeX'),
        ])
        menu.addMenu(submenu_1)

        submenu_2 = RoundMenu(self.tr("export"), self)
        submenu_2.setIcon(FIF.SEND)
        submenu_2.addActions([
            Action(FIF.DOCUMENT, 'excel'),
            Action(FIF.CODE, 'LaTeX'),
        ])
        menu.addMenu(submenu_2)

        # add actions
        action_paste = Action(FIF.PASTE, self.tr('paste'), shortcut='Ctrl+V')
        action_cancel = Action(FIF.CANCEL, self.tr('cancel'), shortcut='Ctrl+Z')
        menu.addActions([
            action_paste,
            action_cancel
        ])

        # add separator
        menu.addSeparator()
        selected_rows = []
        print(self.tableWidget.selectedRanges())
        #print(self.tableWidget.selectedIndexes())
        print([(_.bottomRow(), _.topRow(), _.leftColumn(), _.rightColumn()) for _ in self.tableWidget.selectedRanges()])
        #print([(_.row(), _.column()) for _ in self.tableWidget.selectedIndexes()])
        for index in self.tableWidget.selectedIndexes():
            if index.row() >= 3:
                selected_rows.append(index.row())
        #print(selected_rows)
        
            
        action_add_column = Action(FIF.ADD, self.tr('insert column'))
        action_remove_column = Action(FIF.REMOVE, self.tr('delete column'))
        action_add_row = Action(FIF.ADD, self.tr('insert row'))
        action_remove_row = Action(FIF.REMOVE, self.tr('delete row'))
        action_add_row.triggered.connect(lambda: self.add_row(selected_rows))
        action_remove_row.triggered.connect(lambda: self.delete_row(selected_rows))

        if len(selected_rows) == 0:
            action_copy.setEnabled(False)
            action_cut.setEnabled(False)
            action_paste.setEnabled(False)
            action_add_row.setEnabled(True)
            action_remove_row.setEnabled(False)
        elif len(selected_rows) == 1:
            action_add_row.setEnabled(True)
            action_remove_row.setEnabled(True)
        else:
            action_add_row.setEnabled(False)
            action_remove_row.setEnabled(True)

        menu.addAction(action_add_column)
        menu.addAction(action_remove_column)
        menu.addAction(action_add_row)
        menu.addAction(action_remove_row)
        menu.actions()[-2].setCheckable(True)
        menu.actions()[-2].setChecked(True)

        # show menu
        menu.exec(position.globalPos(), aniType=MenuAnimationType.DROP_DOWN)