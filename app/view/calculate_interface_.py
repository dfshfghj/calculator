import latex2sympy2
from sympy import *
from sympy.parsing.sympy_parser import parse_expr, auto_symbol
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from .Ui_CalculateInterface import Ui_CalculateInterface
from PyQt6.QtGui import QPixmap, QImage, QPainter
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from qfluentwidgets import PushButton, isDarkTheme
from ..common.config import cfg
from functools import lru_cache
#from queue import Queue
from multiprocessing import Process, Queue
from ..common.calculate import start_process


'''
@lru_cache(maxsize=4096)
def _calculate(expression: str, mode: str):
    expression = sympify(expression, rational=True)
    if mode == '=':
        if isinstance(expression, (Sum, Product, Integral)):
            raw_result = simplify(expression.doit())
        else:
            raw_result = simplify(expression)
        return raw_result
    else:
        result = expression.evalf()
        return result
    
def calculate(expression: str, mode: str, queue: Queue):
        queue.put(_calculate(expression, mode))
'''
'''
class CalculateThread(QThread):
    calculated_signal = pyqtSignal(object)
    def __init__(self, expression, mode):
        super().__init__()
        self.expression = expression
        self.mode = mode
    def run(self):
        self.result = calculate(self.expression, self.mode)
        self.calculated_signal.emit(self.result)


'''
def number_format(num):
    if cfg.numberFormat.value == 'Sci':
        if num == 0:
            exponent = 0
            base = format(0, '.8f')
        else:
            exponent = int(log(num, 10))
            base = format(num / 10 ** exponent, '.8f')
        return rf'{base} \times 10^{{{exponent}}}'
    elif cfg.numberFormat.value == 'Fix':
        return str(format(num, '.9f'))
    elif cfg.numberFormat.value == 'Norm 1':
        if num == 0:
            exponent = 0
        else:
            exponent = int(log(num, 10))
        if exponent <= -2 or exponent >= 10:
            base = format(num / 10 ** exponent, '.8f')
            return rf'{base} \times 10^{{{exponent}}}'
        else:
            if isinstance(num, Integer):
                return str(num) 
            else:
                return str(format(num, '.9f'))
    elif cfg.numberFormat.value == 'Norm 2':
        if num == 0:
            exponent = 0
        else:
            exponent = int(log(num, 10))
        if exponent <= -9 or exponent >= 10:
            base = format(num / 10 ** exponent, '.8f')
            return rf'{base} \times 10^{{{exponent}}}'
        else:
            if isinstance(num, Integer):
                return str(num) 
            else:
                return str(format(num, '.9f'))

def copy_to_clipboard(qWidget: QWidget):
    clipboard = QApplication.clipboard()
    clipboard.setText(qWidget.text())
'''
@lru_cache(maxsize=4096)
def calculate(expression: str, mode: str):
    expression = sympify(expression, rational=True)
    if mode == '=':
        if isinstance(expression, (Sum, Product, Integral)):
            raw_result = simplify(expression.doit())
        else:
            raw_result = simplify(expression)
        return raw_result
    else:
        result = expression.evalf()
        return result
'''
class CalculateInterface(Ui_CalculateInterface, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setupUi(self)

        self.mathdic = {'=': '=', '≈': '≈', '+': '+', '-': '-', '×': '*', '÷': '/', '(': '(', ')': ')', 'x²': '**2', 'x³': '**3', 'xʸ': '**', '×10ˣ': '* 10 **',
                        'π': 'pi', '℮': 'E', 'Ans': 'Ans', 'x': 'x', 'y': 'y', 'z': 'z',
                        '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
                        'sin': 'sin(', 'cos': 'cos(', 'tan': 'tan(', 'arcsin': 'asin(', 'arccos': 'acos(', 'arctan': 'atan(', 'ln': 'log(', 'log': 'log(, 10)', 
                        'Sum': 'Sum( , (x, , ))', 'Product': 'Product( , (x, , ))', 'Integral': 'Integral( , (x, , ))', 'Limit': 'Limit(, x, )', 'Derivative': 'Derivative(, x)'}
        self.latexdic = {'=': '=', '≈': '≈', '+': '+', '-': '-', '×': r'\times', '÷': r'\div', '(': '(', ')': ')', 'x²': r'^2', 'x³': r'^3', 'xʸ': r'^y', '×10ˣ': r'\times 10^',
                         'π': r'\pi', '℮': r'e', 'Ans': 'Ans', 'x': 'x', 'y': 'y', 'z': 'z',
                         '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
                         'sin': r'\sin', 'cos': r'\cos', 'tan': r'\tan', 'arcsin': r'\arcsin', 'arccos': r'\arccos', 'arctan': r'\arctan', 'ln': r'\ln', 'log': r'\log_{10}', 
                         'Sum': r'\sum_{x = }^{}', 'Product': r'\prod_{x = }^{}', 'Integral': r'\int_{}^{}', 'Limit': r'\lim_{x \to}', 'Derivative': r'\frac{d}{dx}'}
        self.expression_stack = []
        self.expression = ''
        self.history = []
        self.tmp = 0
        self.history_qimage = None
        self.max_history_image_height = 100000
        self.state = 'wait_for_input'
        self.result = None
        self.recent_image = None
        self.raw_result = None

        self.lineEdit.setText(self.expression)
        self.lineEdit_2.setReadOnly(True)

        self.scrollArea.enableTransparentBackground()

        self.all_buttons = [_ for _ in self.findChildren(PushButton)]

        for button in self.all_buttons:
            button.clicked.connect(
                lambda _, btn=button: self.on_button_clicked(btn))
        self.lineEdit.textChanged.connect(self.on_text_changed)
        self.lineEdit.textChanged.connect(self.render_latex_from_python_expr)

    def keyPressEvent(self, a0):
        if a0.key() == Qt.Key.Key_Up:
            if self.tmp > 0 and self.history:
                self.tmp -= 1
                self.state = 'chosing_history'
                self.expression, self.result, input_mode, display_mode = self.history[self.tmp]
                self.expression_stack.append(self.expression)
                self.lineEdit.setText(self.expression)
                if self.comboBox_2.currentText() == 'python':
                    self.lineEdit_2.setText(str(self.result))
                else:
                    self.lineEdit_2.setText(latex(self.result))
                self.lineEdit.setCursorPosition(len(self.expression))
                self.lineEdit.setFocus()
                self.lineEdit.selectAll()
        elif a0.key() == Qt.Key.Key_Down:
            if self.tmp < len(self.history) - 1 and self.history:
                self.state = 'chosing_history'
                self.tmp += 1
                self.expression, self.result, input_mode, display_mode = self.history[self.tmp]
                self.expression_stack.append(self.expression)
                self.lineEdit.setText(self.expression)
                if self.comboBox_2.currentText() == 'python':
                    self.lineEdit_2.setText(str(self.result))
                else:
                    self.lineEdit_2.setText(latex(self.result))
                self.result = None
                self.lineEdit.setCursorPosition(len(self.expression))
                self.lineEdit.setFocus()
                self.lineEdit.selectAll()
        
        elif a0.key() == Qt.Key.Key_Enter or a0.key() == Qt.Key.Key_Return:
            self.pushButton_20.click()
        else:
            super().keyPressEvent(a0)


    def on_button_clicked(self, button: PushButton):
        if self.state != 'calculating':
            text = button.text()
            if text == 'DEL':
                # print(self.expression_stack)
                if self.expression_stack:
                    self.expression_stack.pop()
                if self.expression_stack:
                    self.expression = self.expression_stack[-1]
                else:
                    self.expression = ''
            elif text == 'AC':
                self.expression_stack = []
                self.expression = ''
            elif text == 'Ans':
                pass
            elif text == '=' or text == '≈':
                #print(self.history)
                try:
                    input_mode = self.comboBox.currentText()
                    if input_mode == 'python':
                        expression = sympify(self.expression, rational=True)
                    elif input_mode == 'LaTeX':
                        expression = latex2sympy2.latex2sympy(self.expression)
                    self.state = 'calculating'
                    self.run_calculate(expression, mode=text)

                except Exception as e:
                    print(e)
                    # pass

            else:
                input_mode = self.comboBox.currentText()
                if input_mode == 'python':
                    self.expression += self.mathdic[text]
                elif input_mode == 'LaTeX':
                    self.expression += self.latexdic[text]
            self.lineEdit.setText(self.expression)
            if self.expression:
                self.comboBox.setDisabled(True)
            else:
                self.comboBox.setDisabled(False)

    def on_text_changed(self, new_text):
        if self.state == 'wait_for_input':
            self.add_history()
            self.lineEdit_2.setText('')
            self.state = 'input'
        self.render_latex_from_python_expr()
        self.expression = new_text
        if self.expression:
            self.comboBox.setDisabled(True)
        else:
            self.comboBox.setDisabled(False)
        # print(self.expression)

    def render_latex_from_python_expr(self):
        try:
            input_mode = self.comboBox.currentText()
            if input_mode == 'python':
                python_expr = self.expression
                transformations = (auto_symbol,)
                latex_code = latex(parse_expr(
                    python_expr, transformations=transformations, evaluate=False)).replace(r'\limits', '').replace(r'\frac', r'\dfrac')
            elif input_mode == 'LaTeX':
                latex_code = self.expression.replace(r'\frac', r'\dfrac')

            fig = Figure(frameon=False)
            canvas = FigureCanvas(fig)
            ax = fig.add_axes([0, 0, 1, 1], frame_on=False)
            ax.set_axis_off()

            if isDarkTheme():
                t = ax.text(0, 0, rf"${latex_code}=$", fontsize=20,
                            ha='left', va='bottom', color='white')
            else:
                t = ax.text(0, 0, rf"${latex_code}=$",
                            fontsize=20, ha='left', va='bottom')
            bbox_inches = t.get_window_extent(
                renderer=fig.canvas.get_renderer()).transformed(fig.dpi_scale_trans.inverted())
            width, height = bbox_inches.width, bbox_inches.height
            fig.set_size_inches(width, height * 1.1)
            fig.canvas.draw()

            buf, size = canvas.print_to_buffer()

            qimg = QImage(buf, size[0], size[1], QImage.Format.Format_RGBA8888)
            if self.result is not None:
                if isinstance(self.result, (Integer, Float)):
                    result_latex_code = number_format(self.result).replace(r'\frac', r'\dfrac')
                else:
                    result_latex_code = latex(self.result).replace(r'\limits', '').replace(r'\frac', r'\dfrac')
                plt.close(fig)
                fig = Figure(frameon=False)
                canvas = FigureCanvas(fig)
                ax = fig.add_axes([0, 0, 1, 1], frame_on=False)
                ax.set_axis_off()
                if isDarkTheme():
                    t = ax.text(0, 0, rf"${result_latex_code}$", fontsize=20,
                                ha='left', va='bottom', color='white')
                else:
                    t = ax.text(0, 0, rf"${result_latex_code}$",
                                fontsize=20, ha='left', va='bottom')
                bbox_inches = t.get_window_extent(
                    renderer=fig.canvas.get_renderer()).transformed(fig.dpi_scale_trans.inverted())
                width, height = bbox_inches.width, bbox_inches.height
                fig.set_size_inches(width, height * 1.1)
                fig.canvas.draw()
                buf, size = canvas.print_to_buffer()
                qimg_result = QImage(
                    buf, size[0], size[1], QImage.Format.Format_RGBA8888)
                qimg_total = QImage(max(qimg.width(), qimg_result.width()), qimg.height(
                ) + qimg_result.height(), QImage.Format.Format_RGBA8888)
                qimg_total.fill(Qt.GlobalColor.transparent)
                painter = QPainter(qimg_total)
                painter.drawImage(qimg_total.width() - qimg.width(), 0, qimg)
                painter.drawImage(
                    qimg_total.width() - qimg_result.width(), qimg.height(), qimg_result)
                painter.end()
                self.recent_image = qimg_total.scaled(qimg_total.width(), qimg_total.height())
                qimg = qimg_total
            if self.history_qimage:
                combined_qimage = QImage(max(qimg.width(), self.history_qimage.width()), qimg.height(
                ) + self.history_qimage.height(), QImage.Format.Format_RGBA8888)
                combined_qimage.fill(Qt.GlobalColor.transparent)
                painter = QPainter(combined_qimage)
                painter.drawImage(combined_qimage.width(
                ) - self.history_qimage.width(), 0, self.history_qimage)
                painter.drawImage(
                    combined_qimage.width() - qimg.width(), self.history_qimage.height(), qimg)
                painter.end()
                qimg = combined_qimage
            pixmap = QPixmap.fromImage(qimg)

            self.label.setFixedSize(pixmap.size())
            self.label.setPixmap(pixmap)
            
        except Exception as e:
            print(e)
            if not self.lineEdit.text().strip():
                if self.history_qimage:
                    qimg = self.history_qimage
                    pixmap = QPixmap.fromImage(qimg)
                    self.label.setFixedSize(pixmap.size())
                    self.label.setPixmap(pixmap)
                else:
                    print('empty')
                    self.label.setPixmap(None)
        h_bar = self.scrollArea.horizontalScrollBar()
        v_bar = self.scrollArea.verticalScrollBar()
        h_bar.setValue(h_bar.maximum())
        v_bar.setValue(v_bar.maximum())
    def add_history(self):
        if self.history_qimage:
            combined_history_qimage = QImage(max(self.history_qimage.width(), self.recent_image.width()), self.history_qimage.height(
            ) + self.recent_image.height(), QImage.Format.Format_RGBA8888)
            combined_history_qimage.fill(Qt.GlobalColor.transparent)
            painter = QPainter(combined_history_qimage)
            painter.drawImage(combined_history_qimage.width(
            ) - self.history_qimage.width(), 0, self.history_qimage)
            painter.drawImage(
                combined_history_qimage.width() - self.recent_image.width(), self.history_qimage.height(), self.recent_image)
            painter.end()
            if combined_history_qimage.height() > self.max_history_image_height:
                self.history_qimage = combined_history_qimage.copy(
                    0, combined_history_qimage.height() - self.max_history_image_height, combined_history_qimage.width(), self.max_history_image_height)
            else:
                self.history_qimage = combined_history_qimage
        else:
            self.history_qimage = self.recent_image

    '''
    def run_calculate(self, expression, mode):
        print(expression)
        self.calculate_thread = CalculateThread(expression, mode)
        self.calculate_thread.calculated_signal.connect(self.on_calculated)
        self.calculate_thread.start()
        self.state = 'calculating'
    '''
    def on_calculated(self, result):
        self.result = result
        print(self.result)
        self.lineEdit_2.setText(str(self.result))
        if self.history and self.history[-1][0] == self.expression:
            self.history[-1] = (self.expression, self.result, self.comboBox.currentText(), self.comboBox_2.currentText())
        else:
            self.history.append((self.expression, self.result, self.comboBox.currentText(), self.comboBox_2.currentText()))
        self.tmp = len(self.history)
        display_mode = self.comboBox_2.currentText()
        if isinstance(self.result, (Integer, Float)):
            self.lineEdit_2.setText(number_format(self.result))
        else:
            if display_mode == 'python':
                self.lineEdit_2.setText(str(self.result))
            elif display_mode == 'LaTeX':
                self.lineEdit_2.setText(latex(self.result))
        self.render_latex_from_python_expr()
        self.state = 'wait_for_input'
        self.expression = ''
        self.result = None
    
    def run_calculate(self, expression, mode):
        queue = Queue()
        #process = Process(target=calculate, args=(expression, mode, queue))
        #process.start()
        self.calculate_process = start_process(expression, mode, queue)
        self.timer = self.startTimer(20)
        self.calculate_queue = queue
        #self.calculate_process = process
    '''
    def calculate(expression: str, queue: Queue):
        queue.put(_calculate(expression))
    '''
    def timerEvent(self, event):
        if not self.calculate_queue.empty():
            result = self.calculate_queue.get()
            self.killTimer(self.timer)
            self.calculate_process.kill()
            self.on_calculated(result)
        elif not self.calculate_process.is_alive():
            self.killTimer(self.timer)
    

class Sin(Function):
    @classmethod
    def eval(cls, arg):
        if isinstance(arg, Integer):
            if cfg.angleUnit.value == 'Degree':
                return sin(Rational(arg, 180) * pi)
            elif cfg.angleUnit.value == 'Gradian':
                return sin(Rational(arg, 200) * pi)
            elif cfg.angleUnit.value == 'Radian':
                return sin(arg)
        else:
            if cfg.angleUnit.value == 'Degree':
                return sin(arg / 180 * pi)
            elif cfg.angleUnit.value == 'Gradian':
                return sin(arg / 200 * pi)
            elif cfg.angleUnit.value == 'Radian':
                return sin(arg)


class Cos(Function):
    @classmethod
    def eval(cls, arg):
        if cfg.angleUnit.value == 'Degree':
            return cos(Rational(arg, 180) * pi)
        elif cfg.angleUnit.value == 'Gradian':
            return cos(Rational(arg, 200) * pi)
        elif cfg.angleUnit.value == 'Radian':
            return cos(arg)


class Tan(Function):
    @classmethod
    def eval(cls, arg):
        if cfg.angleUnit.value == 'Degree':
            return tan(Rational(arg, 180) * pi)
        elif cfg.angleUnit.value == 'Gradian':
            return tan(Rational(arg, 200) * pi)
        elif cfg.angleUnit.value == 'Radian':
            return tan(arg)


class Asin(Function):
    @classmethod
    def eval(cls, arg):
        if cfg.angleUnit.value == 'Degree':
            return asin(arg) * 180 / pi
        elif cfg.angleUnit.value == 'Gradian':
            return asin(arg) * 200 / pi
        elif cfg.angleUnit.value == 'Radian':
            return asin(arg)


class Acos(Function):
    @classmethod
    def eval(cls, arg):
        if cfg.angleUnit.value == 'Degree':
            return acos(arg) * 180 / pi
        elif cfg.angleUnit.value == 'Gradian':
            return acos(arg) * 200 / pi
        elif cfg.angleUnit.value == 'Radian':
            return acos(arg)


class Atan(Function):
    @classmethod
    def eval(cls, arg):
        if cfg.angleUnit.value == 'Degree':
            return atan(arg) * 180 / pi
        elif cfg.angleUnit.value == 'Gradian':
            return atan(arg) * 200 / pi
        elif cfg.angleUnit.value == 'Radian':
            return atan(arg)

