from PyQt5 import QtCore, QtWidgets, uic
import sys


app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("mainwindow.ui")
window.show()
sys.exit(app.exec_())
