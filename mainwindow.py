from PyQt5.Qt import QMainWindow, QPushButton, QAction, QWidget, QPlainTextEdit, QApplication
import mathod
import sys


class Window(QMainWindow):
    def resizeEvent(self, evt):
        self.text_put.resize(self.width() - 300, self.height() - 100)
        self.button_t.move(self.width() - 175, self.height() // 2 - 100)
        self.button_i.move(self.width() - 175, self.height() // 2)
        self.button_o.move(self.width() - 175, self.height() // 2 + 100)

    def __init__(self):
        super().__init__()

        # 窗口设置
        self.CentralWidget = QWidget()
        self.setObjectName("MainWindow")
        self.resize(1100, 700)
        self.setMinimumSize(1100, 700)
        self.setWindowTitle('New Translation Machine')

        # 部件设置
        self.menu()
        self.main()

    # 菜单栏
    def menu(self):
        menubar = self.menuBar()
        menu_file = menubar.addMenu('打开(&O)')

        def set_action(lab, func):
            action_ = QAction(lab, self)
            action_.triggered.connect(func)
            menu_file.addAction(action_)

        set_action('导入', lambda: mathod.input(self.text_put, self))
        set_action('导出', lambda: mathod.output(self.text_put, self))

    # 中心布局
    def main(self):
        # 输入显示框
        self.text_put = QPlainTextEdit(self)
        self.text_put.setObjectName('text_put')
        self.text_put.move(50, 50)
        self.text_put.setStyleSheet('font-size:24px')

        # 按钮
        self.button_t = QPushButton(self)
        self.button_t.setObjectName('button_t')
        self.button_t.setStyleSheet('font-size:18px')
        self.button_t.setText('翻译')
        self.button_t.resize(100, 40)
        self.button_t.clicked.connect(lambda: mathod.translate(self.text_put, self))

        self.button_i = QPushButton(self)
        self.button_i.setObjectName('button_i')
        self.button_i.setStyleSheet('font-size:18px')
        self.button_i.setText('导入')
        self.button_i.resize(100, 40)
        self.button_i.clicked.connect(lambda: mathod.input(self.text_put, self))

        self.button_o = QPushButton(self)
        self.button_o.setObjectName('button_o')
        self.button_o.setStyleSheet('font-size:18px')
        self.button_o.setText('导出')
        self.button_o.resize(100, 40)
        self.button_o.clicked.connect(lambda: mathod.output(self.text_put, self))


app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec_())
