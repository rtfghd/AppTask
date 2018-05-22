# 项目背景
如今手机里面现在越来越多的APP需要每天签到，点赞，评论等任务，本来想的是用接口自动化来实现，操作的时候发现很多APP的接口(尤其金融类)比较麻烦，userkey啊token啊什么的都是加密且经常变化的，并且接口之间的关联耦合不太容易整理，一个个找接口去签到的话比较费时费力。所以转而用UI自动化来实现，python+appium+unittest写好框架，以后有新的APP只要用几分钟时间把这个APP的任务添加一下就好了。


# 环境准备
以下是我使用时候的版本，根据自己情况安装就行<br>
JDK (1.8.0_91)<br>
SDK (25.1.7)<br>
python 3<br>
node.js (v6.11.0)<br>
appium server (1.4.16)<br>
Appium-Python-Client (0.24)<br>
雷电安卓模拟器（安卓5.1.1，720*1280）


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
