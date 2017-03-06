#! /usr/bin/python

from xbee import XBee
import serial
import time


serial_port = serial.Serial('/dev/ttyUSB0',9600)

def print_data(data):
       
    print data
    #xbee.tx(dest_addr = '\x00\x00', data=data['rf_data'])

xbee = XBee(serial_port,callback=print_data)
while 1:
        try:
                time.sleep(0.001)
                  
                
        except KeyboardInterrupt:
                                break
xbee.halt()
serial_port.close

