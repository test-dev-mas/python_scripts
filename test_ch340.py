# identification of CH340 on Mega Pro 2560
# instantiation of serial.Serial class

import serial
import serial.tools.list_ports
import time

class Arduino(serial.Serial):
    def __init__(self):
        super().__init__()

        self.arduino_port = None

        for port in serial.tools.list_ports.comports():
            if port.pid == 0x7523 and port.vid == 0x1a86:
                self.arduino_port = port.device

        if self.arduino_port is None:
            raise ValueError('Device not found')

        self.port = self.arduino_port
        self.baudrate = 115200
        self.timeout = 10
        self.open()

def main():
    arduino = Arduino()

    while True:
        arduino.write(b'hell world!')
        time.sleep(1)

if __name__ == "__main__":
    main()