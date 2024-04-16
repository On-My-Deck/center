# 导入 network 模块
import network
import time
import wifiConnect
import hue_bridge_strip
import json



class hueBridgeStripCmd:
    HUE_BRIDGE_STRIP_API_EVENT_START_DISCOVER = 0
    HUE_BRIDGE_STRIP_API_EVENT_GET_DISCOVER_IP = 1
    HUE_BRIDGE_STRIP_API_EVENT_CREATE_NEW_USER = 2
    HUE_BRIDGE_STRIP_API_EVENT_GET_USER_NAME = 3
    HUE_BRIDGE_STRIP_API_EVENT_GET_ALL_LIGHTS = 4
    HUE_BRIDGE_STRIP_API_EVENT_GET_LIGHT_INFO = 5
    HUE_BRIDGE_STRIP_API_EVENT_SET_STATE = 6
    HUE_BRIDGE_STRIP_API_EVENT_CTRL_SWITCH = 7
    HUE_BRIDGE_STRIP_API_EVENT_SET_BRIGHTNESS = 8
    HUE_BRIDGE_STRIP_API_EVENT_SET_COLOR_TEMPERATURE = 9
    HUE_BRIDGE_STRIP_API_EVENT_SET_SATURATION = 10
    HUE_BRIDGE_STRIP_API_EVENT_SET_HUE_COLOR = 11 
    HUE_BRIDGE_STRIP_API_EVENT_SET_XY_COLOR = 12

    HUE_BRIDGE_STRIP_API_EVENT_SET_HUE_SAT_BRI_COLOR = 13
    HUE_BRIDGE_STRIP_API_EVENT_SET_HUE_SAT_COLOR = 14
    HUE_BRIDGE_STRIP_API_EVENT_SET_HUE_BRI_COLOR = 15
    HUE_BRIDGE_STRIP_API_EVENT_SET_SAT_BRI_COLOR = 16

    HUE_BRIDGE_STRIP_API_EVENT_SET_XY_CT_BRI_COLOR = 17
    HUE_BRIDGE_STRIP_API_EVENT_SET_XY_CT_COLOR = 18
    HUE_BRIDGE_STRIP_API_EVENT_SET_XY_BRI_COLOR = 19
    HUE_BRIDGE_STRIP_API_EVENT_SET_CT_BRI_COLOR = 20

    
    HUE_BRIDGE_STRIP_API_EVENT_SET_SCENE = 21
    HUE_BRIDGE_STRIP_API_EVENT_GET_STATUS = 22
    HUE_BRIDGE_STRIP_API_EVENT_GET_STATUS_BACK = 23

    HUE_BRIDGE_STRIP_API_EVENT_START_DISCOVER_BACK = 24
    HUE_BRIDGE_STRIP_API_EVENT_GET_USER_NAME_BACK = 25
    HUE_BRIDGE_STRIP_API_EVENT_GET_LIGHT_INFO_BACK = 26

    HUE_BRIDGE_STRIP_API_EVENT_MAX = 27


def test() :
# 创建 WIFI 连接对象
    wlan = network.WLAN(network.STA_IF)
# 激活 wlan 接口。True 是激活，False 关闭
    wlan.active(True)
# 扫描允许访问的 SSID 
    wlan.scan()
# 检查设备是否已经连接成功
    wlan.isconnected()    
# WIFI 连接，ssid 是账号，password 是密码
    wlan.connect('CU_GhE9', '32y6xs4u')
# 获取接口的 mac 地址，也就是物理地址
#wlan.config('mac')
# 获取接口的 IP、子网掩码(netmask)、网关(gw)、DNS 地址
    print(wlan.ifconfig())

    if wlan.isconnected() :
    #hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_START_DISCOVER, "{}")
        ip = hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_GET_DISCOVER_IP, "{}")
        print(ip)
        print(ip)
        

            
def discoverWizStrip():
    hue_bridge_strip.hue_bridge_strip_handle(HUE_BRIDGE_STRIP_API_EVENT_SET_HUE_SAT_BRI_COLOR.HUE_BRIDGE_STRIP_API_EVENT_START_DISCOVER, "{}")
    return hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_GET_DISCOVER_IP, "{}")
    
    for i in range(200):
        print('第{}次获取wizStrp IP'.format(i))
        ip = hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_GET_DISCOVER_IP, "{}")
        print(ip)
        #ipJson = json.loads(ip)
        #if ipJson["discover"] is not None:
        if ip is not None:
            return 1
            break
#         time.sleep_ms(1000) #一般睡个5-10秒,应该绰绰有余
    return 0
if __name__ == '__main__':
    wifiConnect.do_connect()
    #ip = discoverWizStrip()
    ip = hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_GET_DISCOVER_IP, "{}")
    print(ip)
    
    ipJson = json.loads(ip)
    hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_START_DISCOVER, "{}")
    print("正在获取 Hue Bridge Strip IP...\n")
#     time.sleep(5)
    if ipJson['discover'] == "0.0.0.0" :
        hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_START_DISCOVER, "{}")
        print("正在获取 Hue Bridge Strip IP...\n")
        time.sleep(5)
        ip = hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_GET_DISCOVER_IP, "{}")
        print(f"Get ip {ip}\n")
    
    
    time.sleep(2)
    ret = hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_CTRL_SWITCH,"{\"on\":1}")
    print(f"back {ret}\n")
    time.sleep(1)
#     time.sleep(1)
#     while True:
#         r = int(input('\nR:'))
#         g = int(input('G:'))
#         b = int(input('B:'))
#         
#         if r == 0:
#             break
#         
#         ret = hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_SET_HUE_SAT_BRI_COLOR, f"{{\"r\":{r},\"g\":{g},\"b\":{b}}}")
#         print(f"back {ret}\n")
#     time.sleep_ms(120)
#     hsb = 0
#     while True:
#         hsb += 1
#         if hsb > 0xFFFFFF:
#             hsb = 0
#             
#         hue = hsb&0xFF
#         sat = (hsb>>8)&0xFF
#         bri = (hsb>>16)&0xFF
#         ret = hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_SET_HUE_SAT_BRI_COLOR,f"{{\"hue\":{hue},\"sat\":{sat},\"bri\":{bri}}}")
#         print(f"back {ret}\n")
#         time.sleep_ms(50)
    
    ret = hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_SET_HUE_SAT_BRI_COLOR,"{\"hue\":50000,\"sat\":100,\"bri\":250}")
    print(f"back {ret}\n")
    time.sleep_ms(1000)
#     
    ret = hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_SET_HUE_SAT_BRI_COLOR,"{\"hue\":50000,\"sat\":100,\"bri\":254}")
    print(f"back {ret}\n")
    time.sleep_ms(1000)
#     
#     ret = hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_SET_HUE_SAT_BRI_COLOR,"{\"hue\":50000,\"sat\":100,\"bri\":250}")
#     print(f"back {ret}\n")
#     time.sleep_ms(1000)
#     ret = hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_SET_HUE_SAT_BRI_COLOR,"{\"r\":100,\"g\":0,\"b\":0}")
#     ret = hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_SET_HUE_SAT_BRI_COLOR,"{\"r\":120,\"g\":0,\"b\":0}")
#     ret = hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_SET_HUE_SAT_BRI_COLOR,"{\"r\":140,\"g\":0,\"b\":0}")
#     ret = hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_SET_HUE_SAT_BRI_COLOR,"{\"r\":160,\"g\":0,\"b\":0}")
#     ret = hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_SET_HUE_SAT_BRI_COLOR,"{\"r\":180,\"g\":0,\"b\":0}")
#     ret = hue_bridge_strip.hue_bridge_strip_handle(hueBridgeStripCmd.HUE_BRIDGE_STRIP_API_EVENT_SET_HUE_SAT_BRI_COLOR,"{\"r\":200,\"g\":0,\"b\":0}")
    
    
#     print(f"back {ret}")
    #time.sleep(10)
    while True:
        print("Turn off\n")
        time.sleep(1)
    
    print(ret)
