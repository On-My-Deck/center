# 导入 network 模块
import network
import time
import wiz_strip
import json

class wizStripCmd:
    WIZ_STRIP_API_EVENT_START_DISCOVER = 0
    WIZ_STRIP_API_EVENT_GET_DISCOVER_IP = 1
    WIZ_STRIP_API_EVENT_GET_USER_NAME = 2
    WIZ_STRIP_API_EVENT_SET_STATE = 3
    WIZ_STRIP_API_EVENT_SET_BRIGHTNESS = 4
    WIZ_STRIP_API_EVENT_SET_COLOR_TEMPERATURE = 5
    WIZ_STRIP_API_EVENT_SET_RGB_COLOR = 6
    WIZ_STRIP_API_EVENT_SET_RG_COLOR = 7
    WIZ_STRIP_API_EVENT_SET_RB_COLOR = 8
    WIZ_STRIP_API_EVENT_SET_GB_COLOR = 9
    WIZ_STRIP_API_EVENT_SET_R_COLOR = 10
    WIZ_STRIP_API_EVENT_SET_G_COLOR = 11
    WIZ_STRIP_API_EVENT_SET_B_COLOR = 12
    WIZ_STRIP_API_EVENT_SET_SCENE = 13
    WIZ_STRIP_API_EVENT_GET_STATUS = 14

    WIZ_STRIP_API_EVENT_START_DISCOVER_BACK = 15
    WIZ_STRIP_API_EVENT_GET_USER_NAME_BACK = 16
    WIZ_STRIP_API_EVENT_GET_LIGHT_INFO_BACK = 17

    WIZ_STRIP_API_EVENT_MAX = 18


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
    #wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_START_DISCOVER, "{}")
        ip = wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_GET_DISCOVER_IP, "{}")
        print(ip)
        print(ip)
        
def is_legal_wifi(essid, password):
    '''
    判断WIFI密码是否合法
    '''
    if len(essid) == 0 or len(password) == 0:
        return False
    return True

def do_connect():
    # 尝试读取配置文件wifi_confi.json,这里我们以json的方式来存储WIFI配置
    # wifi_config.json在根目录下
    
    # 若不是初次运行,则将文件中的内容读取并加载到字典变量 config
    try:
        with open('wifi_config.json','r') as f:
            config = json.loads(f.read())
    # 若初次运行,则将进入excpet,执行配置文件的创建        
    except:
        essid = ''
        password = ''

        while True:
#             essid = input('wifi name:') # 输入essid
#             password = input('wifi passwrod:') # 输入password
            essid = "CU_GhE9"
            password = "32y6xs4u"
            if is_legal_wifi(essid, password):
                config = dict(essid=essid, password=password) # 创建字典
                with open('wifi_config.json','w') as f:
                    f.write(json.dumps(config)) # 将字典序列化为json字符串,存入wifi_config.json
                break
            else:
                print('ERROR, Please Input Right WIFI')
    
    #以下为正常的WIFI连接流程        
    wifi = network.WLAN(network.STA_IF)
    if not wifi.isconnected(): 
        print('connecting to network...')
        wifi.active(True) 
        wifi.connect(config['essid'], config['password']) 
#         import time

        for i in range(200):
            print('第{}次尝试连接WIFI热点'.format(i))
            if wifi.isconnected():
                break
            time.sleep_ms(100) #一般睡个5-10秒,应该绰绰有余
        
        if not wifi.isconnected():
            wifi.active(False) #关掉连接,免得repl死循环输出
            print('wifi connection error, please reconnect')
            import os
            # 连续输错essid和password会导致wifi_config.json不存在
            try:
                os.remove('wifi_config.json') # 删除配置文件
            except:
                pass
            do_connect() # 重新连接
        else:
            print('network config:', wifi.ifconfig())
    else:
        print('network config:', wifi.ifconfig())
            
def discoverWizStrip():
    wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_START_DISCOVER, "{}")
    return wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_GET_DISCOVER_IP, "{}")
    
    for i in range(200):
        print('第{}次获取wizStrp IP'.format(i))
        ip = wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_GET_DISCOVER_IP, "{}")
        print(ip)
        #ipJson = json.loads(ip)
        #if ipJson["discover"] is not None:
        if ip is not None:
            return 1
            break
#         time.sleep_ms(1000) #一般睡个5-10秒,应该绰绰有余
    return 0
if __name__ == '__main__':
    do_connect()
    #ip = discoverWizStrip()
    ip = wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_GET_DISCOVER_IP, "{}")
    print(ip)
    
    ipJson = json.loads(ip)
    if ipJson['discover'] == "0.0.0.0" :
        wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_START_DISCOVER, "{}")
        print("正在获取WizStrp IP...\n")
        time.sleep(5)
        ip = wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_GET_DISCOVER_IP, "{}")
        print(f"Get ip {ip}\n")
    
    
    time.sleep(2)
    ret = wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_SET_STATE,"{\"on\":1}")
    print(f"back {ret}\n")
#     time.sleep(1)
#     while True:
#         r = int(input('\nR:'))
#         g = int(input('G:'))
#         b = int(input('B:'))
#         
#         if r == 0:
#             break
#         
#         ret = wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_SET_RGB_COLOR, f"{{\"r\":{r},\"g\":{g},\"b\":{b}}}")
#         print(f"back {ret}\n")
#     time.sleep_ms(120)
#     rgb = 0
#     while True:
#         rgb += 1
#         if rgb > 0xFFFFFF:
#             rgb = 0
#             
#         r = rgb&0xFF
#         g = (rgb>>8)&0xFF
#         b = (rgb>>16)&0xFF
#         ret = wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_SET_RGB_COLOR,f"{{\"r\":{r},\"g\":{g},\"b\":{b}}}")
#         print(f"back {ret}\n")
#         time.sleep_ms(50)
    
    ret = wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_SET_RGB_COLOR,"{\"r\":250,\"g\":0,\"b\":0}")
    print(f"back {ret}\n")
    time.sleep_ms(120)
    
    ret = wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_SET_RGB_COLOR,"{\"r\":0,\"g\":250,\"b\":0}")
    print(f"back {ret}\n")
    time.sleep_ms(120)
    
    ret = wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_SET_RGB_COLOR,"{\"r\":0,\"g\":0,\"b\":250}")
    print(f"back {ret}\n")
    time.sleep_ms(120)
#     ret = wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_SET_RGB_COLOR,"{\"r\":100,\"g\":0,\"b\":0}")
#     ret = wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_SET_RGB_COLOR,"{\"r\":120,\"g\":0,\"b\":0}")
#     ret = wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_SET_RGB_COLOR,"{\"r\":140,\"g\":0,\"b\":0}")
#     ret = wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_SET_RGB_COLOR,"{\"r\":160,\"g\":0,\"b\":0}")
#     ret = wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_SET_RGB_COLOR,"{\"r\":180,\"g\":0,\"b\":0}")
#     ret = wiz_strip.wiz_strip_handle(wizStripCmd.WIZ_STRIP_API_EVENT_SET_RGB_COLOR,"{\"r\":200,\"g\":0,\"b\":0}")
    
    
#     print(f"back {ret}")
    #time.sleep(10)
    print("Turn off\n")
    
    print(ret)
