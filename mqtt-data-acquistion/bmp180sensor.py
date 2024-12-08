import time
import fcntl
import struct
from ctypes import c_short

# I2C settings
DEVICE = 0x77  # Default device I2C address
I2C_SLAVE = 0x0703  # I2C_SLAVE operation

# Open the I2C device
i2c_file = open('/dev/i2c-1', 'rb+', buffering=0)
fcntl.ioctl(i2c_file, I2C_SLAVE, DEVICE)


def getShort(data, index):
    """Return two bytes from data as a signed 16-bit value."""
    return c_short((data[index] << 8) + data[index + 1]).value


def getUshort(data, index):
    """Return two bytes from data as an unsigned 16-bit value."""
    return (data[index] << 8) + data[index + 1]


def readBytes(reg, length):
    """Read a sequence of bytes from a register."""
    i2c_file.write(bytes([reg]))
    return list(i2c_file.read(length))


def writeByte(reg, value):
    """Write a byte to a register."""
    i2c_file.write(bytes([reg, value]))
    
def readBmp180():
    """Read temperature, pressure, and altitude from BMP180 sensor."""
    # Register Addresses
    REG_CALIB = 0xAA
    REG_MEAS = 0xF4
    REG_MSB = 0xF6
    CRV_TEMP = 0x2E
    CRV_PRES = 0x34
    OVERSAMPLE = 3  # 0 - 3

    # Read calibration data
    cal = readBytes(REG_CALIB, 22)
    AC1 = getShort(cal, 0)
    AC2 = getShort(cal, 2)
    AC3 = getShort(cal, 4)
    AC4 = getUshort(cal, 6)
    AC5 = getUshort(cal, 8)
    AC6 = getUshort(cal, 10)
    B1 = getShort(cal, 12)
    B2 = getShort(cal, 14)
    MB = getShort(cal, 16)
    MC = getShort(cal, 18)
    MD = getShort(cal, 20)

    # Read raw temperature
    writeByte(REG_MEAS, CRV_TEMP)
    time.sleep(0.005)
    raw_temp = readBytes(REG_MSB, 2)
    UT = (raw_temp[0] << 8) + raw_temp[1]

    # Read raw pressure
    writeByte(REG_MEAS, CRV_PRES + (OVERSAMPLE << 6))
    time.sleep(0.04)
    raw_pres = readBytes(REG_MSB, 3)
    UP = ((raw_pres[0] << 16) + (raw_pres[1] << 8) + raw_pres[2]) >> (8 - OVERSAMPLE)

    # Calculate temperature
    X1 = ((UT - AC6) * AC5) >> 15
    X2 = (MC << 11) / (X1 + MD)
    B5 = X1 + X2
    temperature = int(B5 + 8) >> 4
    temperature = temperature / 10.0

    # Calculate pressure
    B6 = int(B5 - 4000)
    X1 = (B2 * ((B6 * B6) >> 12)) >> 11
    X2 = (AC2 * B6) >> 11
    X3 = X1 + X2
    B3 = (((AC1 * 4 + X3) << OVERSAMPLE) + 2) >> 2
    X1 = (AC3 * B6) >> 13
    X2 = (B1 * ((B6 * B6) >> 12)) >> 16
    X3 = ((X1 + X2) + 2) >> 2
    B4 = (AC4 * (X3 + 32768)) >> 15
    B7 = (UP - B3) * (50000 >> OVERSAMPLE)
    pressure = (B7 * 2) / B4
    pressure = int(pressure)
    X1 = (pressure >> 8) * (pressure >> 8)
    X1 = (X1 * 3038) >> 16
    X2 = (-7357 * pressure) >> 16
    pressure = int(pressure + ((X1 + X2 + 3791) >> 4))

    # Calculate altitude
    altitude = 44330.0 * (1.0 - pow(pressure / 101325.0, 1.0 / 5.255))
    altitude = round(altitude, 2)

    return(temperature, pressure, altitude)
