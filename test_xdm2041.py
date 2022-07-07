# a USB-RS232 (ultimate solutions, blue box) is required to make the connection
# no driver needed for Linux system
# recognized as ttyUSB0 when plugged in
# XDM2041 goes into remote mode upon receiving 'SYSTem:REMote'
#
# also works with direct RS232 connection with optiplex 7040
# recognized as ttyS0 under Linux
# 'sudo dmesg|grep ttyS' to find out


import serial, time

with serial.Serial('/dev/ttyS0',115200,timeout=5) as ser:
	ser.write(b'SYSTem:REMote\r')
	ser.write(b'*IDN?\r')
	line=ser.readline()
	print(line.decode('utf-8'))

	ser.write(b'CONF:VOLT\r')

	ser.write(b'FUNC?\r')
	line=ser.readline()
	print(line.decode('utf-8'))

	ser.write(b'MEAS?\r')
	line=ser.readline()
	print(line.decode('utf-8'))

	ser.write(b'CONF:CURR\r')

	ser.write(b'FUNC?\r')
	line=ser.readline()
	print(line.decode('utf-8'))

	ser.write(b'MEAS?\r')
	line=ser.readline()
	print(line.decode('utf-8'))

	ser.write(b'CONF:RES AUTO\r')

	ser.write(b'FUNC?\r')
	line=ser.readline()
	print(line.decode('utf-8'))

	time.sleep(5)

	ser.write(b'MEAS?\r')
	line=ser.readline()
	print(line.decode('utf-8'))