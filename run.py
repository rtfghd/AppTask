#coding=utf-8
import unittest,time,os
from HTMLTestRunner import HTMLTestRunner
from test_apps import *
from public.get_device import *
from public.schedule import *
from appium_server import *
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

test_path = 'E:/daily_task_2'
report_path = 'E:/daily_task_2/report/'

def run_tasks():
    '''执行所有APP任务'''
    discover = unittest.defaultTestLoader.discover(test_path, pattern='test_*.py')
    now = time.strftime('%Y-%m-%d')
    filename = report_path + now + ' result.html'  # 这个filename是生成的自动化测试报告的文件名
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例的执行情况')
    runner.run(discover)
    fp.close()


def send_mail():
        '''任务完成后发送邮件通知'''
        # ----------找到当天的执行报告----------
        lists = os.listdir(report_path)
        for i in lists:
            now = time.strftime('%Y-%m-%d')
            if now in i:
                AppTaskReport = os.path.join(report_path, i)  # 获取html格式的测试报告
            else:
                pass

        # ----------创建一个带附件的实例----------
        msg = MIMEMultipart()
        msg['Subject'] = Header('AppDailyTask', 'utf-8')
        msg['From'] = Header('peili', 'utf-8')
        msg['To'] = Header('peili', 'utf-8')

        # 添加邮件正文内容
        main_body_info = '''
        <html>
            <h1 style="font-weight:bold;">附件是每日任务执行报告</h1>
            <p><span style="color:green;">绿色</span>代表该APP任务执行成功并断言正确</p>
            <p><span style="color:orange;">橙色</span>代表该APP任务执行成功但断言错误，请查看截图文件或者打开APP确认任务是否完成</p>
            <p><span style="color:red;">红色</span>代表任务执行失败，可能是APP有更新，页面突然有活动/广告弹窗或者网络问题导致，请检查网络和APP</p>
        </html>'''
        msg.attach(MIMEText(main_body_info, 'html', 'utf-8'))

        # 添加附件
        file1 = MIMEText(open(AppTaskReport, 'rb').read(), 'plain', 'utf-8')
        file1['Content-Type'] = 'application/octet-stream'
        file1["Content-Disposition"] = 'attachment; filename="AppTaskReport.html"'  # 这里的filename就是邮件中附件的名字，可以自己命名
        msg.attach(file1)


        # ----------登录并发送----------
        try:
            smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)  # QQ邮箱发送服务器以及端口，SMTP默认端口是25，这里改成465
            smtp.login('123456789@qq.com', '********')  # 如果是QQ邮箱的话，第二个参数不是直接用的密码，用的是QQ邮箱的授权码
            smtp.sendmail('123456789@qq.com', '123456789@qq.com', msg.as_string())  # 前两个参数分别是发送邮箱和接收邮箱
            smtp.quit()
            print('邮件发送成功')
        except smtplib.SMTPException as e:
            print(e)


if __name__ == '__main__':

    process() #打印当前开发进度
    start_appium_server() #启动appium服务
    start_android_devices() #启动模拟器
    time.sleep(15)
    run_tasks() #执行APP任务
    send_mail() #发送邮件
    stop_android_devices() #关闭模拟器
    stop_appium_server()  # 关闭appium服务
