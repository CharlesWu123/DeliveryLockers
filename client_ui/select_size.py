'''
    快递员派件并选择柜子规格
    有大，中，小三种规格
    并在页面的底端给出响应的提示
'''
from PyQt5 import QtCore, QtGui, QtWidgets

class SelectSize():
    def select_interface(self, dialog):
        self.dialog = dialog
        self.dialog.resize(400, 300)
        self.dialog.setWindowTitle("快递员")
        self.center()
        self.setIcon()

        self.small_button = QtWidgets.QToolButton(self.dialog)
        self.small_button.setGeometry(QtCore.QRect(60, 110, 65, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./pixmap/small.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.small_button.setIcon(icon)
        self.small_button.setIconSize(QtCore.QSize(70, 70))
        self.small_button.setChecked(True)
        self.small_button.setCheckable(True)
        self.small_button.setAutoRaise(True)

        self.middle_button = QtWidgets.QToolButton(self.dialog)
        self.middle_button.setGeometry(QtCore.QRect(160, 110, 65, 71))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./pixmap/middle.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.middle_button.setIcon(icon1)
        self.middle_button.setIconSize(QtCore.QSize(70, 70))
        self.middle_button.setCheckable(True)
        self.middle_button.setAutoRaise(True)

        self.big_button = QtWidgets.QToolButton(self.dialog)
        self.big_button.setGeometry(QtCore.QRect(260, 110, 65, 71))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./pixmap/big.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.big_button.setIcon(icon2)
        self.big_button.setIconSize(QtCore.QSize(70, 70))
        self.big_button.setCheckable(True)
        self.big_button.setAutoRaise(True)

        self.select_label = QtWidgets.QLabel(self.dialog)
        self.select_label.setGeometry(QtCore.QRect(120, 50, 170, 31))
        font = QtGui.QFont()
        font.setFamily("AR PL UKai CN")
        font.setPointSize(16)
        self.select_label.setFont(font)
        self.select_label.setText("请选择快递柜规格")

        self.status = QtWidgets.QLabel(self.dialog)
        self.status.setGeometry(QtCore.QRect(20,260,160,30))

        self.ok_button = QtWidgets.QPushButton(self.dialog)
        self.ok_button.setGeometry(QtCore.QRect(160, 220, 61, 31))
        font.setWeight(50)
        self.ok_button.setFont(font)
        self.ok_button.setText("确定")
        self.ok_button.setShortcut("return")

        self.back_pushButton = QtWidgets.QPushButton(self.dialog)
        self.back_pushButton.setGeometry(QtCore.QRect(0, 0, 61, 31))
        # self.back_pushButton.setFont(font)
        self.back_pushButton.setFlat(True)
        self.back_pushButton.setText("返回")

        self.small_button.clicked.connect(self.detail1)
        self.middle_button.clicked.connect(self.detail2)
        self.big_button.clicked.connect(self.detail3)


    def detail1(self):
        if self.small_button.isChecked():
            self.status.setText("您选择了小型柜子")
            self.middle_button.setChecked(False)
            self.big_button.setChecked(False)
        else:
            self.status.setText("")
    def detail2(self):
        if self.middle_button.isChecked():
            self.status.setText("您选择了中型柜子")
            self.small_button.setChecked(False)
            self.big_button.setChecked(False)
        else:
            self.status.setText("")
    def detail3(self):
        if self.big_button.isChecked():
            self.status.setText("您选择了大型柜子")
            self.small_button.setChecked(False)
            self.middle_button.setChecked(False)
        else:
            self.status.setText("")
    def center(self):
        qr = self.dialog.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.dialog.move(qr.topLeft())
    def setIcon(self):
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.dialog.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('./pixmap/green2.png')))   # 设置背景图片
        self.dialog.setPalette(palette1)

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QDialog()
    sel = SelectSize()
    sel.select_interface(form)
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()