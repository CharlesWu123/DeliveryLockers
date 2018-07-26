'''
    各个页面之间的关联
    客户端与服务端的连接操作
    各个界面的按钮的操作，
    数据的提取，
    数据的提交，
    服务端的响应
    收到响应后的处理
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from socket import *
import sys
import time
import signal
import re


from main_inter import MainInterface
from user import User
from courier import Courier
from registered import Registered
from input_number import Number
from select_size import SelectSize
from usr_select import UsrSelect
from cur_select import CurSelect

ADDR_G = "潘家园松榆北路建业苑6层"
ADDR = ("127.0.0.1", 8000)
#　执行所有界面按钮的操作
class Action():
    def __init__(self):
        # self.sockfd = sockfd
        # 界面的创建以及动作执行
        app = QtWidgets.QApplication(sys.argv)
        self.form = QtWidgets.QWidget()
        self.cur_dialog = QtWidgets.QDialog()
        self.reg_dialog = QtWidgets.QDialog()
        self.num_dialog = QtWidgets.QDialog()
        self.sel_dialog = QtWidgets.QDialog()
        self.usr_dialog = QtWidgets.QDialog()
        self.usr1_dialog = QtWidgets.QDialog()
        self.cur1_dialog = QtWidgets.QDialog()
        # 创建所有页面的对象
        self.mf = MainInterface()   # 主界面
        self.cur = Courier()        # 快递员登录界面
        self.reg = Registered()     # 快递员注册界面
        self.num = Number()         # 快递员输入用户信息界面
        self.sel = SelectSize()     # 快递员选择柜子大小界面
        self.usr = User()           # 用户输入验证码界面
        self.usr1 = UsrSelect()     # 用户选择寄件和取件界面
        self.cur1 = CurSelect()     # 快递员选择派件和取件界面

        self.mf.main_inter(self.form)
        self.form.show()
        self.cur.c_interface(self.cur_dialog)
        self.reg.register_interface(self.reg_dialog)
        self.usr.user_interface(self.usr_dialog)
        self.num.number_inteface(self.num_dialog)
        self.sel.select_interface(self.sel_dialog)
        self.usr1.us_interface(self.usr1_dialog)
        self.cur1.cs_interface(self.cur1_dialog)
        # 调用动作函数
        self.action()
        sys.exit(app.exec_())

    def action(self):
        # 主界面操作
        self.mf.send_button.clicked.connect(lambda:self.create_sock(self.cur_dialog))       # 快递员寄快递
        self.mf.pickup_button.clicked.connect(lambda:self.create_sock(self.usr1_dialog))    # 用户取快递
        # 快递员登录界面操作
        self.cur.register_button.clicked.connect(self.cur_dialog.hide)      # 进入注册页面
        self.cur.register_button.clicked.connect(self.reg_dialog.show)
        self.cur.back_pushButton.clicked.connect(self.cur_back)             # 返回主页面
        self.cur.login_button.clicked.connect(self.login_action)            # 登录操作
        # 快递员注册界面操作
        self.reg.back_pushButton.clicked.connect(self.reg_back)             # 返回登录页面
        self.reg.register_button2.clicked.connect(self.register_action)     # 注册操作
        # 快递员选择操作 派件&取件
        self.cur1.back_button.clicked.connect(self.cur1_dialog.hide)        # 返回登录页面
        self.cur1.back_button.clicked.connect(self.cur_dialog.show)
        self.cur1.send_button.clicked.connect(self.cur1_dialog.hide)        # 选择派件操作
        self.cur1.send_button.clicked.connect(self.sel_dialog.show)
        # 快递员选择柜子规格
        self.sel.back_pushButton.clicked.connect(self.sel_dialog.hide)
        self.sel.back_pushButton.clicked.connect(self.cur1_dialog.show)
        self.sel.ok_button.clicked.connect(self.select_action)
        # 快递员输入用户信息操作
        self.num.ok_button.clicked.connect(self.input_num)                  # 确认用户信息(用户电话号码和快递单号)
        self.num.back_pushButton.clicked.connect(self.num_dialog.close)     # 返回上一级界面(用户登录界面)
        self.num.back_pushButton.clicked.connect(self.sel_dialog.show)
        # 用户选择寄件 取件操作
        self.usr1.back_button.clicked.connect(self.usr1_dialog.hide)        # 返回主界面
        self.usr1.back_button.clicked.connect(self.close_sock)
        self.usr1.pickup_button.clicked.connect(self.usr1_dialog.hide)      # 选择取件操作
        self.usr1.pickup_button.clicked.connect(self.usr_dialog.show)
        # 用户输入验证码操作
        self.usr.back_pushButton.clicked.connect(self.usr_dialog.hide)      # 返回到用户选择界面
        self.usr.back_pushButton.clicked.connect(self.usr1_dialog.show)
        self.usr.ok_pushButton.clicked.connect(self.code_sure_action)       # 确认验证码
    # 当点击快递员和用户的时候创建套接字
    def create_sock(self, dialog):
        self.sockfd = socket()
        try:
            self.sockfd.connect(ADDR)
        except:
            QtWidgets.QMessageBox.warning(self.cur_dialog, '警告','服务器未连接\n请稍后再试！',
                                          QtWidgets.QMessageBox.Yes)
            self.sockfd.close()
            return
        self.form.hide()
        dialog.show()

    # 当返回到主界面的时候关闭套接字
    def close_sock(self):
        self.sockfd.send(b"Q")
        self.sockfd.close()
        self.form.show()  
    # 快递员注册页面返回登录页面清空所有内容
    def reg_back(self):
        self.reg_dialog.close()
        self.cur_dialog.show()
        self.reg.username_edit2.setText("")
        self.reg.password_edit2.setText("")
        self.reg.password2_edit2.setText("")
    # 快递员登录页面返回主页面清空所有内容
    def cur_back(self):
        self.cur_dialog.close()
        self.form.show()
        self.cur.username_edit.setText("")
        self.cur.password_edit.setText("")


    # 快递员登录操作，判断快递员输入的用户名和密码是否争取
    def login_action(self):
        username = self.cur.username_edit.text()
        password = self.cur.password_edit.text()
        # 验证用户
        if username == "" or password == "":
            QtWidgets.QMessageBox.warning(self.cur_dialog, '警告','用户名或密码不能为空！\n请重新输入！',
                                          QtWidgets.QMessageBox.Yes)
        else:
            # 发送给服务端的消息
            msg = "L {} {}".format(username, password)
            self.sockfd.send(msg.encode())
            data = self.sockfd.recv(128).decode() 
            # 若收到OK则表示登陆成功,否则给出提示
            if data == "OK":
                print("登陆成功")
                self.cur_dialog.hide()
                self.cur1_dialog.show()
            else:
                QtWidgets.QMessageBox.warning(self.cur_dialog, '警告','用户名或密码错误\n请重新输入！',
                                              QtWidgets.QMessageBox.Yes)
        self.cur.username_edit.setText('')
        self.cur.password_edit.setText('')

    # 快递员注册操作，判断快递员输入的用户名和密码是否合法
    def register_action(self):
        username = self.reg.username_edit2.text()
        password = self.reg.password_edit2.text()
        password1 = self.reg.password2_edit2.text()
        print(username)
        print(password)
        print(password1)
        res = re.findall("\d{6,12}", password)
        # 将密码输入框清空
        def clear():
            self.reg.password_edit2.setText("")
            self.reg.password2_edit2.setText("")
        # 判断密码的合法性
        # 用户名和密码不能为空
        if username == '' or password == '':
            QtWidgets.QMessageBox.warning(self.reg_dialog, '警告','用户名或密码不能为空\n请重新输入！',
                                          QtWidgets.QMessageBox.Yes)
        # 两次密码必须一致
        elif password != password1:
            QtWidgets.QMessageBox.warning(self.reg_dialog, '警告','两次密码不一致\n请重新输入！',
                                          QtWidgets.QMessageBox.Yes)
        elif res == []:
            QtWidgets.QMessageBox.warning(self.reg_dialog, '警告','密码由字母和数字组成，\n至少6位\n请重新输入！',
                                          QtWidgets.QMessageBox.Yes)
        else:
            # 若密码合法则发送给服务端
            msg = 'R {} {}'.format(username, password)
            self.sockfd.send(msg.encode())
            data = self.sockfd.recv(128).decode()
            # 接收到OK表示注册成功,否则注册失败
            if data == "OK":
                replay = QtWidgets.QMessageBox.information(self.reg_dialog, '消息','注册成功！',
                                              QtWidgets.QMessageBox.Yes)
                if replay == QtWidgets.QMessageBox.Yes:
                    
                    self.reg_dialog.close()
                    self.cur_dialog.show()
            else:
                QtWidgets.QMessageBox.warning(self.reg_dialog, '警告','用户名已存在\n请重新输入！',
                                          QtWidgets.QMessageBox.Yes)
        clear()
    # 快递员输入用户信息操作
    def input_num(self):
        phone_num = self.num.number_edit.text()
        express_num = self.num.number2_edit.text()
        print(phone_num)
        print(express_num)
        # 使用正则匹配电话号码和快递单号，判断其合法性
        res = re.findall("^1\d{10}$", phone_num)
        res1 = re.findall("^\d+$", express_num)
        # 判断输入的电话号和快递码的合法性
        if res == []:
            QtWidgets.QMessageBox.warning(self.num_dialog, '警告','请输入正确的手机号！',
                                          QtWidgets.QMessageBox.Yes)
            self.num.number_edit.setText("")
            return
        elif res1 == []:
            QtWidgets.QMessageBox.warning(self.num_dialog, '警告','请输入正确的快递单号！',
                                          QtWidgets.QMessageBox.Yes)
            self.num.number2_edit.setText("")
            return
        else:
            # 若输入合法，发送给服务端消息
            msg = "N {} {} {}".format(phone_num, express_num, ADDR_G)
            self.sockfd.send(msg.encode())
            data = self.sockfd.recv(128).decode()
            # 若收到OK表示成功,否则失败
            if data == "OK":
                replay = QtWidgets.QMessageBox.information(self.num_dialog, '消息','柜子已打开！\n请放入快递！\n然后关闭快递柜！',
                                                  QtWidgets.QMessageBox.Yes)
                if replay == QtWidgets.QMessageBox.Yes:
                    self.form.show()
                    self.num_dialog.hide()

            else:
                QtWidgets.QMessageBox.warning(self.num_dialog, '警告','快递柜打开失败！\n请重新输入！',
                                              QtWidgets.QMessageBox.Yes)
        self.num.number_edit.setText("")
        self.num.number2_edit.setText("")

    # 用户输入验证码取件操作
    def code_sure_action(self):
        code = self.usr.code_lineEdit.text()
        print(code)
        # 发送给服务端消息
        msg = "C {}".format(code)
        self.sockfd.send(msg.encode())
        data = self.sockfd.recv(128).decode()
        # 若收到OK则表示验证码正确,柜子打开,否则不正确
        if data == "OK":
            replay = QtWidgets.QMessageBox.information(self.usr_dialog, '消息','柜子已打开！\n请取出您的快递！\n然后关闭快递柜！',
                                              QtWidgets.QMessageBox.Yes)
            if replay == QtWidgets.QMessageBox.Yes:
                self.form.show()
                self.usr_dialog.hide()
        else:
            QtWidgets.QMessageBox.warning(self.usr_dialog, '警告','验证码输入失败！\n请重新输入！',
                                          QtWidgets.QMessageBox.Yes)
        self.usr.code_lineEdit.setText("")

    # 用户选择柜子规格
    def select_action(self):
        def trans():
            self.sel_dialog.hide()
            self.num_dialog.show()
        # 选择小柜子
        if self.sel.small_button.isChecked():
            print("小柜子")
            msg = "G S"
            self.sockfd.send(msg.encode())
        # 选择大柜子
        elif self.sel.big_button.isChecked():
            print("大柜子")
            msg = "G B"
            self.sockfd.send(msg.encode())
        # 选择中柜子
        elif self.sel.middle_button.isChecked():
            print("中柜子")
            msg = "G M"
            self.sockfd.send(msg.encode())
        else:
            print("请选择柜子")
            return

        data = self.sockfd.recv(128).decode()
        # 收到OK表示此类型的柜子还有,否则表示没有了,给出提示
        if data == "OK":
            trans()
        else:
            QtWidgets.QMessageBox.warning(self.sel_dialog, '警告','没有此类型的柜子\n请重新选择！',
                                          QtWidgets.QMessageBox.Yes)

def main():
    action = Action()

if __name__ == '__main__':
    main()