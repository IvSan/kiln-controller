#!/usr/bin/env python

# import spidev
#
# spi = spidev.SpiDev()
# spi.open(0, 0)  # bus 0, device 0 (adjust if using CE1)
# spi.max_speed_hz = 500000
# resp = spi.xfer2([0x00, 0x00, 0x00, 0x00])  # send dummy bytes, expect response
# print(resp)
#
# resp = spi.xfer2([0x0F | 0x80]) + spi.xfer2([0x00])  # Read command + read response
# print(resp)
#
# resp = spi.xfer2([0x8F, 0x00, 0x00, 0x00])  # send read command + 3 dummy bytes to clock out data
# print(resp)  # Should receive 4 bytes including dummy response


import board
import time
from digitalio import DigitalInOut
import adafruit_max31856

spi = board.SPI()
cs = DigitalInOut(board.D5)
sensor = adafruit_max31856.MAX31856(spi, cs)

while True:
    temp = sensor.temperature
    print(f"Temperature: {temp:.2f} °C")
    time.sleep(1)
