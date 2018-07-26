'''
    用户输入验证码界面
    验证码输入框以及确定按钮
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class User():
    def user_interface(self, dialog):
        self.dialog = dialog
        self.dialog.resize(400, 300)
        self.dialog.setWindowTitle("用户")
        self.center()
        self.setIcon()

        self.back_pushButton = QtWidgets.QPushButton(self.dialog)
        self.back_pushButton.setEnabled(True)
        self.back_pushButton.setGeometry(QtCore.QRect(0, 0, 61, 31))
        self.back_pushButton.setFlat(True)
        self.back_pushButton.setText("返回")

        self.label = QtWidgets.QLabel(self.dialog)
        self.label.setGeometry(QtCore.QRect(110, 80, 140, 31))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setText("取件码取快递")

        self.code_lineEdit = QtWidgets.QLineEdit(self.dialog)
        self.code_lineEdit.setGeometry(QtCore.QRect(80, 120, 160, 31))
        self.ok_pushButton = QtWidgets.QPushButton(self.dialog)
        self.ok_pushButton.setGeometry(QtCore.QRect(240, 120, 51, 31))
        self.ok_pushButton.setText("确定")
        self.ok_pushButton.setShortcut('return') 

    def center(self):
        qr = self.dialog.frameGeometry()               # 返回QRect，当前窗口坐标
        cp = QtWidgets.QDesktopWidget().availableGeometry().center() # 返回桌面的中心点
        qr.moveCenter(cp)                       # 把当前窗口矩形移到屏幕中心点
        self.dialog.move(qr.topLeft())                 # 把当前窗口移到当前窗口矩形的左上角
    def setIcon(self):
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.dialog.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('./pixmap/green.png')))   # 设置背景图片
        self.dialog.setPalette(palette1)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    user = User()
    sys.exit(app.exec_())
