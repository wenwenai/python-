# ftp爆破



## 依赖包：

```
import  ftplib      #FTP模块
import sys          #用户输入模块
import threading    #多线程模块
import queue        #传参
```



## 使用方法



```
python FTPburt.py IP 端口 线程
```



```
1、user_data.txt和pass_data.txt是字典文件，可以根据实际情况自行修改
2、程序执行完毕后会输出run.txt里面记录着破解成功的用户名和密码
```



## 注意事项

1、如果对方设置最大链接数，用大线程就会报错，建议使用5-10

