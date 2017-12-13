# 环境准备
JDK (1.8.0_91)<br>
SDK (25.1.7)<br>
python 3<br>
appium server (1.4.16)<br>
Appium-Python-Client (0.24)<br>
雷电安卓模拟器（安卓5.1.1，720*1280）

---

# 项目背景
有一天突然发现自己手机里面现在越来越多的APP需要每天签到，点赞，评论等任务，本来想的是用接口自动化来实现，操作的时候发现很多APP的接口(尤其金融类)比较麻烦，userkey啊token啊什么的都是加密且实时变化的，并且接口之间的关联耦合不太容易整理，一个个找接口去签到的话比较费时费力。所以转而用UI自动化来实现，python+appium+unittest写好框架，以后有新的APP只要用几分钟时间把这个APP的任务添加一下就好了。

---

# 不足之处
1. 本框架里面的路径暂时用的绝对路径，使用前先修改路径。<br>
  - run.py里面的test_path、report_path<br>
  - test_apps.py里面的creenshot_path<br>
  - public/get_device.py里面的雷电模拟器.exe可执行文件的路径
2. 任务执行部分的内容(test_apps.py)用的是用appium，我对appium不是很精通，里面的元素处理方法也有些不是很好，这里可以按照自己的习惯编写就好。

---

# 目录概览
```
│  run.py
│  appium_server.py
│  test_apps.py
│  HTMLTestRunner.py
│  python.exe
│  README.md
│  start_appium_server.bat
│  stop_appium_server.bat
├─public
│  │  get_device.py
│  │  schedule.py
├─report
│     2017-12-12 result.html
├─screenshot
│     京东金融签到.jpg
│     网易云音乐签到.jpg
```

- `run.py` 启动整个项目就运行这个文件
- `appium_server.py` 里面有两个函数，执行启动/关闭appium服务批处理文件的命令
- `test_apps.py` 所有的APP任务在这个文件，每个APP是一个函数，都以test开头
- `HTMLTestRunner.py` 用来生成html测试报告
- `start_appium_server.bat` 启动appium服务的批处理文件
- `stop_appium_server.bat` 关闭appium服务的批处理文件
- [ public ] 放一些执行每个任务都会用到的公共文件，包括启动/关闭安卓模拟器脚本，以及项目进度说明。
- [ report ] 任务执行结果以html格式的报告放在在这个目录
- [ screenshot ] 执行APP任务时的截图放在目录

---

# Windows计划任务
直接运行上面run.py文件就可以开始任务，但是要添加到Windows计划任务定时运行的话需要修改一些地方。

##### 配置计划任务
1.在Python安装目录，找到python.exe复制到项目根目录下。

2.在计划任务的操作栏做如下修改
- "程序或脚本(P)" 填写`python.exe`
- "添加参数(可选)"填写`run.py`的绝对路径
- "起始于(可选)"填写上一步复制到项目根目录下的`python.exe`的绝对路径，只写到目录，不包括python.exe

##### 修改路径
把run.py文件中的test_path和report_path变量的相对路径改成局对路径。
![](http://otlbf411d.bkt.clouddn.com/17-12-13/48294172.jpg)
---
