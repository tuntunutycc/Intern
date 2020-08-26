# main.py -- put your code here!
from network import WLAN
import socket
import machine
import ssl
import time
import pycom
import connection
from machine import Pin
from dth import DTH
wlan = WLAN(mode=WLAN.STA)

th = DTH('P3',0)
time.sleep(2)
api_key = '4Y1AM0EW3R2NNC6D'
host = 'api.thingspeak.com'

while not connection.connect():
    connection.connect()


addr = socket.getaddrinfo(host, 80)[0][-1]
while True:
    result = th.read()
    pycom.rgbled(0x001000) # green
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)
    path = 'update?api_key=' + api_key + '&' + 'field1' + '=' + str(result.temperature) + '&' + 'field2' + '=' + str(result.humidity)
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    s.close()
    time.sleep(1800)
