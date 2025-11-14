#!/usr/bin/env python

import spidev

spi = spidev.SpiDev()
spi.open(0, 0)  # bus 0, device 0 (adjust if using CE1)
spi.max_speed_hz = 500000
resp = spi.xfer2([0x00, 0x00, 0x00, 0x00])  # send dummy bytes, expect response
print(resp)

resp = spi.xfer2([0x0F | 0x80]) + spi.xfer2([0x00])  # Read command + read response
print(resp)