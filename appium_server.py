#coding=utf-8
import os,time

def start_appium_server():
    '''启动appium服务'''
    os.system('start start_appium_server.bat')
    print('appium服务启动成功')

def stop_appium_server():
    '''关闭appium服务'''
    os.system('start stop_appium_server.bat')
    print('appium服务已关闭')
