# SmartOnMyDeck
- [English Version](https://github.com/On-My-Deck/center/blob/main/README.md)
# 概览

`硬件特性`
- ESP32-S3-WROOM-1 ( Wi-Fi, Ble 5 )
- 480x480 圆屏 ( ST7701S )
- 单通道音频 CODEC ( ES8311 )
- 双通道语音 ADC ( ES7210 )
- 防水全频域音腔 [ 8 ohm 3W 30x20 (mm) ]
- 32G USB 存储扩展
- GPIO口扩展芯片 ( AIP5916VB )
- 支持 [SmartKnob](https://github.com/scottbez1/smartknob)操控方式
- 无刷电机：Model A2804-75T
- 锂电池供电 Model 18650
- 5V 充电 USB-C (2.0)

`软件特性`
- 支持 Hue strip and Wiz strip 灯带
- 番茄时间管理
- 语音播放 ( mp3,wave,etc )
- Ftp 文件服务器
- LVGL v8.3.0
- FATFs 文件系统

# 功能开发路线
![RoadMap](https://github.com/On-My-Deck/center/blob/main/doc/RoadMap240422.png)

# 如何使用
`第一次使用`

**固件下载和连接自己的路由**
1. 使用esp32 自动下载模块，连接 esp32s3 的uart0 口
2. 使用Thonny 工具下载固件 (firmware.bin)
3. 启动后 esp32s3 会创建 `AP:` MicroPython-AP ,`key:` 123456789, 使用电脑连接她。
4. 设置 Thonny ( [about Thonny](https://thonny.org/) ) 为 webREPL mode. `url:` ws://192.168.4.1:8266/ `password:` 1234
5. 点击 Thonny 的重连, 建立webREPL 链接后, 可以修改esp32s3中的wifi_config.json 的 essid 和 password 为自己的路由器。
6. 重启esp32s3，会自动连接自己的路由器.

`FTP 服务器的使用`

工具: File zilla client

设置:
- `IP：` esp32s3 IP `port:` ftp server default port
- `user:` esp32 `password:` esp32
- transfer settings -> maximum number of connections 1

# 演示视频
# 参考工程
[esp idf](https://github.com/espressif/esp-idf)

[esp-dev-kits/esp32-s3-lcd-ev-board](https://github.com/espressif/esp-dev-kits/tree/master/esp32-s3-lcd-ev-board)

[MicroPython](https://github.com/micropython/micropython)

[LVGL](https://github.com/lvgl/lvgl)

[scottbez1/smartknob](https://github.com/scottbez1/smartknob)

# 芯片资料
- [ES8311](https://github.com/On-My-Deck/center/blob/main/files/ES8311%20PB.pdf)
- [ES7210](https://github.com/On-My-Deck/center/blob/main/files/Everest-ES7210.pdf)

