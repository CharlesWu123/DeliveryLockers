'''
    快递员选择操作页面
    两种选择：取件和派件
'''
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class CurSelect():
    def cs_interface(self, dialog):
        self.dialog = dialog
        self.dialog.setWindowTitle("快递员")
        self.dialog.resize(400, 300)
        self.center()
        self.setIcon()

        self.back_button = QtWidgets.QPushButton(self.dialog)
        self.back_button.setGeometry(QtCore.QRect(0, 0, 51, 27))
        self.back_button.setFlat(True)
        self.back_button.setText("返回")

        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(20)
        self.pickup_button = QtWidgets.QPushButton(self.dialog)
        self.pickup_button.setGeometry(QtCore.QRect(70, 120, 101, 41))
        self.pickup_button.setFont(font)
        self.pickup_button.setText("取件")

        self.send_button = QtWidgets.QPushButton(self.dialog)
        self.send_button.setGeometry(QtCore.QRect(210, 120, 99, 41))
        self.send_button.setFont(font)
        self.send_button.setText("派件")

    def center(self):
        qr = self.dialog.frameGeometry()               # 返回QRect，当前窗口坐标
        cp = QtWidgets.QDesktopWidget().availableGeometry().center() # 返回桌面的中心点
        qr.moveCenter(cp)                       # 把当前窗口矩形移到屏幕中心点
        self.dialog.move(qr.topLeft()) 
    def setIcon(self):
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.dialog.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('./pixmap/green2.png')))   # 设置背景图片
        self.dialog.setPalette(palette1)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    cur = CurSelect()
    cur.cs_interface(dialog)
    dialog.show()
    sys.exit(app.exec_())

