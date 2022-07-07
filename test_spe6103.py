import serial,time

with serial.Serial('/dev/ttyUSB1',115200,timeout=5) as ser:
	ser.write(b'*IDN?\r')
	line=ser.readline()
	print(line.decode('utf-8'))