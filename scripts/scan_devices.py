#!/usr/bin/env python
import sys
import usb.core
import usb.util

import binascii

# find all usb devices
dev = usb.core.find(find_all=True)

# loop through and pring info
for cfg in dev:
    print(
        "VID:0x{:04x} ".format(cfg.idVendor) +
        "PID:0x{:04x} ".format(cfg.idProduct) +
        f"Man: {usb.util.get_string(cfg, cfg.iManufacturer)} "
    ,end='')
    sn_string = usb.util.get_string(cfg, cfg.iSerialNumber)
    try:
        if sn_string:
            sn_string.encode('ascii')
    except UnicodeEncodeError:
        sn_string = sn_string.encode('utf-8').hex()

    print(f"S/N: {sn_string}")

