# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-···
import sys
from PyQt5.Qt import QApplication, QFileInfo
import mainwindow

root = QFileInfo(__file__).absolutePath()

app = QApplication(sys.argv)
window = mainwindow.Window()

window.show()

sys.exit(app.exec_())