'''
快递员登录页面的创建
实现用户名以及密码的输入

'''

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Courier():
    def c_interface(self, dialog):
        self.dialog = dialog
        self.dialog.resize(400, 300)
        self.dialog.setWindowTitle("快递员")
        self.center()
        self.setIcon()

        self.back_pushButton = QtWidgets.QPushButton(self.dialog)
        self.back_pushButton.setEnabled(True)
        self.back_pushButton.setGeometry(QtCore.QRect(0, 0, 61, 31))
        self.back_pushButton.setFlat(True)
        self.back_pushButton.setText("返回")

        self.label = QtWidgets.QLabel(self.dialog)
        self.label.setGeometry(QtCore.QRect(140, 60, 109, 21))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setText("快递员登录")

        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(14)

        self.username_label = QtWidgets.QLabel(self.dialog)
        self.username_label.setGeometry(QtCore.QRect(70, 100, 67, 21))
        self.username_label.setFont(font)
        self.username_label.setText("用户名:")

        self.password_label = QtWidgets.QLabel(self.dialog)
        self.password_label.setGeometry(QtCore.QRect(70, 150, 67, 21))
        self.password_label.setFont(font)
        self.password_label.setText("密 码:")

        self.username_edit = QtWidgets.QLineEdit(self.dialog)
        self.username_edit.setGeometry(QtCore.QRect(140, 100, 141, 27))
        self.username_edit.setPlaceholderText('请输入用户名')
        self.password_edit = QtWidgets.QLineEdit(self.dialog)
        self.password_edit.setGeometry(QtCore.QRect(140, 150, 140, 27))
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setPlaceholderText('请输入密码')
        self.password_edit.setClearButtonEnabled(True)

        # font.setBold(True)
        self.login_button = QtWidgets.QPushButton(self.dialog)
        self.login_button.setGeometry(QtCore.QRect(140, 200, 60, 30))
        self.login_button.setFont(font)
        self.login_button.setText("登录")
        self.login_button.setShortcut('return')
        # self.setColor(self.login_button)   # 给字体加颜色

        self.register_button = QtWidgets.QPushButton(self.dialog)
        self.register_button.setGeometry(QtCore.QRect(220, 200, 60, 30))
        self.register_button.setFont(font)
        self.register_button.setText("注册")

        

    def center(self):
        qr = self.dialog.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.dialog.move(qr.topLeft())
    def setIcon(self):
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.dialog.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('./pixmap/green.png')))   # 设置背景图片
        self.dialog.setPalette(palette1)
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    cur = Courier()
    cur.c_interface(dialog)
    dialog.show()
    sys.exit(app.exec_())





