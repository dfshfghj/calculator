# Form implementation generated from reading ui file 'Ui_calculator.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CalculateInterface(object):
    def setupUi(self, CalculateInterface):
        CalculateInterface.setObjectName("CalculateInterface")
        CalculateInterface.resize(516, 515)
        self.verticalLayout = QtWidgets.QVBoxLayout(CalculateInterface)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=CalculateInterface)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = ScrollArea(parent=CalculateInterface)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 494, 140))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = ImageLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.widget_2 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.widget_2.setMinimumSize(QtCore.QSize(20, 0))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.widget_3 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 20))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2.addWidget(self.widget_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_2 = LineEdit(parent=CalculateInterface)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_3 = BodyLabel(parent=CalculateInterface)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.comboBox_2 = ComboBox(parent=CalculateInterface)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_2, 1, 2, 1, 1)
        self.label_2 = BodyLabel(parent=CalculateInterface)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = LineEdit(parent=CalculateInterface)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.comboBox = ComboBox(parent=CalculateInterface)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton7_13 = PushButton(parent=CalculateInterface)
        self.pushButton7_13.setObjectName("pushButton7_13")
        self.gridLayout_2.addWidget(self.pushButton7_13, 3, 5, 1, 1)
        self.pushButton7_14 = PushButton(parent=CalculateInterface)
        self.pushButton7_14.setObjectName("pushButton7_14")
        self.gridLayout_2.addWidget(self.pushButton7_14, 3, 0, 1, 1)
        self.pushButton7_17 = PushButton(parent=CalculateInterface)
        self.pushButton7_17.setObjectName("pushButton7_17")
        self.gridLayout_2.addWidget(self.pushButton7_17, 2, 1, 1, 1)
        self.pushButton7_8 = PushButton(parent=CalculateInterface)
        self.pushButton7_8.setObjectName("pushButton7_8")
        self.gridLayout_2.addWidget(self.pushButton7_8, 3, 3, 1, 1)
        self.pushButton7_18 = PushButton(parent=CalculateInterface)
        self.pushButton7_18.setObjectName("pushButton7_18")
        self.gridLayout_2.addWidget(self.pushButton7_18, 2, 2, 1, 1)
        self.pushButton7_7 = PushButton(parent=CalculateInterface)
        self.pushButton7_7.setObjectName("pushButton7_7")
        self.gridLayout_2.addWidget(self.pushButton7_7, 1, 4, 1, 1)
        self.pushButton7_16 = PushButton(parent=CalculateInterface)
        self.pushButton7_16.setObjectName("pushButton7_16")
        self.gridLayout_2.addWidget(self.pushButton7_16, 2, 0, 1, 1)
        self.pushButton7_19 = PushButton(parent=CalculateInterface)
        self.pushButton7_19.setObjectName("pushButton7_19")
        self.gridLayout_2.addWidget(self.pushButton7_19, 1, 5, 1, 1)
        self.pushButton7_6 = PushButton(parent=CalculateInterface)
        self.pushButton7_6.setObjectName("pushButton7_6")
        self.gridLayout_2.addWidget(self.pushButton7_6, 3, 2, 1, 1)
        self.pushButton7_11 = PushButton(parent=CalculateInterface)
        self.pushButton7_11.setObjectName("pushButton7_11")
        self.gridLayout_2.addWidget(self.pushButton7_11, 2, 4, 1, 1)
        self.pushButton7_4 = PushButton(parent=CalculateInterface)
        self.pushButton7_4.setObjectName("pushButton7_4")
        self.gridLayout_2.addWidget(self.pushButton7_4, 1, 2, 1, 1)
        self.pushButton7_5 = PushButton(parent=CalculateInterface)
        self.pushButton7_5.setObjectName("pushButton7_5")
        self.gridLayout_2.addWidget(self.pushButton7_5, 1, 3, 1, 1)
        self.pushButton7_3 = PushButton(parent=CalculateInterface)
        self.pushButton7_3.setObjectName("pushButton7_3")
        self.gridLayout_2.addWidget(self.pushButton7_3, 1, 1, 1, 1)
        self.pushButton7_10 = PushButton(parent=CalculateInterface)
        self.pushButton7_10.setObjectName("pushButton7_10")
        self.gridLayout_2.addWidget(self.pushButton7_10, 2, 3, 1, 1)
        self.pushButton7_12 = PushButton(parent=CalculateInterface)
        self.pushButton7_12.setObjectName("pushButton7_12")
        self.gridLayout_2.addWidget(self.pushButton7_12, 2, 5, 1, 1)
        self.pushButton7_9 = PushButton(parent=CalculateInterface)
        self.pushButton7_9.setObjectName("pushButton7_9")
        self.gridLayout_2.addWidget(self.pushButton7_9, 3, 4, 1, 1)
        self.pushButton7_2 = PushButton(parent=CalculateInterface)
        self.pushButton7_2.setObjectName("pushButton7_2")
        self.gridLayout_2.addWidget(self.pushButton7_2, 1, 0, 1, 1)
        self.pushButton7_15 = PushButton(parent=CalculateInterface)
        self.pushButton7_15.setObjectName("pushButton7_15")
        self.gridLayout_2.addWidget(self.pushButton7_15, 3, 1, 1, 1)
        self.pushButton = PushButton(parent=CalculateInterface)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = PushButton(parent=CalculateInterface)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_7 = PushButton(parent=CalculateInterface)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 0, 2, 1, 1)
        self.pushButton_8 = PushButton(parent=CalculateInterface)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 0, 3, 1, 1)
        self.pushButton_9 = PushButton(parent=CalculateInterface)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 0, 4, 1, 1)
        self.pushButton_23 = PushButton(parent=CalculateInterface)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_2.addWidget(self.pushButton_23, 0, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = PushButton(parent=CalculateInterface)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)
        self.pushButton_4 = PushButton(parent=CalculateInterface)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 5, 0, 1, 1)
        self.pushButton_12 = PushButton(parent=CalculateInterface)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 3, 4, 1, 1)
        self.pushButton_13 = PushButton(parent=CalculateInterface)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 4, 1, 1, 1)
        self.pushButton_16 = PushButton(parent=CalculateInterface)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 4, 4, 1, 1)
        self.pushButton_DEL = PushButton(parent=CalculateInterface)
        self.pushButton_DEL.setObjectName("pushButton_DEL")
        self.gridLayout.addWidget(self.pushButton_DEL, 2, 4, 1, 1)
        self.pushButton_21 = PushButton(parent=CalculateInterface)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout.addWidget(self.pushButton_21, 2, 1, 1, 1)
        self.pushButton_17 = PushButton(parent=CalculateInterface)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 5, 3, 1, 1)
        self.pushButton_14 = PushButton(parent=CalculateInterface)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 4, 3, 1, 1)
        self.pushButton7 = PushButton(parent=CalculateInterface)
        self.pushButton7.setObjectName("pushButton7")
        self.gridLayout.addWidget(self.pushButton7, 2, 0, 1, 1)
        self.pushButton_5 = PushButton(parent=CalculateInterface)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 0, 1, 1)
        self.pushButton_15 = PushButton(parent=CalculateInterface)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 4, 5, 1, 1)
        self.pushButton_18 = PushButton(parent=CalculateInterface)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 5, 1, 1, 1)
        self.pushButton_20 = PushButton(parent=CalculateInterface)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 5, 5, 1, 1)
        self.pushButton_AC = PushButton(parent=CalculateInterface)
        self.pushButton_AC.setObjectName("pushButton_AC")
        self.gridLayout.addWidget(self.pushButton_AC, 2, 5, 1, 1)
        self.pushButton_10 = PushButton(parent=CalculateInterface)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 3, 3, 1, 1)
        self.pushButton_6 = PushButton(parent=CalculateInterface)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 3, 1, 1, 1)
        self.pushButton_19 = PushButton(parent=CalculateInterface)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 5, 4, 1, 1)
        self.pushButton_22 = PushButton(parent=CalculateInterface)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_22, 2, 3, 1, 1)
        self.pushButton_11 = PushButton(parent=CalculateInterface)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 3, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(CalculateInterface)
        QtCore.QMetaObject.connectSlotsByName(CalculateInterface)

    def retranslateUi(self, CalculateInterface):
        _translate = QtCore.QCoreApplication.translate
        CalculateInterface.setWindowTitle(_translate("CalculateInterface", "Form"))
        self.label.setText(_translate("CalculateInterface", "math"))
        self.label_3.setText(_translate("CalculateInterface", CalculateInterface.tr("result")))
        self.comboBox_2.setItemText(0, _translate("CalculateInterface", "python"))
        self.comboBox_2.setItemText(1, _translate("CalculateInterface", "LaTeX"))
        self.label_2.setText(_translate("CalculateInterface", CalculateInterface.tr("expression")))
        self.comboBox.setItemText(0, _translate("CalculateInterface", "python"))
        self.comboBox.setItemText(1, _translate("CalculateInterface", "LaTeX"))
        self.pushButton7_13.setText(_translate("CalculateInterface", "xʸ"))
        self.pushButton7_14.setText(_translate("CalculateInterface", "π"))
        self.pushButton7_17.setText(_translate("CalculateInterface", "arccos"))
        self.pushButton7_8.setText(_translate("CalculateInterface", "x²"))
        self.pushButton7_18.setText(_translate("CalculateInterface", "arctan"))
        self.pushButton7_7.setText(_translate("CalculateInterface", "log"))
        self.pushButton7_16.setText(_translate("CalculateInterface", "arcsin"))
        self.pushButton7_19.setText(_translate("CalculateInterface", "℮"))
        self.pushButton7_6.setText(_translate("CalculateInterface", ")"))
        self.pushButton7_11.setText(_translate("CalculateInterface", "y"))
        self.pushButton7_4.setText(_translate("CalculateInterface", "tan"))
        self.pushButton7_5.setText(_translate("CalculateInterface", "ln"))
        self.pushButton7_3.setText(_translate("CalculateInterface", "cos"))
        self.pushButton7_10.setText(_translate("CalculateInterface", "x"))
        self.pushButton7_12.setText(_translate("CalculateInterface", "z"))
        self.pushButton7_9.setText(_translate("CalculateInterface", "x³"))
        self.pushButton7_2.setText(_translate("CalculateInterface", "sin"))
        self.pushButton7_15.setText(_translate("CalculateInterface", "("))
        self.pushButton.setText(_translate("CalculateInterface", "Sum"))
        self.pushButton_2.setText(_translate("CalculateInterface", "Product"))
        self.pushButton_7.setText(_translate("CalculateInterface", "Integral"))
        self.pushButton_8.setText(_translate("CalculateInterface", "Derivative"))
        self.pushButton_9.setText(_translate("CalculateInterface", "Limit"))
        self.pushButton_23.setText(_translate("CalculateInterface", "≈"))
        self.pushButton_3.setText(_translate("CalculateInterface", "1"))
        self.pushButton_4.setText(_translate("CalculateInterface", "0"))
        self.pushButton_12.setText(_translate("CalculateInterface", "×"))
        self.pushButton_13.setText(_translate("CalculateInterface", "2"))
        self.pushButton_16.setText(_translate("CalculateInterface", "+"))
        self.pushButton_DEL.setText(_translate("CalculateInterface", "DEL"))
        self.pushButton_21.setText(_translate("CalculateInterface", "8"))
        self.pushButton_17.setText(_translate("CalculateInterface", "×10ˣ"))
        self.pushButton_14.setText(_translate("CalculateInterface", "3"))
        self.pushButton7.setText(_translate("CalculateInterface", "7"))
        self.pushButton_5.setText(_translate("CalculateInterface", "4"))
        self.pushButton_15.setText(_translate("CalculateInterface", "-"))
        self.pushButton_18.setText(_translate("CalculateInterface", "."))
        self.pushButton_20.setText(_translate("CalculateInterface", "="))
        self.pushButton_AC.setText(_translate("CalculateInterface", "AC"))
        self.pushButton_10.setText(_translate("CalculateInterface", "6"))
        self.pushButton_6.setText(_translate("CalculateInterface", "5"))
        self.pushButton_19.setText(_translate("CalculateInterface", "Ans"))
        self.pushButton_22.setText(_translate("CalculateInterface", "9"))
        self.pushButton_11.setText(_translate("CalculateInterface", "÷"))
from qfluentwidgets import BodyLabel, ComboBox, ImageLabel, LineEdit, PushButton, ScrollArea
