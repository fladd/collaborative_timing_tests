#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
"""
Detect any connected USB2TTL8 devices by checking for available
serial ports and seeing if any respond appropriately to a GET CONFIG\n command.
Prints name, device serial number, and serial port for each device found.
"""
from __future__ import absolute_import, division, print_function

import serial
import os
import json


def getSerialPorts():
    available = []
    if os.name == 'nt':  # Windows
        for i in range(1, 512):
            try:
                sport = 'COM' + str(i)
                s = serial.Serial(sport, baudrate=128000)
                available.append(sport)
                s.close()
            except (serial.SerialException, ValueError):
                pass
    else:  # Mac / Linux
        from serial.tools import list_ports
        available = [port[0] for port in list_ports.comports()]
    return available


def getUSB2TTL8Devices():
    devices = []
    available = getSerialPorts()
    for p in available:
        try:
            mkey_sport = serial.Serial(p, baudrate=128000, timeout=1.0)
            mkey_sport.write(b"GET CONFIG\n")
            rx_data = mkey_sport.readline()
            if rx_data:
                rx_data = rx_data[:-1].strip()
                try:
                    mkconf = json.loads(rx_data)
                    if mkconf.get("model_name","") == "USB2TTL8":
                        mkconf['port'] = p
                        devices.append(mkconf)
                except:
                    raise RuntimeError("ERROR: {}".format(rx_data))
            mkey_sport.close()
        except:
            pass
    return devices

if __name__ == '__main__':
    mkdevs = getUSB2TTL8Devices()
    for mkdev in mkdevs:
        print()
        print("USB2TTL8 Device:")
        print("\tName:\t\t{}".format(mkdev.get('name')))
        print("\tSerial Port:\t{}".format(mkdev.get('port')))
        print("\tSerial Number:\t{}".format(mkdev.get('product_serial')))
        print()
