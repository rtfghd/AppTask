@echo off
title start_appium_server
cmd /c "appium -a 127.0.0.1 -p 4723 -bp 4728 --chromedriver-port 9519 -U emulator-5554"