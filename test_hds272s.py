# could not get py-visa working
# went with pyusb instead
# hds272s is recognized when plugged in
# a "usbusers" group is added, and a new udev rule is added

import usb.core
import usb.util

import matplotlib
matplotlib.use('Gtk3Agg')
import matplotlib.pyplot as plt

import ctypes
import time

# find our device, OWON HDS272S
dev = usb.core.find(idVendor=0x5345, idProduct=0x1234)
# without this line, after first read, resource will be occupied indefinitely
dev.reset()

# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = intf[1]
#assert ep is not None

def get_timebase():
    dev.write(0x01, b':HORizontal:SCALe?')
    res=dev.read(0x81,64,1000)
    print(res.tobytes().decode('utf-8'))

    # dev.write(0x01, b':HORizontal:SCALe 100us')

def get_channel():
    dev.write(0x01, b':CH2:DISPlay?')
    res=dev.read(0x81,64,1000)
    print(res.tobytes().decode('utf-8'))

def get_measurement():
    # individual measurement can be run like this:
    # dev.write(0x01, b':MEASurement:CH1:FREQuency?')
    items = ['MAX', 'MIN', 'PKPK', 'VAMP', 'AVERage', 'PERiod', 'FREQuency']

    for item in items:
        cmd = ':MEASurement:CH1:' + item + '?'
        dev.write(0x01, bytes(cmd, 'utf-8'))
        res=dev.read(0x81,64,1000)
        print(res.tobytes().decode('utf-8'))

def get_wave():
    dev.write(0x01, b':DATa:WAVe:SCReen:HEAD?')
    res=dev.read(0x81,2000,1000)
    print(res.tobytes().decode('utf-8'))
    
    dev.write(0x01, b':DATa:WAVe:SCReen:CH1?')
    res=dev.read(0x81,2000,1000)
    # shift all values by 50
    print(res)
    # for i in range(res.buffer_info()[1]):
    #     res[i] = ctypes.c_uint8(res[i]+128).value
    # print(res)

def plot_wave():
    dev.write(0x01, b':DATa:WAVe:SCReen:CH1?')
    res=dev.read(0x81,2000,1000)

    for i in range(res.buffer_info()[1]):
        res[i] = ctypes.c_uint8(res[i]+127).value

    fig,ax = plt.subplots()
    # first data point always looks problematic
    ax.plot(res[1:603])
    plt.show()

def wave_gen():
    dev.write(0x01, b':FUNCtion?')
    res=dev.read(0x81,2000,1000)
    print(res.tobytes().decode('utf-8'))

    items = ['SINE', 'SQUare', 'RAMP']

    for item in items:
        cmd = ':FUNCtion ' + item
        dev.write(0x01, bytes(cmd, 'utf-8'))
        # res=dev.read(0x81,64,1000)
        # print(res.tobytes().decode('utf-8'))
        time.sleep(2)



def main():
    # write to endpoint address 0x01, read from endpoint address 0x81
    dev.write(0x01, b'*IDN')
    res=dev.read(0x81,64,1000)
    print(res.tobytes().decode('utf-8'))

    # get_timebase()
    # get_channel()
    # get_measurement()
    # get_wave()
    # plot_wave()
    wave_gen()

if __name__ == "__main__":
    main()