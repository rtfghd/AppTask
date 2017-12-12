@echo off
title stop_appium_server
tasklist -v | find "start_appium_server">nul
if %errorlevel%==0 (
taskkill -fi "WINDOWTITLE eq start_appium_server"
)