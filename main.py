from hcsr04 import HCSR04
from time import sleep
import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
import network

try:
    from requests import get, post
except:
    from urequests import get, post

try:
    from json import loads
except:
    from ujson import loads

# Configurações de rede
SSID = 'MaisVerde_2H'
PASSWORD = 'mod48pqr'

apiToken = "********:********************"
chatID = "************"
botAPI_endpoint = f'https://api.telegram.org/bot{apiToken}'

def sendTelegramMessage(message):
    jsonResponse = loads(get(f'{botAPI_endpoint}/sendMessage?chat_id={chatID}&text={message}').text)

# Conectando-se à rede Wi-Fi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Conectando à rede Wi-Fi...')
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            pass
    print('Conexão Wi-Fi estabelecida')
    print('Configurações de rede:', wlan.ifconfig())

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

#initializing the I2C method for ESP32
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

# ESP32
sensor = HCSR04(trigger_pin=15, echo_pin=2, echo_timeout_us=10000)

infra = Pin(18, machine.Pin.IN)

led = Pin(2, machine.Pin.OUT)
i = 0
cont = 0
def func():
    led.on()
    ultraSonic = sensor.distance_cm()
    sleep(0.2)
    led.off()
    if(ultraSonic > 0 and ultraSonic < 5):
        return 1
    else:
        return 0

connect_to_wifi()

while True:

    if(func() > 0):
        while(True):
            if(not infra.value()):
                cont = cont + 1
                lcd.clear()
                lcd.putstr("Pessoas na sala:")
                lcd.putstr(str(cont))
                sendTelegramMessage("Pessoas na sala: " + str(cont))
                while(func()> 0 or not infra.value()):
                    pass
                break
    if(not infra.value()):
        while(True):
            if(func() > 0):
                if(cont > 0):
                    cont = cont - 1
                lcd.clear()
                lcd.putstr("Pessoas na sala:")
                lcd.putstr(str(cont))
                sendTelegramMessage("Pessoas na sala: " + str(cont))
                while(func() > 0 or not infra.value()):
                    pass
                break
    print(cont)
