from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.Qsci import QsciScintilla, QsciLexerPython
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import Qt
from qfluentwidgets import isDarkTheme, qconfig


class CodeEditor(QsciScintilla):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('CodingInterface')

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        font = QFont()
        font.setFamily('Consolas')
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.setFont(font)

        self.setMarginType(0, QsciScintilla.MarginType.NumberMargin)
        self.setMarginWidth(0, "0000")

        self.setMarginsFont(font)

        self.lexer = QsciLexerPython(self)
        self.setLexer(self.lexer)

        self.lexer.setFont(font)
        self.setTextColor()

        qconfig.themeChanged.connect(self.setTextColor)

    def setTextColor(self):

        if isDarkTheme():
            self.setStyleSheet("""QsciScintilla QLineEdit {
                background-color: #2e2e2e;
                color: #ffffff;
            }""")
            self.setMarginsBackgroundColor(QColor('#2e2e2e'))
            self.setPaper(QColor('#2e2e2e'))
            self.lexer.setDefaultPaper(QColor('#2e2e2e'))
            self.setMarginsForegroundColor(QColor("white"))
            self.setCaretForegroundColor(QColor('white'))
            self.setCaretLineBackgroundColor(QColor('#444444'))
            self.setCaretLineVisible(True)
            self.lexer.setColor(QColor("#66ccff"), self.lexer.Default)
            self.lexer.setColor(QColor("#ff6666"), self.lexer.Keyword)
            self.lexer.setColor(QColor("#33ff33"), self.lexer.Comment)
            self.lexer.setColor(QColor("#ffcc00"), self.lexer.Number)
            self.lexer.setColor(QColor("#ff99ff"),
                                self.lexer.DoubleQuotedString)
            self.lexer.setColor(QColor("#ff99ff"),
                                self.lexer.SingleQuotedString)
            self.lexer.setColor(QColor("#ff99ff"),
                                self.lexer.TripleSingleQuotedString)
            self.lexer.setColor(QColor("#ff99ff"),
                                self.lexer.TripleDoubleQuotedString)
            self.lexer.setColor(QColor("#f3ee66"),
                                self.lexer.FunctionMethodName)
            self.lexer.setColor(QColor("#33ffff"), self.lexer.ClassName)
            self.lexer.setColor(QColor("#ff99ff"),
                                self.lexer.DoubleQuotedFString)
            self.lexer.setColor(QColor("#ff99ff"),
                                self.lexer.SingleQuotedFString)
            self.lexer.setColor(QColor("#99ffff"), self.lexer.Identifier)

        else:
            self.setStyleSheet("""QsciScintilla QLineEdit {
                background-color: #ffffff;
                color: #000000;
            }""")
            self.setPaper(QColor('#ffffff'))
            self.lexer.setDefaultPaper(QColor('#ffffff'))
            self.setMarginsBackgroundColor(QColor('#ffffff'))
            self.setMarginsForegroundColor(QColor('#000000'))
            self.setCaretForegroundColor(QColor('#000000'))
            self.setCaretLineBackgroundColor(QColor('#eeeeee'))
            self.setCaretLineVisible(True)

            self.lexer.setColor(QColor("#000000"), self.lexer.Default)
            self.lexer.setColor(QColor("#990000"), self.lexer.Keyword)
            self.lexer.setColor(QColor("#33ff33"), self.lexer.Comment)
            self.lexer.setColor(QColor("#000000"), self.lexer.Number)
            self.lexer.setColor(QColor("#993399"),
                                self.lexer.DoubleQuotedString)
            self.lexer.setColor(QColor("#993399"),
                                self.lexer.SingleQuotedString)
            self.lexer.setColor(QColor("#993399"),
                                self.lexer.TripleSingleQuotedString)
            self.lexer.setColor(QColor("#993399"),
                                self.lexer.TripleDoubleQuotedString)
            self.lexer.setColor(QColor("#000099"),
                                self.lexer.FunctionMethodName)
            self.lexer.setColor(QColor("#33ffff"), self.lexer.ClassName)
            self.lexer.setColor(QColor("#993399"),
                                self.lexer.DoubleQuotedFString)
            self.lexer.setColor(QColor("#993399"),
                                self.lexer.SingleQuotedFString)
            self.lexer.setColor(QColor("#000000"), self.lexer.Identifier)
