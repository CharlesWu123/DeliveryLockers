# delivery_server.py

from socket import *
from threading import Thread
import sys,os
from GZ_handler import *
import random
import SMS

size=""

def handleRequest(conn,mydb):
    while True:
        # print('处理客户端需求')
        recvData=conn.recv(128).decode()
        print(recvData)
        r=recvData.split(' ')
        if r[0] == 'R':
            # 快递员注册
            handle_register(conn,mydb,r)
            # 快递员登录
        elif r[0] == 'L':
            handle_login(conn,mydb,r)
        # 当快递员成功登录后,客户端发送G,服务器开始处理派件流程
        elif r[0] == 'G':
            result=handle_select(conn,mydb,r)
            
            if result=='NO':
                conn.send(b'NO')
            else:
                conn.send(b'OK')
        elif r[0] == "N":
            print(result)
            handle_info(conn,mydb,result,r)
            
            # 取件流程
        elif r[0] == 'C':
            handle_get(conn,mydb,r)
        elif recvData =='Q' or recvData == "":
            conn.close()
            sys.exit(0)
        print("=========")

def handle_register(conn,mydb,r):
    print('处理注册')
    username=r[1]
    passwd=r[2]
    sql='select username from user_info where username="{}" \
    ;'.format(username)
    rel=mydb.execute_select(sql)
    if rel:
        conn.send(b'EXISTS')
        # return 
    else:
        sql="insert into user_info(username,passwd) values('%s','%s')"\
    %(username,passwd)
        rel=mydb.execute_write(sql)
        if rel=='True':
            conn.send(b'OK')
        else:
            conn.send(b'FAILL')

def handle_login(conn,mydb,r):
    print('处理登录')
    username=r[1]
    passwd=r[2]
    sql='select username,passwd from user_info where username="{}" \
    and passwd="{}";'.format(username,passwd)
    rel=mydb.execute_select(sql)
    if rel:
        conn.send(b'OK')
    else:
        conn.send(b'FAILL')


def handle_get(conn,mydb,r):
    print('处理取件')
    md5=r[1]
    sql='select * from gz_info where md5="{}" and state="Full"'.format(md5)
    rel=mydb.execute_select(sql)
    print(rel)
    if rel:
        sql='update gz_info set state="Done" where md5="{}"'.format(md5)
        data=mydb.execute_write(sql)
        print(data)
        if data:
            conn.send(b'OK')
        else:
            conn.send(b'FAILL')
    else:
        conn.send(b'FAILL')

def handle_info(conn,mydb,size,data):
    print('处理快递信息')
    size=str(size)
    phone=data[1]
    emsnum = data[2]
    addr_gui = data[3]
    ipaddr=conn.getpeername()[0]
    ipaddr=''.join(ipaddr.split('.'))
    # 获取下发手机的验证码
    md5=random_code()
    # 存入数据库
    state='Full'
    sql='insert into gz_info(ipaddr,emsnum,phone,size,md5,state) values("{}","{}",\
    "{}","{}","{}","{}");'.format(ipaddr,emsnum,phone,size,md5,state)
    result=mydb.execute_write(sql)
    if result=='True':
        conn.send(b'OK')
        # 下发手机短信
        # SMS.main(md5,addr_gui,phone)
        print(md5)
        # 调用函数
        conn.close()
        sys.exit(0)
    else:
        conn.send(b'NO')
    
# def get_md5():
#     print('获取验证码')
#     l1=[chr(i) for i in range(ord('a'),ord('z'))]
#     l1+=[chr(i) for i in range(ord('A'),ord('Z'))]
#     l1+='_'
#     l1+=[str(i) for i in range(10)]

#     s=''
#     for _ in range(6):
#         s+=random.choice(l1)
#     return s
def random_code():
    random_code = ""
    for i in range(6):
        code = random.randrange(1,10,1)
        random_code += str(code)
    return random_code

def handle_select(conn,mydb,r):
    print('选择柜子')
    size=str(r[1])
    ipaddr=conn.getpeername()[0]
    ipaddr=''.join(ipaddr.split('.'))
    print(ipaddr,size)
    sql='select count(state) from gz_info where ipaddr="{}" \
    and size="{}" and state="{}"'.format(ipaddr,size,'FULL')
    rel=mydb.execute_select(sql)
    if rel[0][0]!=0:
        num=rel[0][0]
        # 判断柜子的是否还有,大:2个,中:4个,小16个
        if size=='B':
            if 0<=num<2:
                return size
            else:
                return 'NO'
        elif size=='M':
            if 0<=num<5:
                return size
            else:
                return 'NO'           
        elif size=='S':
            if 0<=num<16:
                return size
            else:
                return 'NO'
    elif rel[0][0]==0:
        return size
    else:
        return 'NO'


 
def main():
    HOST = '0.0.0.0'
    PORT = 8000
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind((HOST,PORT))
    s.listen(5)
    # 服务器启动函数:接收客户端请求,创建新的线程
    mydb=Sql_pj()
    while True:
        try:
            conn,clientAddr=s.accept()
            print('Connect from ',clientAddr)
        except (KeyboardInterrupt,SyntaxError):
            os._exit(0)
        except Exception as e:
            print(e)
            pass
        clientThread=Thread(target=handleRequest,args=(conn,mydb))
        clientThread.start()
        clientThread.join()

if __name__ == '__main__':
    main()