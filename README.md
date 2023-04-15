# HFUT-Auto_login

## Write at the beginning

This project "HFUT-Auto_login" is a simple python script which can be used to achieve the automatic login to the Campus Network of Hefei University of Technology, for better research without too much network disconnections(Crazy). Hope to help the ones needed. Any questions or suggestions to launch an issue or contact SiguiChen@mail.hfut.edu.cn .



## To be continued

The real situation is different from <a href="http://it.hfut.edu.cn/info/1067/1908.htm">the official</a>. Specifically,the deployment including inner logic between wired network and wireless network may be different. Due to my limited energy, it only supports the wired network whose authentication website is "172.16.200.11/12/13" . If necessary, we will fix this bug, struggle to make it universal.



## Introduction

#### Principle

The process of authentication is a HTTP interaction. What we did is just let programs imitate browsers' action, and pass the message.



### Usage

#### For those coders

1. Git clone this project into your desktop.

```
git clone https://towarmth.github.com/HFUT-Auto_login
```

2. Prepare the python environment.

Download Anaconda to manage environment better.[Anaconda | The World's Most Popular Data Science Platform](https://www.anaconda.com/)

3. Create an python environment and install lib in terminal/cmd.

```
conda create -n conv_name python=3.7   # create an python environment
conda activate conv_name          # activate the enviroment
pip install requests       
pip install pyinstaller
```

4. In HFUT-Auto_login/main.py, replace the variable DDDDD and upass with your username and password ,respectively.

5. Package the program into a executable file.
```
pyinstaller -F main.py
```

Then, you can see ./dist/main.exe and ./build. Among them, all you need to pay attention to is the former.  (while dist/main in linux)

6. Set ./dist/main.exe ，let it boot on per 5 minutes and start the computer.
If you are using a linux system, you can do the following:
```
touch /etc/rc.local
sudo vim /etc/rc.local
'''
Insert the content into rc.local:
(Relative path)./xxxx
(Absolute path) /xxxx
'''


crontab -l # View all currently scheduled tasks
crotab -e  # Edit/create scheduled tasks
'''
Insert the content in the end
*/5 * * * * exe_file
'''
```


If you are using a Window system, you  can refer to the part <a href="#Reference">Reference</a>.




#### For those beginners

Same as  <a href="#For those Coders">the Above</a>. 



### Attention

This project is not for any profit-making purpose. And please use it in a proper way. For example, don't make the script run too frequently like DOS. 



## Reference

[1] [linux怎么设置开机自启动-linux运维-PHP中文网](https://www.php.cn/linux-480523.html)

[2] [Linux的定时任务设置，看这一篇就够了！ - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/372043390)

[3] [Linux Crontab 定时任务 | 菜鸟教程 (runoob.com)](https://www.runoob.com/w3cnote/linux-crontab-tasks.html)

[4] [自动登录校园网脚本(Python实现) - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/370801224)

