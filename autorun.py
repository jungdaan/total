from scapy import *
import os
import time
import sys

interface = "wlan1"
AP_Found = 0

channel=0

if __name__ == '__main__':
	os.system("ifconfig " + interface + " down")
	os.system("iwconfig " + interface + " mode mon")
	os.system("ifconfig " + interface + " up")

	try:
		with open("/pjhs/autorun_setting", "rt") as f:
			settings = f.read().split()
			encrypt = settings[0]
			essid = settings[1]
			psk = settings[2]
			channel = settings[3]
	except:
		print("There is no default setting")
		sys.exit()


	os.system("iwconfig {} channel {}".format(interface, channel))
	print("ESSID : {}, Password : {}, Channel : {}".format(essid, psk, channel))
	

	dot11_cmd = "/pjhs/dot11decrypt/build/dot11decrypt "
	dot11_cmd += ("{} {}:{}:{}".format(interface, encrypt, essid, psk))
	os.system(dot11_cmd)

