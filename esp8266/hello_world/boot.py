# This file is executed on every boot (including wake-boot from deepsleep)
import gc
import time
import secrets

#import uos
import machine
import network


# uos.dupterm(None, 1) # disable REPL on UART(0)

import esp
esp.osdebug(None)
gc.collect()


def connect_wifi():
    """ connect to a wifi network """
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)  # disable access point

    wifi = network.WLAN(network.STA_IF)

    if not wifi.isconnected():

        print('connecting to ', secrets.ssid)

        wifi.active(True)
        wifi.connect(secrets.ssid, secrets.wifi_pass)
        for retry in range(5):
            if not wifi.isconnected():
                print('waiting ...', retry)
                time.sleep(3)
        if not wifi.isconnected():  # could not connect
            print('Could not connect, rebooting')
            time.sleep(2)
            machine.reset()

    if wifi.isconnected():  # should be connected now
        print('network config:', wifi.ifconfig())
        print('rssi:', wifi.status('rssi'))

    else:  # warn with led and reboot
        print('Connection failed!')
        time.sleep(5)
        print('Restarting')
        machine.reset()


connect_wifi()

#import webrepl
# webrepl.start()
