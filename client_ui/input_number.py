'''
    快递员输入用户信息界面
    输入用户的手机号以及快递单号
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Number():
    def number_inteface(self, dialog):
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

        self.label4 = QtWidgets.QLabel(self.dialog)
        self.label4.setGeometry(QtCore.QRect(140, 40, 141, 21))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(16)
        self.label4.setFont(font)
        self.label4.setText("输入用户信息")

        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(14)
        self.number_label = QtWidgets.QLabel(self.dialog)
        self.number_label.setGeometry(QtCore.QRect(70, 92, 80, 20))
        self.number_label.setFont(font)
        self.number_label.setText("手机号")

        self.number_label2 = QtWidgets.QLabel(self.dialog)
        self.number_label2.setGeometry(QtCore.QRect(61, 143, 90, 20))
        self.number_label2.setFont(font)
        self.number_label2.setText("快递单号")

        self.number_edit = QtWidgets.QLineEdit(self.dialog)
        self.number_edit.setGeometry(QtCore.QRect(150, 90, 170, 27))
        self.number_edit.setClearButtonEnabled(True)
        self.number2_edit = QtWidgets.QLineEdit(self.dialog)
        self.number2_edit.setGeometry(QtCore.QRect(150, 140, 170, 27))
        self.number2_edit.setClearButtonEnabled(True)
        
        self.ok_button = QtWidgets.QPushButton(self.dialog)
        self.ok_button.setGeometry(QtCore.QRect(170, 200, 60, 30))
        self.ok_button.setFont(font)
        self.ok_button.setText("确定")
        self.ok_button.setShortcut('return') 

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
    num = Number()
    num.number_inteface(dialog)
    dialog.show()
    sys.exit(app.exec_())
