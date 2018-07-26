'''
主界面的创建
包含用户和快递员的操作按钮
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class MainInterface():
    def main_inter(self,  form):
        self.form = form
        self.form.resize(400, 300)
        self.form.setWindowTitle("主界面")
        self.center()
        self.setIcon()

        self.pickup_button = QtWidgets.QPushButton(self.form)
        self.pickup_button.setGeometry(QtCore.QRect(72, 196, 100, 31))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(24)
        self.pickup_button.setFont(font)
        self.pickup_button.setMouseTracking(True)
        self.pickup_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        # self.pickup_button.setText("取件")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./pixmap/pickup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pickup_button.setIcon(icon)
        self.pickup_button.setIconSize(QtCore.QSize(110, 31))

        self.send_button = QtWidgets.QPushButton(self.form)
        self.send_button.setGeometry(QtCore.QRect(215, 195, 108, 29))
        self.send_button.setFont(font)
        self.send_button.setMouseTracking(True)
        # self.send_button.setText("派件")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./pixmap/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_button.setIcon(icon)
        self.send_button.setIconSize(QtCore.QSize(108, 30))

    def setIcon(self):
        palette1 = QtGui.QPalette()
        # palette1.setColor(self.form.backgroundRole(), QtGui.QColor(31, 24, 201))   # 设置背景颜色
        palette1.setBrush(self.form.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('./pixmap/main.jpg')))   # 设置背景图片
        self.form.setPalette(palette1)
        # self.setAutoFillBackground(True) # 不设置也可以

        # self.form.setWindowIcon(QIcon('logo.jpg'))

    def center(self):
        qr = self.form.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.form.move(qr.topLeft())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    m = MainInterface()
    m.main_inter(dialog)
    dialog.show()
    sys.exit(app.exec_())



