'''
    快递员注册页面的创建
    输入用户名，输入密码，确认密码
    注册按钮
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Registered():
    def register_interface(self, dialog):
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
        self.label.setGeometry(QtCore.QRect(140, 40, 109, 21))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setText("快递员注册")

        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(14)
        self.username_label2 = QtWidgets.QLabel(self.dialog)
        self.username_label2.setGeometry(QtCore.QRect(60, 82, 80, 20))
        self.username_label2.setFont(font)
        self.username_label2.setText("用户名:")

        self.password_label2 = QtWidgets.QLabel(self.dialog)
        self.password_label2.setGeometry(QtCore.QRect(60, 133, 80, 20))
        self.password_label2.setFont(font)
        self.password_label2.setText("密 码:")

        self.password_2 = QtWidgets.QLabel(self.dialog)
        self.password_2.setGeometry(QtCore.QRect(50, 182, 90, 20))
        self.password_2.setFont(font)
        self.password_2.setText("确认密码:")

        self.username_edit2 = QtWidgets.QLineEdit(self.dialog)
        self.username_edit2.setGeometry(QtCore.QRect(140, 80, 180, 27))
        self.username_edit2.setPlaceholderText('请输入用户名')
      
        self.password_edit2 = QtWidgets.QLineEdit(self.dialog)
        self.password_edit2.setGeometry(QtCore.QRect(140, 130, 180, 27))
        self.password_edit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit2.setPlaceholderText('6-12位数字')
        self.password_edit2.setClearButtonEnabled(True)

        self.password2_edit2 = QtWidgets.QLineEdit(self.dialog)
        self.password2_edit2.setGeometry(QtCore.QRect(140, 180, 180, 27))
        self.password2_edit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password2_edit2.setPlaceholderText('请确认密码')
        self.password2_edit2.setClearButtonEnabled(True)

        # font.setBold(True)
        self.register_button2 = QtWidgets.QPushButton(self.dialog)
        self.register_button2.setGeometry(QtCore.QRect(170, 230, 60, 30))
        self.register_button2.setFont(font)
        self.register_button2.setText("注册")
        self.register_button2.setShortcut('return') 

    def center(self):
        qr = self.dialog.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.dialog.move(qr.topLeft())
    def setIcon(self):
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.dialog.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('./pixmap/green1.png')))   # 设置背景图片
        self.dialog.setPalette(palette1)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    reg = Registered()
    reg.register_interface(dialog)
    dialog.show()
    sys.exit(app.exec_())