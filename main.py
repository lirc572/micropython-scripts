import sleep_as_rochor
from morse import Morse
from machine import Pin

onoff = '0'
with open('onoff.b', 'r') as f:
    onoff = f.read()
with open('onoff.b', 'w') as f:
    f.write('1' if onoff=='0' else '0')

def do_connect():
    from machine import RTC
    import network, ntptime
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('????????', '????????')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    ntptime.settime()
    print(RTC().datetime())
    return wlan.ifconfig()[0]
    

ip_address = do_connect()

p00 = Pin(0, Pin.OUT)  #gnd of buzzer
p02 = Pin(2, Pin.OUT)  #dio of buzzer
p15 = Pin(15, Pin.OUT) #vcc of buzzer
p13 = Pin(13, Pin.IN, Pin.PULL_UP) #btn pin (active low)
p00.off()
p15.on()
p02.on() #off

m = Morse(p02)
m.fromStr(ip_address)
m.play()

sleep_as_rochor.main(p02, onoff)
