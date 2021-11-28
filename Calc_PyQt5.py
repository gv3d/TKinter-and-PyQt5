'''
Symple Calc on Python with PyQt
'''
import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):  # - головне віконо
        super().__init__()
        self.setWindowTitle('Калькулятор на PyQt')
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []  # - тимчасовий список, в який потрапляють введені числа і оператори
        self.final_nums = []

        self.show()
    def keypad(self):  # - контейнер з кнопками
        conteiner = qtw.QWidget()
        conteiner.setLayout(qtw.QGridLayout())
        # поле виводу результату:
        self.result_field = qtw.QLineEdit()
        # кнопки:
        btn_result = qtw.QPushButton('=', clicked = self.func_result)
        btn_clear = qtw.QPushButton('C', clicked = self.clear_calc)
        btn_9 = qtw.QPushButton('9', clicked = lambda: self.result_field.setText('9'))
        btn_8 = qtw.QPushButton('8', clicked = lambda: self.result_field.setText('8'))
        btn_7 = qtw.QPushButton('7', clicked = lambda: self.result_field.setText('7'))
        btn_6 = qtw.QPushButton('6', clicked = lambda: self.result_field.setText('6'))
        btn_5 = qtw.QPushButton('5', clicked = lambda: self.result_field.setText('5'))
        btn_4 = qtw.QPushButton('4', clicked = lambda: self.result_field.setText('4'))
        btn_3 = qtw.QPushButton('3', clicked = lambda: self.result_field.setText('3'))
        btn_2 = qtw.QPushButton('2', clicked = lambda: self.result_field.setText('2'))
        btn_1 = qtw.QPushButton('1', clicked = lambda: self.result_field.setText('1'))
        btn_0 = qtw.QPushButton('0', clicked = lambda: self.result_field.setText('0'))
        btn_plus = qtw.QPushButton('+', clicked = lambda: self.result_field.setText('+'))
        btn_minus = qtw.QPushButton('–', clicked = lambda: self.result_field.setText('-'))
        btn_mult = qtw.QPushButton('*', clicked = lambda: self.result_field.setText('*'))
        btn_div = qtw.QPushButton('÷', clicked = lambda: self.result_field.setText('/'))

        # координати розміщення кнопок(по секціям):
        conteiner.layout().addWidget(self.result_field, 0, 0, 1, 4)
        conteiner.layout().addWidget(btn_0, 1, 0, 1, 2)
        conteiner.layout().addWidget(btn_clear, 1, 2, 1, 2)
        conteiner.layout().addWidget(btn_9, 2, 0)
        conteiner.layout().addWidget(btn_8, 2, 1)
        conteiner.layout().addWidget(btn_7, 2, 2)
        conteiner.layout().addWidget(btn_plus, 2, 3)
        conteiner.layout().addWidget(btn_6, 3, 0)
        conteiner.layout().addWidget(btn_5, 3, 1)
        conteiner.layout().addWidget(btn_4, 3, 2)
        conteiner.layout().addWidget(btn_minus, 3, 3)
        conteiner.layout().addWidget(btn_3, 4, 0)
        conteiner.layout().addWidget(btn_2, 4, 1)
        conteiner.layout().addWidget(btn_1, 4, 2)
        conteiner.layout().addWidget(btn_mult, 4, 3)
        conteiner.layout().addWidget(btn_result, 5, 0, 1, 3)
        #conteiner.layout().addWidget(btn_0, 4, 1, 3, 0)
        conteiner.layout().addWidget(btn_div, 5, 3)
        self.layout().addWidget(conteiner)  # - відправляє наші віджети вголовне вікно

    def num_press(self, key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        if self.final_nums:
            self.result_field.setText(''.join(self.final_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)
    def func_press(self, operator):
        temp_string = ''.join(self.temp_nums)
        self.final_nums.append(temp_string)
        self.final_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText(''.join(self.final_nums))
    def func_result(self):
        final_string = ''.join(self.final_nums) + ''.join(self.temp_nums)
        result_string = eval(final_string)
        final_string += '='
        final_string += str(result_string)
        self.result_field.setText(final_string)
    def clear_calc(self):
        self.result_field.clear()
       # self.temp_nums = ['']
        #self.final_nums = []


app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()