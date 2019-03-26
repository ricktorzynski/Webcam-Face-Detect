import struct
import smbus
import sys

# 0 = /dev/i2c-0 (port I2C0)
# 1 = /dev/i2c-1 (port I2C1)
bus = smbus.SMBus ( 1 )

# MAX17043
address = 0x36

def readVoltage ( bus, address = address ):
  
    read      = bus.read_word_data (address, 2 )
    swapped   = struct.unpack ( "<H", struct.pack ( ">H", read ) )[0]
    voltage   = swapped * 78.125 / 10000000
    return voltage

def readCapacity ( bus, address = address ):
   
    read      = bus.read_word_data ( address, 4 )
    swapped   = struct.unpack ( "<H", struct.pack ( ">H", read ) )[0]
    capacity  = swapped/256
    return capacity

print ( '%(volt).2fV (%(cap)i%%)' % ('volt': readVoltage (bus ), 'cap': readCapacity ( bus ) ) );