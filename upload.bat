::使用adb调试工具来上传文件的脚本
adb devices
adb root
adb remount
adb push Z:\codedown\AndroidR\out\target\product\redi\vendor\bin\hw\dtvkitserver  /vendor/bin/hw/
adb shell sync
ping 127.0.0.1 -n 5 > nul
adb reboot