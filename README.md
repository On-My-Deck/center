# SmartOnMyDeck
# Over View

`HardWare Feature`
- ESP32-S3-WROOM-1 ( Wi-Fi, Ble 5 )
- 480x480 round LCD ( ST7701S )
- Mono Audio CODEC ( ES8311 )
- Two Channels Audio ADC ( ES7210 )
- Waterproof full-range multimedia cavity speaker [ 8 ohm 3W 30x20 (mm) ]
- 32G MSC
- Extended GPIO port ( AIP5916VB )
- Support [SmartKnob](https://github.com/scottbez1/smartknob)
- BLDC gimbal motor：Model A2804-75T
- Li-ion battery power supply: Model 18650
- USB-C (2.0) connector for 5V Charging

`SoftWare Feature`
- Support Hue strip and Wiz strip
- Tomato Clock
- Audio Player ( mp3,wave,etc )
- Ftp server
- LVGL v8.3.0
- FATFs

# RoadMap
# How to use
`For the first time`
1. Use esp32 auto download module to connect uart0 of esp32s3
2. Download firmware.bin to esp32s3 using Thonny utility
3. After booting esp32s3 generates the MicroPython-AP, use your PC to connect to this AP.
4. Set Thonny ( [more info about Thonny](https://thonny.org/) ) to webREPL mode. url:ws://192.168.4.1:8266/ password:1234
5. Click Thonny's to restart the backend process, and after successful linking, change the essid and password in wifi_config.json to the Wi-Fi you need to link.
6. Reboot the esp32s3 so that you can link your own router.
# Demo Video
# Reference Projects
[esp idf](https://github.com/espressif/esp-idf)

[esp-dev-kits/esp32-s3-lcd-ev-board](https://github.com/espressif/esp-dev-kits/tree/master/esp32-s3-lcd-ev-board)

[MicroPython](https://github.com/micropython/micropython)

[LVGL](https://github.com/lvgl/lvgl)

[scottbez1/smartknob](https://github.com/scottbez1/smartknob)




# DataSheet
- [ES8311](https://github.com/On-My-Deck/center/blob/main/files/ES8311%20PB.pdf)
- [ES7210](https://github.com/On-My-Deck/center/blob/main/files/Everest-ES7210.pdf)
- 
