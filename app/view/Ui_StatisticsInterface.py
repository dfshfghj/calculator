# Form implementation generated from reading ui file 'Ui_statistics.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_StatisticsInterface(object):
    def setupUi(self, StatisticsInterface):
        StatisticsInterface.setObjectName("StatisticsInterface")
        StatisticsInterface.resize(562, 499)
        self.verticalLayout = QtWidgets.QVBoxLayout(StatisticsInterface)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=StatisticsInterface)
        self.widget.setMinimumSize(QtCore.QSize(0, 25))
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.command_bar = CommandBar(parent=StatisticsInterface)
        self.command_bar.setObjectName("command_bar")
        self.verticalLayout.addWidget(self.command_bar)
        self.scrollArea = ScrollArea(parent=StatisticsInterface)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 542, 196))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = ImageLabel(parent=self.scrollAreaWidgetContents)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = PrimaryPushButton(parent=StatisticsInterface)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = PrimaryPushButton(parent=StatisticsInterface)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = TableWidget(parent=StatisticsInterface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectItems)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(StatisticsInterface)
        QtCore.QMetaObject.connectSlotsByName(StatisticsInterface)

    def retranslateUi(self, StatisticsInterface):
        _translate = QtCore.QCoreApplication.translate
        StatisticsInterface.setWindowTitle(_translate("StatisticsInterface", "Form"))
        self.pushButton_2.setText(_translate("StatisticsInterface", "统计结果"))
        self.pushButton.setText(_translate("StatisticsInterface", "画图"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("StatisticsInterface", "变量名"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("StatisticsInterface", "单位"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("StatisticsInterface", "注释"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("StatisticsInterface", "1"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("StatisticsInterface", "2"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("StatisticsInterface", "3"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("StatisticsInterface", "4"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("StatisticsInterface", "5"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("StatisticsInterface", "6"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("StatisticsInterface", "7"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("StatisticsInterface", "8"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("StatisticsInterface", "9"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("StatisticsInterface", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("StatisticsInterface", "A"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("StatisticsInterface", "B"))
from qfluentwidgets import CommandBar, ImageLabel, PrimaryPushButton, ScrollArea, TableWidget
