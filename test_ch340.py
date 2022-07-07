# identification of CH340 on Mega Pro 2560
# instantiation of serial.Serial class

import serial
import serial.tools.list_ports
import time

arduino_port = None

for port in serial.tools.list_ports.comports():
    if port.pid == 0x7523 and port.vid == 0x1a86:
        arduino_port = port.device

if arduino_port is None:
    raise ValueError('Device not found')

with serial.Serial(arduino_port, 115200, timeout=10) as ser:
    while True:
        ser.write(b'hell world!')
        time.sleep(1)